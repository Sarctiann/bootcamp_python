from fastapi import APIRouter
from .products import products_router

__all__ = ["api_router"]

api_router = APIRouter(prefix="/api")
api_router.include_router(products_router)
