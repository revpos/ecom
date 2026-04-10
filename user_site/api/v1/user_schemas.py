from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from ...utils.helpers import get_datetime_utc


# Base model for user data (shared attributes)
class UserBase(BaseModel):
    user_id: int = Field(..., gt=0)
    email: EmailStr = Field(..., min_length=4, max_length=255)
    password: str = Field(..., min_length=8, max_length=16)
    created_at: datetime


# POST /users/ endpoint (req, res) schemas (exclude created_at since it's auto-generated)
class UserCreateRequest(UserBase):
    full_name: str | None = Field(default=None, max_length=100)


class UserCreateResponse(BaseModel):
    email: EmailStr = Field(..., min_length=4, max_length=255)
    full_name: str | None = Field(default=None, max_length=100)
    created_at: datetime = Field(default_factory=get_datetime_utc)


# GET /users/ and GET /users/{user_id} response schema (exclude password)
class UserPublicResponse(BaseModel):
    user_id: int
    email: EmailStr = Field(..., min_length=4, max_length=255)
    full_name: str | None = Field(default=None, max_length=100)
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None


# PUT /users/{user_id} request and response schemas
class UserUpdateRequest(BaseModel):
    full_name: str | None = Field(..., max_length=100)


class UserUpdateResponse(BaseModel):
    email: EmailStr = Field(..., min_length=4, max_length=255)
    full_name: str | None = Field(default=None, max_length=100)
    is_active: bool
    updated_at: datetime = Field(default_factory=get_datetime_utc)


class UserPasswordUpdateRequest(BaseModel):
    email: EmailStr = Field(..., min_length=4, max_length=255)
    old_password: str = Field(..., min_length=8, max_length=16)
    new_password: str = Field(..., min_length=8, max_length=16)


class UserPasswordUpdateResponse(BaseModel):
    message: str = "Password updated successfully"
    email: EmailStr = Field(..., min_length=4, max_length=255)
    updated_at: datetime = Field(default_factory=get_datetime_utc)


class UserDeleteRequest(BaseModel):
    user_id: int = Field(..., gt=0)
    email: EmailStr | None = Field(..., min_length=4, max_length=255)


class UserDeleteResponse(BaseModel):
    message: str = "User deleted successfully"
    email: EmailStr = Field(..., min_length=4, max_length=255)
    deleted_at: datetime = Field(default_factory=get_datetime_utc)
