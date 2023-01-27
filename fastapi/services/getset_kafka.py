from functools import lru_cache

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from fastapi import Depends

from db.kafka import get_producer


class KafkaService:
    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def set(self, topic: str, value: bytes, key: bytes) -> None:
        await self.producer.send_and_wait(topic=topic, key=key, value=value)


@lru_cache()
def get_view_service(
        producer: AIOKafkaProducer = Depends(get_producer)
) -> KafkaService:
    return KafkaService(producer)
