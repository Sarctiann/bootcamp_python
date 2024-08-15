__all__ = ["api_router", "auth_router"]

from fastapi import APIRouter

from .auth import auth_router
from .products import products_router

api_router = APIRouter(prefix="/api")
api_router.include_router(products_router)
