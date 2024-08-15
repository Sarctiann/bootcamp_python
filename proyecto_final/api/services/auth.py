__all__ = ["UsersServiceDependency", "AuthServiceDependency", "AuthCredentials"]


from typing import Annotated

from fastapi import Depends, HTTPException, Response, Security, status
from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials
from passlib.context import CryptContext
from pydantic_mongo import PydanticObjectId

from ..config import COLLECTIONS, db, token_expiration_time
from ..models import CreationUser, LoginUser, PrivateStoredUser, PublicStoredUser

access_security = JwtAccessBearer(secret_key="secret_key", auto_error=True)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


class UsersService:
    assert (collection_name := "users") in COLLECTIONS
    collection = db[collection_name]

    @classmethod
    def get_all(cls, role=None):
        filter = {"role": role} if role else {}
        cursor = cls.collection.find(filter)

        return [PublicStoredUser.model_validate(user).model_dump() for user in cursor]

    @classmethod
    def get_one(
        cls,
        id: PydanticObjectId | None = None,
        username: str | None = None,
        email: str | None = None,
    ):
        if all(q is None for q in (id, username, email)):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No id, username or email provided",
            )
        filter = {
            "$or": [
                {"_id": id},
                {"username": username},
                {"email": email},
            ]
        }

        if db_user := cls.collection.find_one(filter):
            return PrivateStoredUser.model_validate(db_user).model_dump()
        else:
            return None

    @classmethod
    def create_one(cls, user: CreationUser):
        existing_user = cls.get_one(
            username=user.username,
            email=user.email,
        )
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="User already exists"
            )

        insert_user = user.model_dump(exclude={"password"})
        insert_user.update(hash_password=get_password_hash(user.password))

        result = cls.collection.insert_one(insert_user)
        if result:
            return result.inserted_id
        return None

    @classmethod
    def login_and_set_access_token(cls, user: LoginUser, response: Response):

        existing_user = cls.get_one(username=user.username)
        if not existing_user or not verify_password(
            user.password, existing_user.get("hash_password")
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found"
            )

        userdata = PublicStoredUser.model_validate(existing_user).model_dump()
        access_token = access_security.create_access_token(
            subject=userdata, expires_delta=token_expiration_time
        )
        access_security.set_access_cookie(response, access_token)

        return {"access_token": access_token}


UsersServiceDependency = Annotated[UsersService, Depends()]
AuthCredentials = Annotated[JwtAuthorizationCredentials, Security(access_security)]


class AuthService:
    def __init__(self, credentials: AuthCredentials):
        self.credentials = credentials

    @property
    def is_admin(self):
        return self.credentials.subject.get("role") == "admin"

    @property
    def is_customer(self):
        return self.credentials.subject.get("role") == "customer"

    @property
    def is_seller(self):
        return self.credentials.subject.get("role") == "seller"


AuthServiceDependency = Annotated[AuthService, Depends()]
