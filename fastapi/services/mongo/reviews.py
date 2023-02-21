import uuid
from http import HTTPStatus
from typing import Optional, List

from fastapi import HTTPException

from core.config import Settings
from db.mongo import Mongo
from models.model import ReviewValue


mongo = Mongo()

settings = Settings()


async def get_review_list(
    user_id: int,
    limit: int = settings.DEFAULT_LIMIT,
    offset: int = settings.DEFAULT_OFFSET,
) -> List[ReviewValue]:
    """Получить список рецензий"""
    data = await mongo.find(
        settings.COL_REVIEWS, {"user_id": user_id}, limit=limit, offset=offset
    )
    return [ReviewValue(**item) async for item in data]


async def get_review(user_id: int, review_id: uuid.UUID) -> Optional[ReviewValue]:
    """Получить одну рецензию"""
    data = await mongo.find_one(
        settings.COL_REVIEWS, {"user_id": user_id, "review_uuid": review_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return ReviewValue(**data)


async def remove_review(user_id: int, review_id: uuid.UUID) -> None:
    """Удалить рецензию"""
    data = await mongo.find_one(
        settings.COL_REVIEWS, {"user_id": user_id, "review_uuid": review_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    await mongo.delete(
        settings.COL_REVIEWS, {"user_id": user_id, "review_uuid": review_id}
    )
