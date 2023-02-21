import json
import os
from logging import config as logging_config
from dotenv import load_dotenv
from pydantic import BaseSettings

from core.logger import LOGGING


load_dotenv()
logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    PROJECT_NAME = os.getenv('PROJECT_NAME')
    KAFKA_HOST = os.getenv('KAFKABROKER_HOST')
    KAFKA_PORT = int(os.getenv('KAFKABROKER_PORT'))
    KAFKA_SERVER = f'{KAFKA_HOST}:{KAFKA_PORT}'
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_PORT = int(os.getenv('MONGO_PORT'))
    MONGO_DB = os.getenv('MONGO_DB')
    DEFAULT_LIMIT = 10
    DEFAULT_OFFSET = 0

    TOPICS = json.loads(os.getenv('TOPICS'))
    COL_VIEWS = [x for x in TOPICS if 'Views' in x][0]
    COL_MOVIE_LIKES = [x for x in TOPICS if 'Movie_likes' in x][0]
    COL_REVIEW_LIKES = [x for x in TOPICS if 'Review_likes' in x][0]
    COL_REVIEWS = [x for x in TOPICS if 'Reviews' in x][0]
    COL_BOOKMARKS = [x for x in TOPICS if 'Bookmarks' in x][0]

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


