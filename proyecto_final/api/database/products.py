from typing import Annotated

from fastapi import Depends
from pymongo.collection import Collection

from .__base import db

__all__ = ["product_collection"]


product_collection = Annotated[Collection, Depends(lambda: db.products)]
