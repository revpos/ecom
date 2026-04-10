from dataclasses import dataclass
import re
from typing import Final

from user_site.utils.helpers import hash_password


EMAIL_MIN_LENGTH: Final[int] = 6
EMAIL_MAX_LENGTH: Final[int] = 255
PASSWORD_MIN_LENGTH: Final[int] = 8
PASSWORD_MAX_LENGTH: Final[int] = 255

EMAIL_REGEX: Final = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")


@dataclass(frozen=True, slots=True)
class Email:
    value: str

    def __post_init__(self):
        self._validate_format()
        self._validate_length()
        object.__setattr__(self, "value", self.value.lower().strip())

    def _validate_format(self):
        if not self.value or not EMAIL_REGEX.match(self.value):
            raise ValueError(f"Invalid email format: {self.value!r}")

    def _validate_length(self):
        if not EMAIL_MIN_LENGTH <= len(self.value) <= EMAIL_MAX_LENGTH:
            raise ValueError(
                f"Email must be between {EMAIL_MIN_LENGTH} "
                f"and {EMAIL_MAX_LENGTH} characters"
            )

    def __str__(self) -> str:
        return self.value


# def _validate_pw_len(password: str, min_length: int = 8, max_length: int = 16) -> bool:
#     return min_length <= len(password) <= max_length


@dataclass(frozen=True, slots=True)
class Password:
    hashed: str

    @classmethod
    def create(cls, raw: str) -> "Password":
        if not PASSWORD_MIN_LENGTH <= len(raw) <= PASSWORD_MAX_LENGTH:
            raise ValueError(
                f"Password must be between {PASSWORD_MIN_LENGTH} "
                f"and {PASSWORD_MAX_LENGTH} characters"
            )
        return cls(hashed=hash_password(raw))

    def __str__(self) -> str:
        return "*" * len(self.hashed)
    
# if __name__ == "__main__":
#     email = Email(value="f@b.c")
#     pwd = Password.create(raw="pas123")

#     print(email)
#     print(pwd)