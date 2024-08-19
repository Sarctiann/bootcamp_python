__all__ = ["Product", "StoredProduct", "UpdationProduct"]

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class Product(BaseModel):
    seller_id: PydanticObjectId
    name: str
    price: float
    quantity: int
    description: str = Field(default=None)
    image: str = Field(default=None)


class UpdationProduct(BaseModel):
    seller_id: PydanticObjectId = Field(default=None)
    name: str = Field(default=None)
    price: float = Field(default=None)
    quantity: int = Field(default=None)
    description: str = Field(default=None)
    image: str = Field(default=None)


class StoredProduct(Product):
    id: PydanticObjectId = Field(alias="_id")
