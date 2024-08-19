__all__ = ["Product", "StoredProduct", "UpdationProduct"]

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class Product(BaseModel):
    name: str
    description: str = Field(default=None)
    price: float
    quantity: int
    image: str = Field(default=None)


class UpdationProduct(BaseModel):
    name: str = Field(default=None)
    description: str = Field(default=None)
    price: float = Field(default=None)
    quantity: int = Field(default=None)
    image: str = Field(default=None)


class StoredProduct(Product):
    id: PydanticObjectId = Field(alias="_id")
