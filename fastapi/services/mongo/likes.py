import uuid
from http import HTTPStatus
from typing import Optional, List

from fastapi import HTTPException

from core.config import Settings
from db.mongo import Mongo
from models.model import ReviewLikesValue, MovieLikesValue

mongo = Mongo()

settings = Settings()


async def get_movie_likes_list(
        user_id: int,
        limit: int = settings.DEFAULT_LIMIT,
        offset: int = settings.DEFAULT_OFFSET,
) -> List[MovieLikesValue]:
    """Получить список лайков фильмов пользователя"""
    data = await mongo.find(
        settings.COL_MOVIE_LIKES, {"user_id": user_id}, limit=limit, offset=offset
    )
    return [MovieLikesValue(**item) async for item in data]


async def get_reviews_likes_list(
        user_id: int,
        limit: int = settings.DEFAULT_LIMIT,
        offset: int = settings.DEFAULT_OFFSET,
) -> List[ReviewLikesValue]:
    """Получить список лайков рецензий пользователя"""
    data = await mongo.find(
        settings.COL_REVIEW_LIKES, {"user_id": user_id}, limit=limit, offset=offset
    )
    return [ReviewLikesValue(**item) async for item in data]


async def get_movie_like(user_id: int, film_id: uuid.UUID) -> Optional[MovieLikesValue]:
    """Получить один лайк"""
    data = await mongo.find_one(
        settings.COL_MOVIE_LIKES, {"user_id": user_id, "movie_uuid": film_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return MovieLikesValue(**data)


async def get_review_like(user_id: int, review_id: uuid.UUID) -> Optional[ReviewLikesValue]:
    """Получить один лайк"""
    data = await mongo.find_one(
        settings.COL_REVIEW_LIKES, {"user_id": user_id, "review_uuid": review_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return ReviewLikesValue(**data)


async def remove_movie_like(user_id: int, film_id: uuid.UUID) -> None:
    """Удалить лайк"""
    data = await mongo.find_one(
        settings.COL_MOVIE_LIKES, {"user_id": user_id, "movie_uuid": film_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    await mongo.delete(
        settings.COL_MOVIE_LIKES, {"user_id": user_id, "movie_uuid": film_id}
    )


async def remove_review_like(user_id: int, review_id: uuid.UUID) -> None:
    """Удалить лайк"""
    data = await mongo.find_one(
        settings.COL_REVIEW_LIKES, {"user_id": user_id, "review_uuid": review_id}
    )
    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    await mongo.delete(
        settings.COL_REVIEW_LIKES, {"user_id": user_id, "movie_uuid": review_id}
    )
