import os
from pathlib import Path

from clickhouse_driver import Client
from dotenv import load_dotenv

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = Client(host=os.getenv('CLICKHOUSE_HOST'))
# kafka = f"{os.getenv('KAFKA_HOST')}:{os.getenv('KAFKA_PORT')}"

client.execute(f"""
    CREATE TABLE IF NOT EXISTS default.views_queue ON CLUSTER company_cluster
(
  id     Int64,
  key            Int64,
  movie_id          UUID,
  movie_timestamp timestamp,
  event_timestamp timestamp
)
ENGINE=Kafka('broker:29092', 'views', 'views_group2', 'JSONEachRow')
settings kafka_thread_per_consumer = 0, kafka_num_consumers = 1;
""")

client.execute(f"""
    CREATE TABLE default.views ON CLUSTER company_cluster
(
  id     Int64,
  key            Int64,
  movie_id          UUID,
  movie_timestamp timestamp,
  event_timestamp timestamp
)
Engine=ReplacingMergeTree()
ORDER BY (id, key, movie_id)
PARTITION BY (movie_id);
""")

client.execute("""
CREATE MATERIALIZED VIEW default.views_consumer ON CLUSTER company_cluster
TO default.views
AS SELECT *
FROM default.views_queue;
""")
