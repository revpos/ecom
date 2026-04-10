from fastapi import Depends

from user_site.application import UserService

from ..infrastructure.db import get_db_session
from ..infrastructure.repo_adapters import SQLAlchemyUserRepository


# UserService(session=get_user_repo())
def get_user_repo(session = Depends(get_db_session)):
    return SQLAlchemyUserRepository(session)


# APIRouter(service=get_user_servive()) 
def get_user_service(repo = Depends(get_user_repo)):
    return UserService(repo)