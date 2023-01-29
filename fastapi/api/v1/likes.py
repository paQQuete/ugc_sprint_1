from fastapi import APIRouter, Depends

from models.model import MovieLikesProduce, ReviewLikesProduce
from services.getset_kafka import KafkaService, get_kafka_service


router = APIRouter()


@router.post('/movie/set', response_model=MovieLikesProduce)
async def set_movie(view: MovieLikesProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.movie_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return MovieLikesProduce(topic=view.topic, value=view.value)


@router.post('/review/set', response_model=ReviewLikesProduce)
async def set_movie(view: ReviewLikesProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.review_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return ReviewLikesProduce(topic=view.topic, value=view.value)
