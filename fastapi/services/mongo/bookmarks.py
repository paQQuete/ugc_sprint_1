import uuid
from http import HTTPStatus
from typing import Optional, List

from fastapi import HTTPException

from core.config import Settings
from db.mongo import Mongo
from models.model import BookmarksValue


mongo = Mongo()

settings = Settings()


async def get_bookmarks_list(
        user_id: int,
        limit: int = settings.DEFAULT_LIMIT,
        offset: int = settings.DEFAULT_OFFSET,
) -> List[BookmarksValue]:
    """Получить список закладок"""
    data = await mongo.find(
        settings.COL_BOOKMARKS, {"user_id": user_id}, limit=limit, offset=offset
    )
    return [BookmarksValue(**item) async for item in data]


async def get_bookmark(user_id: int, film_id: uuid.UUID) -> Optional[BookmarksValue]:
    """Получить одну закладку"""
    data = await mongo.find_one(
        settings.COL_BOOKMARKS, {"user_id": user_id, "movie_uuid": film_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return BookmarksValue(**data)


async def remove_bookmark(user_id: int, film_id: uuid.UUID) -> None:
    """Удалить закладку"""
    data = await mongo.find_one(
        settings.COL_BOOKMARKS, {"user_id": user_id, "movie_uuid": film_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    await mongo.delete(
        settings.COL_BOOKMARKS, {"user_id": user_id, "movie_uuid": film_id}
    )
