__all__ = ["products_router"]

from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from pydantic_mongo import PydanticObjectId

from ..models import Product, UpdationProduct
from ..services import ProductsServiceDependency, SecurityDependency
from ..__common_deps import QueryParamsDependency

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get("/")
async def list_products(
    products: ProductsServiceDependency, params: QueryParamsDependency
):
    return products.get_all(params)


@products_router.get("/{id}")
async def get_product(id: PydanticObjectId, products: ProductsServiceDependency):
    return products.get_one(id) or JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": f"Product with id: {id}, was not found."},
    )


@products_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(
    product: Product,
    products: ProductsServiceDependency,
    security: SecurityDependency,
):
    security.is_seller_or_raise
    inserted_id = products.create_one(product)
    return {"result message": f"Product created with id: {inserted_id}"}


@products_router.put("/{id}")
async def update_product(
    id: PydanticObjectId, product: UpdationProduct, products: ProductsServiceDependency
):
    return products.update_one(id, product)


@products_router.delete("/{id}")
async def delete_product(id: PydanticObjectId, products: ProductsServiceDependency):
    return products.delete_one(id)
