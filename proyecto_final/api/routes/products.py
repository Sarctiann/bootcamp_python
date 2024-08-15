__all__ = ["products_router"]

from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from pydantic_mongo import PydanticObjectId

from ..models import Product
from ..services import ProductsServiceDependency

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get("/")
async def list_products(products: ProductsServiceDependency):
    return products.get_all()


@products_router.get("/{id}")
async def get_product(id: PydanticObjectId, products: ProductsServiceDependency):
    return products.get_one(id) or JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": f"Product with id: {id}, was not found."},
    )


@products_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product, products: ProductsServiceDependency):
    inserted_id = products.create_one(product)
    return {"result message": f"Product created with id: {inserted_id}"}
