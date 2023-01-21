from functools import lru_cache

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from fastapi import Depends

from core import config
from db.kafka import get_producer, get_consumer


class ViewService:
    def __init__(self, producer: AIOKafkaProducer, consumer: AIOKafkaConsumer):
        self.producer = producer
        self.consumer = consumer

    async def set(self, topic: str, value: bytes, key: bytes) -> None:
        await self.producer.send_and_wait(topic=topic, key=key, value=value)


@lru_cache()
def get_view_service(
        producer: AIOKafkaProducer = Depends(get_producer),
        consumer: AIOKafkaConsumer = Depends(get_consumer)
) -> ViewService:
    return ViewService(producer, consumer)
