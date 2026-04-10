from dataclasses import dataclass, field
from datetime import datetime
from typing import Annotated

from .value_objects import Email, Password
from ..utils.helpers import validate_pw_len

@dataclass(slots=True)
class UserProfile:
    first_name: str | None = None
    last_name: str | None = None
    bio: str | None = None

# Password is a string with length between 8 and 16


@dataclass(slots=True)
class User:
    user_id: int
    email: Email
    password: Password
    is_active: bool = True
    profile: UserProfile | None = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None

    # def __post_init__(self):
    #     if self.user_id <= 0:
    #         raise ValueError("user_id must be positive")
        # if not 6 <= len(self.email.value) <= 255:
        #     raise ValueError("invalid email format, length not in range(6, 256)")
        # if not 8 <= len(self.password.hashed) <= 255:
        #     raise ValueError("Invalid Password, length not in range(8, 256)")

    @property
    def full_name(self) -> str | None:
        if not self.profile:
            return 
        if not self.profile.first_name and not self.profile.last_name:
            return
    
        return f"{self.profile.first_name} {self.profile.last_name}"

        
    
    