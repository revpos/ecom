import hashlib
from datetime import datetime, timezone


def get_datetime_utc() -> datetime:
    """Get the current datetime in UTC."""
    return datetime.now(timezone.utc)


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def validate_pw_len(password: str, min_length: int = 8, max_length: int = 16) -> bool:
    return min_length <= len(password) <= max_length


# if __name__ == "__main__":
#     from typing import Annotated
#     word = 12345667
#     anno_word = str(Annotated[word, validate_pw_len(str(word))])
#     print(anno_word)