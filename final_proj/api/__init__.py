from fastapi import APIRouter
from .routes import roles_router

__all__ = ["api"]

api = APIRouter(prefix="/api")
api.include_router(roles_router, prefix="/roles", tags=["Roles"])
