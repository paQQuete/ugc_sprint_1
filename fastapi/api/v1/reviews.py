from fastapi import APIRouter, Depends

from models.model import ReviewProduce
from services.getset_kafka import KafkaService, get_kafka_service


router = APIRouter()


@router.post('/set', response_model=ReviewProduce)
async def set_movie(view: ReviewProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.movie_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return ReviewProduce(topic=view.topic, value=view.value)
