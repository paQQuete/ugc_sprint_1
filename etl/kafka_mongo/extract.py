import json

from kafka import KafkaConsumer


class KafkaConsume:
    def __init__(self, topic: str, kafka_server: str, offset_group: str = 'etl-kafka-mongo'):
        self.consumer = KafkaConsumer(
            topic,
            group_id=offset_group,
            bootstrap_servers=kafka_server,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            key_deserializer=lambda k: k.decode('utf-8'),
            enable_auto_commit=False,
            auto_offset_reset='earliest'
        )

    def commit(self):
        self.consumer.commit()

