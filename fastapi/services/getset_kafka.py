from functools import lru_cache
from typing import Union, List

import aiokafka
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from fastapi import Depends

from core import config
from db.kafka import get_producer, get_consumer
from models import serializers



class ViewService:
    def __init__(self, producer: AIOKafkaProducer, consumer: AIOKafkaConsumer):
        self.producer = producer
        self.consumer = consumer

    async def set(self, topic: str, value: bytes, key: bytes) -> None:
        await self.producer.send_and_wait(topic=topic, key=key, value=value)

    async def get(self, topic: str, offset: int, group_id: str, batchsize: Union[int, None]) -> List[dict]:
        self.consumer = aiokafka.AIOKafkaConsumer(
            topic,
            bootstrap_servers=config.KAFKA_SERVER,
            group_id=group_id,
            key_deserializer=serializers.deserialize,
            value_deserializer=serializers.deserialize,
            max_poll_records=batchsize,
            retry_backoff_ms=1000,
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            isolation_level='read_committed',
        )
        await self.consumer.start()
        output_data = list()
        async for msg in self.consumer:
            output_data.append({
                'topic': msg.topic,
                'key': msg.key,
                'value': msg.value,
                'offset': msg.offset,
                'timestamp': msg.timestamp,
                'timestamp_type': msg.timestamp_type

            })
        await self.consumer.commit()
        await self.consumer.stop()


        # data = await self.consumer.getmany()
        # output_data = list()
        # for tp, messages in data.items():
        #     topic = tp.topic
        #     partition = tp.partition
        #     for message in messages:
        #         output_data.append({
        #             'topic': message.topic,
        #             'key': message.key,
        #             'value': message.value,
        #             'offset': message.offset,
        #             'timestamp': message.timestamp,
        #             'timestamp_type': message.timestamp_type
        #
        #         })
        # await self.consumer.commit()
        return output_data


@lru_cache()
def get_view_service(
        producer: AIOKafkaProducer = Depends(get_producer),
        consumer: AIOKafkaConsumer = Depends(get_consumer)
) -> ViewService:
    return ViewService(producer, consumer)
