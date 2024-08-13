from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId

__all__ = ["Product"]


class Product(BaseModel):

    id: PydanticObjectId = Field(alias="_id", default=None)
    # De esta forma podemos hacer que el campo sea opcional para el momento de la
    # creacion en nuestro caso
    name: str
    description: str
    price: float
    quantity: int
