from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    password: str
    created_at: datetime


users_db = [
    User(id=1, email="user1@example.com", password="password1", created_at=datetime.now()),
    User(id=2, email="user2@example.com", password="password2", created_at=datetime.now())
]


# response model for POST /users
class UserCreate(BaseModel):
    email: str
    password: str


# response model for GET /users and GET /users/{user_id}
class UserRead(BaseModel):
    id: int
    email: str
    created_at: datetime


# service
class UserService:
    def __init__(self):
        self._db = users_db

    def get_users(self) -> list[User]:
        return self._db

    def create_user(self, email: str, password: str) -> User:
        user = User(id=len(self._db) + 1, email=email, password=password, created_at=datetime.now())
        self._db.append(user)
        return user
    
    def get_user(self, user_id: int) -> User | None:
        for user in self._db:
            if user.id == user_id:
                return user
        return None

    def update_user_password(self, user_id: int, password: str) -> User | None:
        user = self.get_user(user_id)
        if not user:
            return None
        user.password = password
        return user

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user(user_id)
        if not user:
            return False
        self._db.remove(user)
        return True

# util function for external usage (export for dependency injection)
def get_user_service() -> UserService:
    return UserService()