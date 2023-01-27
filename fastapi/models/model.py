import uuid
from uuid import UUID

import orjson
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class BaseOrjsonModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class BaseTimestampModel(BaseOrjsonModel):
    created_at: int
    updated_at: int


class BaseLikesModel(BaseTimestampModel):
    rating: int
    user_id: int


class ViewValue(BaseOrjsonModel):
    movie_timestamp: int
    event_timestamp: int
    movie_id: UUID
    user_id: str


class ViewProduce(BaseOrjsonModel):
    topic: str
    value: ViewValue


class MovieLikesValue(BaseLikesModel):
    movie_uuid: uuid.UUID


class MovieLikesProduce(BaseOrjsonModel):
    topic: str
    value: MovieLikesValue


class ReviewLikesValue(BaseLikesModel):
    review_uuid: uuid.UUID


class ReviewLikesProduce(BaseOrjsonModel):
    topic: str
    value: ReviewLikesValue


class ReviewValue(BaseTimestampModel):
    user_id: int
    movie_uuid: uuid.UUID
    title: str
    text: str


class ReviewProduce(BaseOrjsonModel):
    topic: str
    value: ReviewValue


class BookmarksValue(BaseTimestampModel):
    user_id: int
    movie_uuid: uuid.UUID


class BookmarksProduce(BaseOrjsonModel):
    topic: str
    value: BookmarksValue