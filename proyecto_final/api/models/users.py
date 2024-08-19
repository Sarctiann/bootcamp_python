__all__ = [
    "BaseUser",
    "LoginUser",
    "PublicStoredUser",
    "PrivateStoredUser",
    "CreationUser",
    "UpdationUser",
]

from enum import Enum

from pydantic import BaseModel, Field, AliasChoices
from pydantic_mongo import PydanticObjectId


class CreationRole(str, Enum):
    customer = "customer"
    seller = "seller"


class Role(str, Enum):
    admin = "admin"
    customer = "customer"
    seller = "seller"


class BaseUser(BaseModel):
    username: str
    role: Role = Role.customer
    email: str = Field(default=None)
    image: str | None = Field(default=None)


class UpdationUser(BaseUser):
    username: str = Field(default=None)
    role: Role = Field(default=None)
    email: str = Field(default=None)
    image: str | None = Field(default=None)


class CreationUser(BaseUser):
    role: CreationRole = CreationRole.customer
    password: str


class LoginUser(BaseModel):
    username: str
    password: str


class PublicStoredUser(BaseUser):
    id: PydanticObjectId = Field(validation_alias=AliasChoices("_id", "id"))


class PrivateStoredUser(BaseUser):
    id: PydanticObjectId = Field(alias="_id")
    hash_password: str
