import uuid
from typing import Union

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
    movie_id: uuid.UUID
    user_id: int
    genre_uuid: uuid.UUID


class ViewProduce(BaseOrjsonModel):
    topic: str = 'ugcViews'
    value: ViewValue


class MovieLikesValue(BaseLikesModel):
    movie_uuid: uuid.UUID
    genre_uuid: uuid.UUID


class MovieLikesProduce(BaseOrjsonModel):
    topic: str = 'ugcMovie_likes'
    value: MovieLikesValue


class ReviewLikesValue(BaseLikesModel):
    review_uuid: uuid.UUID


class ReviewLikesProduce(BaseOrjsonModel):
    topic: str = 'ugcReview_likes'
    value: ReviewLikesValue


class GenreLikesValue(BaseOrjsonModel):
    genre_uuid: uuid.UUID


class GenreLikesProduce(BaseOrjsonModel):
    topic: str = 'ugcGenre_likes'
    value: GenreLikesValue


class ReviewValue(BaseTimestampModel):
    review_uuid: uuid.UUID
    user_id: int
    movie_uuid: uuid.UUID
    title: str
    text: str


class ReviewProduce(BaseOrjsonModel):
    topic: str = 'ugcReviews'
    value: ReviewValue


class BookmarksValue(BaseTimestampModel):
    user_id: int
    movie_uuid: uuid.UUID


class BookmarksProduce(BaseOrjsonModel):
    topic: str = 'ugcBookmarks'
    value: BookmarksValue