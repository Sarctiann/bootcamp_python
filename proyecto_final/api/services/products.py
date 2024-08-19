__all__ = ["ProductsServiceDependency", "ProductsService"]

from typing import Annotated

from fastapi import Depends, HTTPException, status
from pydantic_mongo import PydanticObjectId

from ..config import COLLECTIONS, db
from ..models import Product, StoredProduct, UpdationProduct
from ..__common_deps import QueryParamsDependency


class ProductsService:
    assert (collection_name := "products") in COLLECTIONS
    collection = db[collection_name]

    @classmethod
    def create_one(cls, product: Product):
        insertion_product = product.model_dump(exclude_unset=True)
        result = cls.collection.insert_one(insertion_product)
        if result:
            return str(result.inserted_id)
        return None

    @classmethod
    def get_all(cls, params: QueryParamsDependency):
        return [
            StoredProduct.model_validate(product).model_dump()
            for product in params.query_collection(cls.collection)
        ]

    @classmethod
    def get_one(cls, id: PydanticObjectId):
        if db_product := cls.collection.find_one({"_id": id}):
            return StoredProduct.model_validate(db_product).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )

    @classmethod
    def update_one(cls, id: PydanticObjectId, product: UpdationProduct):
        document = cls.collection.find_one_and_update(
            {"_id": id},
            {"$set": product.model_dump()},
            return_document=True,
        )

        if document:
            return StoredProduct.model_validate(document).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )

    @classmethod
    def delete_one(cls, id: PydanticObjectId):
        document = cls.collection.find_one_and_delete({"_id": id})
        if document:
            return StoredProduct.model_validate(document).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
            )


ProductsServiceDependency = Annotated[ProductsService, Depends()]
