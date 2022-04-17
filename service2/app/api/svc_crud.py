from urllib.parse import urljoin

import aiohttp
from app.settings import config
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def fetch_item_from_crud_service(item_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            get_item_url(item_id), verify_ssl=config.VERIFY_SVC_CRUD_SSL
        ) as response:
            return await response.json()


def get_item_url(item_id: int):
    SVC_CRUD_URL = config.SVC_CRUD_URL
    return urljoin(SVC_CRUD_URL, f"/v1/items/{item_id}")
