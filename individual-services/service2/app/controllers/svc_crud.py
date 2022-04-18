import pickle
from urllib.parse import urljoin

import aiohttp
from app.common.logger import get_logger
from app.dependencies.caching import BaseCache
from app.settings import config


class SVCCrudController:
    def __init__(self, cache: BaseCache, logger=None):
        self.cache = cache
        self.logger = logger or get_logger(__package__)

    async def get_item_from_svc_crud(self, item_id):
        if cached := await self.fetch_from_cache(item_id):
            return cached, 200

        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.get_item_url(item_id), verify_ssl=config.VERIFY_SVC_CRUD_SSL
            ) as response:
                try:
                    json = await response.json()
                    await self.set_to_cache(item_id, json)
                except Exception as exp:
                    json = None
                    self.logger.error(exp)

                return json, response.status

    @staticmethod
    def get_item_url(item_id: int):
        SVC_CRUD_URL = config.SVC_CRUD_URL
        return urljoin(SVC_CRUD_URL, f"/v1/items/{item_id}")

    async def fetch_from_cache(self, item_id):
        pickled = await self.cache.get(item_id)
        if pickled:
            return pickle.loads(pickled)

    async def set_to_cache(self, item_id, item):
        pickled = pickle.dumps(item)
        await self.cache.set(item_id, pickled, config.CACHE_INVALIDATION_TTL)
