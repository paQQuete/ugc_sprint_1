from typing import Optional
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer


producer: Optional[AIOKafkaProducer] = None
consumer: Optional[AIOKafkaConsumer] = None


async def get_producer() -> AIOKafkaProducer:
    return producer


async def get_consumer() -> AIOKafkaConsumer:
    return consumer
