from config.settings import Settings
from extract import KafkaConsume
from load import MongoLoad
from utils import sysargs_parser

SETTINGS = Settings()


def task(topic: str, offset_group: str = 'etl'):
    consumer = KafkaConsume(topic=topic, kafka_server=SETTINGS.KAFKA, offset_group=offset_group)
    try:
        for msg in consumer.consumer:
            loader = MongoLoad(topic=msg.topic, data=msg.value, mongo_host=SETTINGS.MONGO_HOST,
                               mongo_port=SETTINGS.MONGO_PORT)
            consumer.commit()
    except BaseException:
        loader.close()
        consumer.close()
    finally:
        loader.close()
        consumer.close()


if __name__ == '__main__':
    args = sysargs_parser.args_parser().parse_args()
    task(topic=args.topic, offset_group=args.offset_group)
