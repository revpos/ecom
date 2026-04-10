from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from user_site.domain import UserRepositoryPort
from user_site._core.deps import get_db_session
from user_site.infrastructure.models import UserSQL

from user_site.domain.entities import User, UserProfile
from user_site.domain.value_objects import Email, Password


class SQLAlchemyUserRepository:
    def __init__(self, session: Session = next(get_db_session())):
        self.session = session

    def get_users(self) -> list[User]:

        results = self.session.query(UserSQL).all()
        if not results:
            return []
        
        return [
            User(
                user_id=dbu.user_id,
                email=Email(value=dbu.email_address),
                password=Password(hashed=dbu.secure_password),
                created_at=dbu.created_at,
                updated_at=dbu.updated_at,
            ) for dbu in results
        ]

    def get_by_email(self, email: str):
        row = self.session.query(UserSQL).filter(UserSQL.email_address == email).first()
        if not row:
            return None
        
        return User(
            user_id=row.user_id,
            email=Email(value=row.email_address),
            password=Password(hashed=row.secure_password),
            created_at=row.created_at,
            updated_at=row.updated_at,
            )
    

    def get_by_id(self, user_id: int) -> User | None:
        row = self.session.query(UserSQL).filter(UserSQL.user_id == user_id).first()
        if not row:
            return None

        name_parts = (row.full_name or "").strip().split()

        first_name, last_name = "", ""

        if len(name_parts) == 1:
            first_name = name_parts[0]
        elif len(name_parts) >= 2:
            first_name = name_parts[0]
            last_name = " ".join(name_parts[1:])

        profile = UserProfile(
            first_name=first_name, 
            last_name=last_name, 
            bio=row.bio
        )

        return User(
            user_id=row.user_id,
            email=Email(value=row.email_address),
            password=Password(hashed=row.secure_password),
            profile=profile,
            created_at=row.created_at,
            updated_at=row.updated_at,
        )

    
    def save(self, user: User) -> bool:
        user_record = UserSQL(
            email_address=user.email.value,
            secure_password=user.password.hashed,
            full_name=user.full_name,
        )
        self.session.add(user_record)
        try:
            self.session.commit()
            self.session.refresh(user_record)
        except Exception:
            self.session.rollback()
            return False
        return True

