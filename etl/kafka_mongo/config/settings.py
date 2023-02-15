import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    KAFKA_HOST: str = os.getenv('KAFKA_HOST')
    KAFKA_PORT: str = os.getenv('KAFKA_PORT')
    KAFKA = f'{KAFKA_HOST}:{KAFKA_PORT}'

    MONGO_HOST: str = os.getenv('MONGO_HOST')
    MONGO_PORT: int = int(os.getenv('MONGO_PORT'))
