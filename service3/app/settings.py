from pydantic import BaseSettings as _PydanticSettings


class BaseSettings(_PydanticSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True
        strict_env = True
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    DEBUG: bool = False
    PORT: int = 8000
    APP_PREFIX: str = ""
    DB_CONNECTION_STRING: str = "sqlite:///./sqlite3.db"
    DB_PAGINATE: int = 10


config = Settings()
