from typing import Literal

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId

__all__ = ["User", "StoredUser", "CreationUser"]


class User(BaseModel):
    name: str
    role: Literal["admin", "customer", "seller"]
    email: str = Field(default=None)
    image: str = Field(default=None)


class CreationUser(User):
    password: str


class StoredUser(User):
    id: PydanticObjectId = Field(alias="_id")
    hash_password: str
