import uuid
from typing import Any, List

from fastapi import APIRouter, Depends

from services.set_kafka import KafkaService, get_kafka_service
from models.model import ReviewProduce, ReviewValue
from services.mongo import reviews


router = APIRouter()


@router.post('/', response_model=ReviewProduce)
async def set_review(view: ReviewProduce, kafka_service: KafkaService = Depends(get_kafka_service)):
    await kafka_service.set(
        topic=view.topic,
        key=str(view.value.movie_uuid).encode('UTF-8'),
        value=view.value.json().encode('UTF-8')
    )
    return ReviewProduce(topic=view.topic, value=view.value)


@router.get("/{user_id}", response_model=List[ReviewValue], description="Список рецензий")
async def get_review_list(
    user_id: int,
    limit: int = 10,
    offset: int = 0,
) -> Any:
    """
    Список рецензий
    """
    return await reviews.get_review_list(user_id=user_id, limit=limit, offset=offset)



@router.get("/{user_id}/{review_uuid}", response_model=ReviewValue, description="Получить рецензию")
async def get_review(
    user_id: int,
    review_uuid: uuid.UUID
) -> Any:
    """
    Получить рецензию
    """
    return await reviews.get_review(user_id=user_id, review_id=review_uuid)


@router.delete("/{user_id}/{review_uuid}", status_code=200, description="Удалить рецензию")
async def delete_review(
    user_id: int,
    review_uuid: uuid.UUID,
) -> Any:
    """
    Удалить рецензию
    """
    return await reviews.remove_review(user_id=user_id, review_id=review_uuid)
