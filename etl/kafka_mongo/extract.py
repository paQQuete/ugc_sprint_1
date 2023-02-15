
class KafkaExtract:
    def __init__(self, kafka_server: str, offset_group: str = 'etl-kafka-mongo'):
        self.kafka_server = kafka_server
        self.offset_group = offset_group
