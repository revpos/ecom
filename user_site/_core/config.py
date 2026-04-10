from dotenv import load_dotenv
from typing import Final
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    APP_NAME: Final[str] = "rev-store"
    DEBUG: Final[bool] = False
    DB_USER: Final[str] = ""
    DB_PASSWORD: Final[str] = ""
    DB_NAME: Final[str] = "rstest.db"

    @property
    def DB_URL(self):
        return f"sqlite:///./{self.DB_NAME}"


settings = Config()