from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId

__all__ = ["Product", "StoredProduct"]


class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class StoredProduct(Product):
    id: PydanticObjectId = Field(alias="_id")
