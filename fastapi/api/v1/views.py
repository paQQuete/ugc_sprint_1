import uuid

from fastapi import APIRouter, Depends

from models.model import ViewProduce, ViewValue
from services.set_kafka import KafkaService, get_kafka_service
from services.mongo import views

router = APIRouter()


@router.post('/', response_model=ViewProduce)
async def set_view(view: ViewProduce, view_service: KafkaService = Depends(get_kafka_service)):
    await view_service.set(
        topic=view.topic,
        key=str(view.value.user_id).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return ViewProduce(topic=view.topic, value=view.value)


@router.get('/{user_id}/{film_id}', response_model=ViewValue)
async def get_view(user_id: int, film_id: uuid.UUID):
    return await views.get_view(user_id=user_id, film_id=film_id)


@router.delete('/{user_id}/{film_id}', status_code=200)
async def delete_view(user_id: int, film_id: uuid.UUID):
    return await views.remove_review(user_id=user_id, film_id=film_id)
