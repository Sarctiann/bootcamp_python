from pydantic import BaseModel, Field

__all__ = ["Product"]


class Product(BaseModel):

    id: int | None = Field(default=None)
    # De esta forma podemos hacer que el campo sea opcional para el momento de la
    # creacion en nuestro caso
    name: str
    description: str
    price: float
    quantity: int
