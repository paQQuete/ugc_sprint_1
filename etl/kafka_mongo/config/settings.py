import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

DEBUG=False
if DEBUG:
    env_path = Path('.') / '.env.local'
    load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    KAFKA_HOST: str = os.getenv('KAFKA_HOST')
    KAFKA_PORT: str = os.getenv('KAFKA_PORT')
    KAFKA = f'{KAFKA_HOST}:{KAFKA_PORT}'

    MONGO_HOST: str = os.getenv('MONGO_HOST')
    MONGO_PORT: int = int(os.getenv('MONGO_PORT'))

    topics: list = os.getenv('TOPICS')