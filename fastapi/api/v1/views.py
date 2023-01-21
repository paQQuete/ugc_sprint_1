from fastapi import APIRouter, Depends

from models.model import ViewProduce, ViewConsume, RequestConsume
from services.getset_kafka import ViewService, get_view_service


router = APIRouter()


@router.post('/set', response_model=ViewProduce)
async def set_view(view: ViewProduce, view_service: ViewService = Depends(get_view_service)):
    await view_service.set(
        topic=view.topic,
        key=str(view.value.user_id).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return ViewProduce(topic=view.topic, value=view.value)
