from typing import Optional

from pydantic import BaseSettings as _PydanticSettings

TEN_MINUTES = 600


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

    SVC_CRUD_URL: str
    VERIFY_SVC_CRUD_SSL: bool = True

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str]

    CACHE_INVALIDATION_TTL: int = TEN_MINUTES


config = Settings()
