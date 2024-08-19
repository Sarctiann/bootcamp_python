__all__ = ["api_router", "auth_router"]

from fastapi import APIRouter

from .auth import auth_router
from .orders import orders_router
from .products import products_router
from .users import users_router

api_router = APIRouter(prefix="/api")
api_router.include_router(orders_router)
api_router.include_router(products_router)
api_router.include_router(users_router)
