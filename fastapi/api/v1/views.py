import string
import random

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


@router.get('/get', response_model=ViewConsume)
async def set_view(view: RequestConsume, view_service: ViewService = Depends(get_view_service)):
    return await view_service.get(topic=view.topic, offset=view.offset, group_id=view.group_id, batchsize=view.batchsize)
