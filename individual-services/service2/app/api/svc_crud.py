from app.controllers.svc_crud import SVCCrudController
from fastapi import APIRouter, Request, Response

router = APIRouter()


@router.get("/")
async def fetch_item_from_crud_service(item_id: int, request: Request):
    json, status = await SVCCrudController(
        request.app.state.cache
    ).get_item_from_svc_crud(item_id)
    if json:
        return json
    return Response(content=json, status_code=status)
