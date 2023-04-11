import uuid
from typing import List

from fastapi import APIRouter, Depends

from models.model import MovieLikesProduce, ReviewLikesProduce, MovieLikesValue, ReviewLikesValue, GenreLikesProduce, \
    GenreLikesValue
from services.set_kafka import KafkaService, get_kafka_service
from services.mongo import likes

router = APIRouter()


@router.post('/movie', response_model=MovieLikesProduce)
async def set_movie_like(view: MovieLikesProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.movie_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return MovieLikesProduce(topic=view.topic, value=view.value)


@router.post('/review', response_model=ReviewLikesProduce)
async def set_review_like(view: ReviewLikesProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.review_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return ReviewLikesProduce(topic=view.topic, value=view.value)


@router.post('/genre', response_model=GenreLikesProduce)
async def set_genre_like(view: GenreLikesProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.review_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return GenreLikesProduce(topic=view.topic, value=view.value)


@router.get('/movie/{user_id}', response_model=List[MovieLikesValue])
async def get_movie_likes_list(user_id: int):
    return await likes.get_movie_likes_list(user_id=user_id)


@router.get('/review/{user_id}', response_model=List[ReviewLikesValue])
async def get_review_likes_list(user_id: int):
    return await likes.get_reviews_likes_list(user_id=user_id)


@router.get('/genre/{user_id}', response_model=List[GenreLikesValue])
async def get_genre_likes_list(user_id: int):
    return await likes.get_genre_likes_list(user_id=user_id)


@router.get('/movie/{user_id}/{film_id}', response_model=MovieLikesValue)
async def get_movie_like(user_id: int, film_id: uuid.UUID):
    return await likes.get_movie_like(user_id=user_id, film_id=film_id)


@router.get('/review/{user_id}/{review_id}', response_model=ReviewLikesValue)
async def get_review_like(user_id: int, review_id: uuid.UUID):
    return await likes.get_review_like(user_id=user_id, review_id=review_id)


@router.get('/genre/{user_id}/{genre_id}', response_model=GenreLikesValue)
async def get_genre_like(user_id: int, genre_id: uuid.UUID):
    return await likes.get_genre_like(user_id=user_id, genre_id=genre_id)


@router.delete('/movie/{user_id}/{film_id}', status_code=200)
async def remove_movie_like(user_id: int, film_id: uuid.UUID):
    return await likes.remove_movie_like(user_id=user_id, film_id=film_id)


@router.delete('/review/{user_id}/{review_id}', status_code=200)
async def remove_review_like(user_id: int, review_id: uuid.UUID):
    return await likes.remove_review_like(user_id=user_id, review_id=review_id)


@router.delete('/genre/{user_id}/{genre_id}', status_code=200)
async def remove_genre_like(user_id: int, genre_id: uuid.UUID):
    return await likes.remove_genre_like(user_id=user_id, genre_id=genre_id)
