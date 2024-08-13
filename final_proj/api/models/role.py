from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId


class Role(BaseModel):
    id: PydanticObjectId = Field(alias="_id", default=None)
    name: str
    description: str
