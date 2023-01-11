import datetime
from typing import Union, List, Optional

import orjson
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class ViewProduce(BaseModel):
    topic: str
    key: str
    value: str
    timestamp: Union[datetime.datetime, None] = None

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class ViewConsume(BaseModel):
    class Message:
        topic: str
        key: str
        value: str
        offset: int
        timestamp: int
        timestamp_type: int

    topic: str
    offset: Union[int, None] = None
    group_id: str
    batchsize: Union[int, None] = None
    messages: Optional[List['Message']] = None

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class RequestConsume(BaseModel):
    topic: str
    offset: Union[int, None] = None
    group_id: str
    batchsize: Union[int, None] = None

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
