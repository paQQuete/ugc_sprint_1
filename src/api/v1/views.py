import string
import random

from fastapi import APIRouter, Depends

from models.model import ViewProduce, ClientGroupResponse
from services.view import ViewService, get_view_service


router = APIRouter()


@router.post('/set', response_model=ViewProduce)
async def set_view(view: ViewProduce, view_service: ViewService = Depends(get_view_service)):
    await view_service.set(topic=view.topic, value=view.value.encode('UTF-8'), key=view.key.encode('UTF-8'))
    return ViewProduce(topic=view.topic, value=view.value, key=view.key)


# @router.get('/get', response_model=ViewProduce)
# async def get_view(view: ViewProduce, view_service: ViewService = Depends(get_view_service)):
#     await view_service.get()
#
#
# @router.get('/utils/get_group_id', response_model=ClientGroupResponse)
# async def get_id():
#     return ClientGroupResponse(group_id=f"""group-{''.join((random.choice(string.ascii_letters) for i in range(20)))}""")
