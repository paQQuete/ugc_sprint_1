from typing import Union

import orjson
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class ViewProduce(BaseModel):
    topic: str
    value: str
    key: str
    timestamp: Union[str, None] = None

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


# class ClientGroupResponse(BaseModel):
#     group_ip: str
#
#     class Config:
#         json_loads = orjson.loads
#         json_dumps = orjson_dumps
#
#
# class ViewConsume(BaseModel):
#     group_ip: str
#
#     class Config:
#         json_loads = orjson.loads
#         json_dumps = orjson_dumps
