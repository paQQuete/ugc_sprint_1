from abc import ABC, abstractmethod


class AsyncKafkaProducer(ABC):
    @abstractmethod
    async def set(self, topic: str, value: bytes, key: bytes, **kwargs):
        pass


class AsyncKafkaConsumer(ABC):
    @abstractmethod
    async def get(self, topic: str, **kwargs):
        pass
