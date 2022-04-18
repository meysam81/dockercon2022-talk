from datetime import timedelta

import aioredis
from app.settings import config

from .base import BaseCache


class RedisCache(BaseCache):
    def __init__(
        self, host: str = None, port: int = None, db: int = None, password: str = None
    ):
        self.redis = aioredis.from_url(
            self.get_connection_url(
                host=host or config.REDIS_HOST,
                port=port or config.REDIS_PORT,
                db=db or config.REDIS_DB,
                password=password or config.REDIS_PASSWORD,
            )
        )

    @staticmethod
    def get_connection_url(host, port, db=0, password=None):
        if password:
            return f"redis://:{password}@{host}:{port}/{db}"
        return f"redis://{host}:{port}/{db}"

    async def get(self, key: str) -> str:
        return await self.redis.get(key)

    async def set(self, key: str, value: bytes, expiry: int) -> bool:
        return await self.redis.set(key, value, ex=timedelta(seconds=expiry))
