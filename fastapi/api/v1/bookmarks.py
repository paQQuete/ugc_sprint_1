import uuid
from typing import List

from fastapi import APIRouter, Depends

from models.model import BookmarksProduce, BookmarksValue
from services.set_kafka import KafkaService, get_kafka_service
from services.mongo import bookmarks


router = APIRouter()


@router.post('/', response_model=BookmarksProduce)
async def set_bookmark(view: BookmarksProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.movie_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return BookmarksProduce(topic=view.topic, value=view.value)


@router.get('/{user_id}', response_model=List[BookmarksValue])
async def get_bookmarks_list(user_id: int):
    return await bookmarks.get_bookmarks_list(user_id=user_id)


@router.get('/{user_id}/{film_id}', response_model=BookmarksValue)
async def get_bookmark(user_id: int, film_id: uuid.UUID):
    return await bookmarks.get_bookmark(user_id=user_id, film_id=film_id)


@router.delete('/{user_id}/{film_id}', status_code=200)
async def remove_bookmark(user_id: int, film_id: uuid.UUID):
    return await bookmarks.remove_bookmark(user_id=user_id, film_id=film_id)
