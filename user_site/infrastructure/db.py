from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from user_site.core.config import settings
from infrastructure.models import Base

# Database configuration
sqlite_file_name = "ecom_users.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(settings.DB_URL, echo=True, future=True)
sessionmaker = Session(bind=engine, autocommit=False, autoflush=False,)

# Create the database tables inherited from Base(DeclarativeBase)
Base.metadata.create_all(engine)


# Util function to get a database session(export for dependency injection)
def get_db_session():
    with Session(engine) as session:
        yield session
