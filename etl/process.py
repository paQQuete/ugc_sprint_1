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
    CREATE TABLE IF NOT EXISTS default.views_queue
(
  id     Int64,
  key            String,
  value          String
)
ENGINE=Kafka('broker:29092', 'views', 'views_group1', 'JSONEachRow')
settings kafka_thread_per_consumer = 0, kafka_num_consumers = 1;
""")

client.execute(f"""
    CREATE TABLE default.views
(
  id     Int64,
  key            String,
  value          String
)
Engine=ReplacingMergeTree()
ORDER BY (id, key, value)
PARTITION BY (key);
""")

client.execute("""
CREATE MATERIALIZED VIEW default.views_consumer
TO default.views
AS SELECT *
FROM default.views_queue;
""")
