import app.entities.items as entity
import app.models.items as model
from app.database.orm import connection
from app.settings import config
from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter

router = APIRouter()

router.include_router(
    CRUDRouter(
        schema=entity.Items,
        db_model=model.Items,
        create_schema=entity.CreateItem,
        update_schema=entity.UpdateItem,
        paginate=config.DB_PAGINATE,
        delete_all_route=False,
        db=lambda: connection(config.DB_CONNECTION_STRING),
    )
)
