#!/usr/bin/env python
import os
from importlib import import_module

from app.dependencies.caching.redis_cache import RedisCache
from app.settings import config
from fastapi import APIRouter, FastAPI

app = FastAPI()

router = APIRouter()

APIS = {
    "svc_crud": "/svc-crud-items",
}


@router.get("/")
async def index():
    return {
        "message": "Hello World",
        "hostname": os.uname().nodename,
        "app_prefix": config.APP_PREFIX,
    }


for api, prefix in APIS.items():
    import_name = f"app.api.{api}"
    router.include_router(import_module(import_name).router, prefix=prefix)

app.include_router(router, prefix=config.APP_PREFIX)
app.state.cache = RedisCache()  # NOTE: dependency injection

if config.DEBUG:
    from collections import defaultdict as dd
    from pprint import pprint

    routes = dd(set)
    for r in app.routes:
        routes[r.path].update(r.methods)

    pprint(dict(routes))


if __name__ == "__main__":
    import uvicorn

    if config.DEBUG:
        from pprint import pprint

        pprint({r.path: r.methods for r in app.routes})

    uvicorn.run("main:app", host="0.0.0.0", reload=config.DEBUG, port=config.PORT)
