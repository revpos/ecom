import logging

# from user_site._core.logging import logging
from user_site.infrastructure.models import UserSQL
from user_site.api.v1.user_schemas import UserCreateResponse
from user_site.api.v1.user_schemas import (
    UserPublicResponse as UserPublic
)

from user_site.domain import User, UserRepositoryPort, Email, Password 

logger = logging.getLogger(__name__)


def _to_public(user: User) -> UserPublic:
    full_name = user.full_name

    return UserPublic(
        user_id=user.user_id,
        email=user.email.value,
        full_name=full_name,
        is_active=user.is_active,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )

class UserService:
    # __slots__ = ["_repo", "logger",]

    def __init__(self, repo: UserRepositoryPort, ):
        self._repo = repo

    def _get_by_id(self, user_id: int) -> User | None:
        return self._repo.get_by_id(user_id)

    def _get_by_email(self, email: str) -> User | None:
        return self._repo.get_by_email(email)

    def list_users(self) -> list[UserPublic]:
        users = self._repo.get_users()
        if not users:
            return []
        
        return [_to_public(u) for u in users]

    def get_user(
        self, user_id: int | None = None, email: str | None = None
    ) -> UserPublic | None:
        user = (
            self._get_by_id(user_id)
            if user_id is not None
            else self._get_by_email(email)
            if email is not None
            else None
        )
        return _to_public(user) if user else None

    def create_user(
        self, email: str, password: str, full_name: str | None = None
    ) -> UserCreateResponse:
        if self._get_by_email(email):
            raise ValueError(f"Email already registered: {email}")

        n = len(self.list_users())
        
        user = User(
            user_id=n+1,
            email=Email(value=email),
            password=Password.create(raw=password),
            is_active=True,
        )
        self._repo.save_to_db(user)

        return UserCreateResponse(
            email=user.email.value,
            full_name=user.full_name,
            created_at=user.created_at,
        )
