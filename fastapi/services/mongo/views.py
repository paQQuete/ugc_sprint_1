import uuid
from http import HTTPStatus
from typing import Optional, List

from fastapi import HTTPException

from core.config import Settings
from db.mongo import Mongo
from models.model import ViewValue


mongo = Mongo()

settings = Settings()


async def get_view_list(
    user_id: int,
    limit: int = settings.DEFAULT_LIMIT,
    offset: int = settings.DEFAULT_OFFSET,
) -> List[ViewValue]:
    """Получить список просмотров пользователя"""
    data = await mongo.find(
        settings.COL_VIEWS, {"user_id": user_id}, limit=limit, offset=offset
    )
    return [ViewValue(**item) async for item in data]


async def get_view(user_id: int, film_id: uuid.UUID) -> Optional[ViewValue]:
    """Получить прогресс просмотра одного фильма"""
    data = await mongo.find_one(
        settings.COL_VIEWS, {"user_id": user_id, "movie_id": film_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return ViewValue(**data)


async def remove_review(user_id: int, film_id: uuid.UUID) -> None:
    """Удалить прогресс просмотра одного фильма"""
    data = await mongo.find_one(
        settings.COL_VIEWS, {"user_id": user_id, "movie_id": film_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    await mongo.delete(
        settings.COL_VIEWS, {"user_id": user_id, "movie_id": film_id}
    )
