from fastapi import Depends
from ..models.products import Product
from pymongo.collection import Collection
from ..database import db
from typing import Annotated


__all__ = ["product_collection"]


product_collection = Annotated[Collection, Depends(db.products)]
