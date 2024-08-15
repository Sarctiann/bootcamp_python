__all__ = ["User", "LoginUser", "StoredUser", "CreationUser"]

from typing import Literal

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class User(BaseModel):
    username: str
    role: Literal["admin", "customer", "seller"]
    email: str = Field(default=None)
    image: str = Field(default=None)


class LoginUser(BaseModel):
    username: str
    password: str


class CreationUser(User):
    password: str


class StoredUser(User):
    id: PydanticObjectId = Field(alias="_id")
    hash_password: str
