__all__ = ["orders_router"]

from fastapi import APIRouter
from pydantic_mongo import PydanticObjectId

from ..__common_deps import QueryParams, QueryParamsDependency
from ..models import Order, UpdationProduct
from ..services import (
    OrdersServiceDependency,
    ProductsServiceDependency,
    SecurityDependency,
)

orders_router = APIRouter(prefix="/orders", tags=["Orders"])


@orders_router.get("/get_all")
def get_all_orders(
    orders: OrdersServiceDependency,
    security: SecurityDependency,
    params: QueryParamsDependency,
):
    security.is_admin
    return orders.get_all(params)


@orders_router.get("/get_by_seller/{id}")
def get_orders_by_seller_id(
    id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency
):
    auth_user_id = security.auth_user_id
    assert (
        auth_user_id == id or security.auth_user_role == "admin"
    ), "User does not have access to this orders"

    params = QueryParams(filter=f"seller_id={id}")
    return orders.get_all(params)


@orders_router.get("/get_by_customer/{id}")
def get_orders_by_customer_id(
    id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency
):
    auth_user_id = security.auth_user_id
    assert (
        auth_user_id == id or security.auth_user_role == "admin"
    ), "User does not have access to this orders"

    params = QueryParams(filter=f"custommer_id={id}")
    return orders.get_all(params)


@orders_router.get("/get_by_product/{id}")
def get_orders_by_product_id(
    id: PydanticObjectId, security: SecurityDependency, orders: OrdersServiceDependency
):
    auth_user_id = security.auth_user_id if security.auth_user_role != "admin" else None
    return orders.get_one(id, authorized_user_id=auth_user_id)


@orders_router.post("/")
def create_order(
    order: Order,
    orders: OrdersServiceDependency,
    products: ProductsServiceDependency,
    security: SecurityDependency,
):
    security.is_customer_or_raise
    product = products.get_one(order.product_id)
    assert product.get("quantity", 0) >= order.quantity, "Product is out of stock"
    products.update_one(
        order.product_id,
        UpdationProduct(quantity=product["quantity"] - order.quantity),
    )
    result = orders.create_one(order)
    if result:
        return {"result message": f"Order created with id: {result}"}
