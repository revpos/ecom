from typing import Annotated

from fastapi import APIRouter, Depends

from user_site.api.v1.user_schemas import UserCreateRequest

from user_site._core.deps import get_user_service

user_router = APIRouter(tags=["users"])


@user_router.get("/demo")
def get_users():
    return {"user1": "alice", "user2": "bob"}



@user_router.post("/users/")
def create_user(
    payload: UserCreateRequest, 
    service = Depends(get_user_service)
):
    """Create a new user. Returns the created UserCreateResponse."""
    new_user = service.register_user(
        email=user.email,
        password=user.password,
        full_name=user.full_name,  # full_name is optional and not provided in the request
    )

    return UserCreateResponse(
        email=new_user.email,
        full_name=new_user.full_name,
        created_at=new_user.created_at,
    )