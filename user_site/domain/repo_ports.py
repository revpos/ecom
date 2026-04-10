# from abc import ABC, abstractmethod
from typing import Protocol

from sqlalchemy.orm import Session

from user_site.domain import User


class UserRepositoryPort(Protocol):
    _session: Session

    def get_users(self) -> list[User]:
        """Get a users collection as a list"""
        ...

    def get_by_email(self, email: str) -> User | None:
        """Fetch a user by email."""
        ...

    def get_by_id(self, user_id: int) -> User | None:
        """Fetch a user by user_id."""
        ...

    def save_to_db(self, user: User) -> bool:
        """Persist a user to storage."""
        ...