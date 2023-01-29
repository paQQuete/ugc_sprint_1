from fastapi import APIRouter, Depends

from models.model import BookmarksProduce
from services.getset_kafka import KafkaService, get_kafka_service


router = APIRouter()


@router.post('/set', response_model=BookmarksProduce)
async def set_movie(view: BookmarksProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.movie_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return BookmarksProduce(topic=view.topic, value=view.value)
