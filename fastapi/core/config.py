import os
from logging import config as logging_config
from dotenv import load_dotenv
from pydantic import BaseSettings

from core.logger import LOGGING


load_dotenv()
logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    PROJECT_NAME = os.getenv('PROJECT_NAME')
    # KAFKA_HOST = os.getenv('KAFKABROKER_HOST')
    KAFKA_HOST = os.getenv('KAFKA_HOST')
    # KAFKA_PORT = int(os.getenv('KAFKABROKER_PORT'))
    KAFKA_PORT = int(os.getenv('KAFKA_PORT'))
    KAFKA_SERVER = f'{KAFKA_HOST}:{KAFKA_PORT}'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


