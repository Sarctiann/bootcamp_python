from fastapi import APIRouter, Response

from ..models import CreationUser, LoginUser
from ..services import AuthServiceDependency, SecurityDependency, UsersServiceDependency

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/register")
def register(
    user: CreationUser, users: UsersServiceDependency, auth: AuthServiceDependency
):
    hash_password = auth.get_password_hash(user.password)
    inserted_id = users.create_one(user, hash_password)
    return {"result message": f"User created with id: {inserted_id}"}


@auth_router.post("/login")
def login_with_cookie(
    user: LoginUser,
    response: Response,
    users: UsersServiceDependency,
    auth: AuthServiceDependency,
):
    db_user = users.get_one(username=user.username, with_password=True)
    return auth.login_and_set_access_token(
        user=user, db_user=db_user, response=response
    )


@auth_router.get("/authenticated_user")
def read_current_user(security: SecurityDependency):
    return dict(
        id=security.auth_user_id,
        name=security.auth_user_name,
        email=security.auth_user_email,
        role=security.auth_user_role,
    )
