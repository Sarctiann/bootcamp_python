__all__ = ["OrdersServiceDependency"]


from typing import Annotated

from fastapi import Depends, HTTPException, status
from pydantic_mongo import PydanticObjectId

from ..__common_deps import QueryParamsDependency
from ..config import COLLECTIONS, db
from ..models import Order, StoredOrder


class OrdersService:
    assert (collection_name := "orders") in COLLECTIONS
    collection = db[collection_name]

    @classmethod
    def create_one(cls, order: Order):
        insertion_document = {
            "custommer_id": {"$oid": order.custommer_id},
            "product_id": {"$oid": order.product_id},
            "price": order.price,
            "quantity": order.quantity,
        }
        document = cls.collection.insert_one(insertion_document)
        if document:
            return str(document.inserted_id)
        return None

    @classmethod
    def get_all(cls, params: QueryParamsDependency):
        return [
            StoredOrder.model_validate(order).model_dump()
            for order in params.query_collection(cls.collection)
        ]

    @classmethod
    def get_one(cls, id: PydanticObjectId, authorized_user_id: PydanticObjectId | None):
        filter_criteria: dict = {"_id": id}
        if authorized_user_id:
            filter_criteria.update(
                {
                    "$or": [
                        {"custommer_id": authorized_user_id},
                        {"seller_id": authorized_user_id},
                    ]
                }
            )

        if db_order := cls.collection.find_one(filter_criteria):
            return StoredOrder.model_validate(db_order).model_dump()
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
            )


OrdersServiceDependency = Annotated[OrdersService, Depends()]
