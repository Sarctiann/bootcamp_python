__all__ = ["UsersServiceDependency", "UsersService"]


from typing import Annotated

from fastapi import Depends, HTTPException, status
from pydantic_mongo import PydanticObjectId

from ..config import COLLECTIONS, db
from ..models import CreationUser, PrivateStoredUser, PublicStoredUser, UpdationUser
from ..__common_deps import QueryParamsDependency


class UsersService:
    assert (collection_name := "users") in COLLECTIONS
    collection = db[collection_name]

    @classmethod
    def create_one(
        cls, user: CreationUser, hash_password: str, make_it_admin: bool = False
    ):
        try:
            existing_user = cls.get_one(
                username=user.username,
                email=user.email,
            )
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail="User already exists"
                )
        except HTTPException:
            pass

        insert_user = user.model_dump(exclude={"password"}, exclude_unset=True)
        insert_user.update(hash_password=hash_password)

        if make_it_admin:
            insert_user.update(role="admin")

        result = cls.collection.insert_one(insert_user)
        if result:
            return str(result.inserted_id)
        return None

    @classmethod
    def get_all(cls, params: QueryParamsDependency):
        return [
            PublicStoredUser.model_validate(user).model_dump()
            for user in params.query_collection(cls.collection)
        ]

    @classmethod
    def get_one(
        cls,
        *,
        id: PydanticObjectId | None = None,
        username: str | None = None,
        email: str | None = None,
        with_password: bool = False,
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
            return (
                PrivateStoredUser.model_validate(db_user).model_dump()
                if with_password
                else PublicStoredUser.model_validate(db_user).model_dump()
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

    @classmethod
    def update_one(cls, id: PydanticObjectId, user: UpdationUser):
        print(user.model_dump())
        document = cls.collection.find_one_and_update(
            {"_id": id},
            {"$set": user.model_dump(exclude={"password"}, exclude_unset=True)},
            return_document=True,
        )

        if document:
            return PublicStoredUser.model_validate(document).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

    @classmethod
    def update_password(cls, id: PydanticObjectId, hash_password: str):
        document = cls.collection.find_one_and_update(
            {"_id": id},
            {"$set": {"hash_password": hash_password}},
            return_document=True,
        )
        if document:
            return PublicStoredUser.model_validate(document).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

    @classmethod
    def delete_one(cls, id: PydanticObjectId):
        document = cls.collection.find_one_and_delete({"_id": id})
        if document:
            return PublicStoredUser.model_validate(document).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )


UsersServiceDependency = Annotated[UsersService, Depends()]
