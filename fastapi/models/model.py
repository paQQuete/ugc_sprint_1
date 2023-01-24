from uuid import UUID

import orjson
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class BaseOrjsonModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class ViewValue(BaseOrjsonModel):
    movie_timestamp: int
    event_timestamp: int
    movie_id: UUID
    user_id: str


class ViewProduce(BaseOrjsonModel):
    topic: str
    value: ViewValue
