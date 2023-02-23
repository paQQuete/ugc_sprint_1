from typing import Optional
from aiokafka import AIOKafkaProducer


producer: Optional[AIOKafkaProducer] = None


def get_producer() -> AIOKafkaProducer:
    return producer
