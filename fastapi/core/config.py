import os
from logging import config as logging_config

from dotenv import load_dotenv
from pydantic import BaseSettings, AnyUrl
from core.logger import LOGGING


DEBUG = True
if DEBUG:
    load_dotenv()

logging_config.dictConfig(LOGGING)


class KafkaDSN(BaseSettings):
    KAFKA_HOST: str
    KAFKA_PORT: int

    class Config:
        env_file = '.env'


class Settings(BaseSettings):
    PROJECT_NAME: str
    KAFKA: KafkaDSN = KafkaDSN()
    KAFKA_SERVER: str = f'{KAFKA.KAFKA_HOST}:{KAFKA.KAFKA_PORT}'
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_DB: str
    DEFAULT_LIMIT: int = 10
    DEFAULT_OFFSET: int = 0

    COL_VIEWS: str
    COL_MOVIE_LIKES: str
    COL_REVIEW_LIKES: str
    COL_REVIEWS: str
    COL_BOOKMARKS: str
    COL_GENRE_LIKES: str

    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        env_file = '.env'
