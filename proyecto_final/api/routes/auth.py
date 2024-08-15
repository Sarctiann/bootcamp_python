from typing import Annotated

from fastapi import APIRouter, Response, Security
from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials

from ..config import token_expiration_time
from ..models import LoginUser, CreationUser

auth_router = APIRouter(prefix="/auth", tags=["Auth"])
access_security = JwtAccessBearer(secret_key="secret_key", auto_error=True)


@auth_router.post("/register")
def register(user: CreationUser):
    userdata = user.model_dump()


@auth_router.post("/login")
def login_with_cookie(user: LoginUser, response: Response):
    userdata = user.model_dump()
    access_token = access_security.create_access_token(
        subject=userdata, expires_delta=token_expiration_time
    )
    access_security.set_access_cookie(response, access_token)
    return {"access_token": access_token}


auth_dependency = Annotated[JwtAuthorizationCredentials, Security(access_security)]


@auth_router.get("/authenticated_user")
def read_current_user(credentials: auth_dependency):
    return credentials.subject
