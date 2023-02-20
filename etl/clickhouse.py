import os
import random
from pathlib import Path

from clickhouse_driver import Client
from dotenv import load_dotenv


load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = Client(host=os.getenv('CLICKHOUSE_HOST'))
kafka_broker = f"{os.getenv('KAFKABROKER_HOST')}:{os.getenv('KAFKABROKER_PORT')}"

client.execute(f"""
    CREATE TABLE IF NOT EXISTS default.views_queue ON CLUSTER company_cluster
(
  user_id           String,
  movie_id          UUID,
  movie_timestamp timestamp,
  event_timestamp timestamp
)
ENGINE=Kafka('{kafka_broker}', 'views', 'views_group{random.randint(1,256)}', 'JSONEachRow')
settings kafka_thread_per_consumer = 0, kafka_num_consumers = 1;
""")

client.execute("""
CREATE MATERIALIZED VIEW default.views_consumer ON CLUSTER company_cluster
TO default.views
AS SELECT *
FROM default.views_queue;
""")

client.execute("""
    CREATE TABLE default.views ON CLUSTER company_cluster
(
  user_id           String,
  movie_id          UUID,
  movie_timestamp timestamp,
  event_timestamp timestamp
)
Engine=ReplacingMergeTree()
ORDER BY (user_id)
PARTITION BY (movie_id);
""")

