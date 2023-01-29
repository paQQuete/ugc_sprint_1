from fastapi import APIRouter, Depends

from models.model import ViewProduce
from services.getset_kafka import KafkaService, get_kafka_service


router = APIRouter()


@router.post('/set', response_model=ViewProduce)
async def set_view(view: ViewProduce, view_service: KafkaService = Depends(get_kafka_service)):
    await view_service.set(
        topic=view.topic,
        key=str(view.value.user_id).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return ViewProduce(topic=view.topic, value=view.value)
