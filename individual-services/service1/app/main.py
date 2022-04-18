#!/usr/bin/env python
import os

from app.settings import Settings
from fastapi import APIRouter, FastAPI

app = FastAPI()
config = Settings()

router = APIRouter()


@router.get("/")
async def index():
    return {
        "message": "Hello World",
        "hostname": os.uname().nodename,
        "app_prefix": config.APP_PREFIX,
    }


app.include_router(router, prefix=config.APP_PREFIX)

if __name__ == "__main__":
    import uvicorn

    if config.DEBUG:
        from pprint import pprint

        pprint({r.path: r.methods for r in app.routes})

    uvicorn.run("main:app", host="0.0.0.0", reload=config.DEBUG, port=config.PORT)
