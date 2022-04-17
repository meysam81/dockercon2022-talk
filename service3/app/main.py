import os
from importlib import import_module

from app.settings import config
from fastapi import APIRouter, FastAPI

app = FastAPI()

router = APIRouter()


APIS = [
    "items",
]


@router.get("/")
async def index():
    return {
        "message": "Hello World",
        "hostname": os.uname().nodename,
        "app_prefix": config.APP_PREFIX,
    }


for api in APIS:
    import_name = f"app.api.{api}"
    router.include_router(import_module(import_name).router)

app.include_router(router, prefix=config.APP_PREFIX)

if config.DEBUG:
    from collections import defaultdict as dd
    from pprint import pprint

    routes = dd(set)
    for r in app.routes:
        routes[r.path].update(r.methods)

    pprint(dict(routes))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=config.DEBUG, port=config.PORT)
