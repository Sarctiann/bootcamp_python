__all__ = [
    "BaseUser",
    "LoginUser",
    "PublicStoredUser",
    "PrivateStoredUser",
    "CreationUser",
]

from enum import Enum

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class Role(str, Enum):
    admin = "admin"
    customer = "customer"
    seller = "seller"


class BaseUser(BaseModel):
    username: str
    role: Role = Role.admin
    email: str = Field(default=None)
    image: str = Field(default=None)


class CreationUser(BaseUser):
    password: str


class LoginUser(BaseModel):
    username: str
    password: str


class PublicStoredUser(BaseUser):
    id: PydanticObjectId


class PrivateStoredUser(BaseUser):
    id: PydanticObjectId = Field(alias="_id")
    hash_password: str
