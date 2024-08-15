__all__ = ["ProductsServiceDependency"]

from typing import Annotated

from fastapi import Depends
from pydantic_mongo import PydanticObjectId

from ..config import COLLECTIONS, db
from ..models import Product, StoredProduct


class ProductsService:
    assert (collection_name := "products") in COLLECTIONS
    collection = db[collection_name]

    @classmethod
    def create_one(cls, product: Product):
        result = cls.collection.insert_one(product.model_dump())
        if result:
            return result.inserted_id
        return None

    @classmethod
    def get_all(cls):
        return [
            StoredProduct.model_validate(product).model_dump()
            for product in cls.collection.find()
        ]

    @classmethod
    def get_one(cls, id: PydanticObjectId):
        if db_product := cls.collection.find_one({"_id": id}):
            return StoredProduct.model_validate(db_product).model_dump()
        else:
            return None

    @classmethod
    def update_one(cls, id: PydanticObjectId, product: Product):
        return cls.collection.find_one_and_update(
            {"_id": id},
            {"$set": product.model_dump()},
            return_document=True,
        )

    @classmethod
    def delete_one(cls, id: PydanticObjectId):
        return cls.collection.find_one_and_delete({"_id": id})


ProductsServiceDependency = Annotated[ProductsService, Depends()]
