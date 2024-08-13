from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from pydantic_mongo import PydanticObjectId

from ..database.products import product_collection
from ..models import Product


__all__ = ["products_router"]


products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get("/")
async def list_products(products: product_collection):
    return [Product.model_validate(product) for product in products.find()]


@products_router.get("/{id}")
async def get_product(id: PydanticObjectId, products: product_collection):
    if db_product := products.find_one({"_id": id}):
        return Product.model_validate(db_product)
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": f"Product with id: {id}, was not found."},
        )


@products_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product, products: product_collection):
    result = products.insert_one(product.model_dump(exclude={"id"}))
    return {"result message": f"Product created with id: {result.inserted_id}"}
