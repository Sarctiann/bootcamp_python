from pydantic import BaseModel

__all__ = ["Product"]


class Product(BaseModel):
    id: int | None
    name: str
    description: str
    price: float
    quantity: int
