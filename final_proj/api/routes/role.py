from fastapi import APIRouter

# from pydantic_mongo import PydanticObjectId

from ..models import Role
from ..database import db


__all__ = ["roles_router"]

roles_router = APIRouter()


@roles_router.get("/")
def get_roles():
    roles = [Role.model_validate(r) for r in db.roles.find()]
    return {"roles": roles}


@roles_router.get("/{role_id}")
def get_role(role_id: int):
    role = Role.model_validate(db.roles.find_one({"role_id": role_id}))
    return {"role": role}


@roles_router.post("/")
def create_role(role: Role):
    result = db.roles.insert_one(role.model_dump(exclude={"id"}))
    return {"result": str(result.inserted_id)}
