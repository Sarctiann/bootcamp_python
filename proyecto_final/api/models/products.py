__all__ = ["Product", "StoredProduct"]

from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class StoredProduct(Product):
    id: PydanticObjectId = Field(alias="_id")
