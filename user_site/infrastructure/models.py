from datetime import datetime
# import uuid

from sqlalchemy import Boolean, DateTime, String, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy.dialects.postgresql import UUID

class Base(DeclarativeBase):
    pass

# User table schema
class UserSQL(Base):
    __tablename__ = "users"

    # user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email_address: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True, default=None
    )
    secure_password: Mapped[str] = mapped_column(String(63), nullable=False, default=None)
    full_name: Mapped[str | None] = mapped_column(String(63), nullable=True, default=None)
    bio: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True, default=None, onupdate=func.now())

