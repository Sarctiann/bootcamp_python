from fastapi import APIRouter
from pydantic_mongo import PydanticObjectId

from ..models import BaseUser, CreationUser, UpdationUser
from ..services import UsersServiceDependency, AuthServiceDependency
from ..__common_deps import QueryParamsDependency

users_router = APIRouter(prefix="/Users", tags=["Users"])


@users_router.post("/")
def create_user(
    user: CreationUser, users: UsersServiceDependency, auth: AuthServiceDependency
):
    hash_password = auth.get_password_hash(user.password)
    inserted_id = users.create_one(user, hash_password)
    return {"result message": f"User created with id: {inserted_id}"}


@users_router.get("/")
def get_all_users(users: UsersServiceDependency, params: QueryParamsDependency):
    return users.get_all(params)


@users_router.get("/{id}")
def get_one_user(id: PydanticObjectId, users: UsersServiceDependency):
    return users.get_one(id=id)


@users_router.put("/{id}")
def update_user(
    id: PydanticObjectId, user: UpdationUser, users: UsersServiceDependency
):
    return users.update_one(id=id, user=user)


@users_router.delete("/{id}")
def delete_user(id: PydanticObjectId, users: UsersServiceDependency):
    return users.delete_one(id=id)
