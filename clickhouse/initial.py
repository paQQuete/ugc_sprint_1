import os
from pathlib import Path

from clickhouse_driver import Client
from dotenv import load_dotenv


load_dotenv()
env_path = Path('.') / '.env.local'
load_dotenv(dotenv_path=env_path)

client = Client(host=os.getenv('CLICKHOUSE_HOST'))

client.execute('CREATE DATABASE IF NOT EXISTS example ON CLUSTER company_cluster')
client.execute(
    'CREATE TABLE example.regular_table ON CLUSTER company_cluster (id Int64, x Int32) Engine=MergeTree() ORDER BY id')

os.system(r"docker exec clickhouse-node1 bash -c 'clickhouse-client --queries-file /etc/clickhouse-server/node1.sql'")
os.system(r"docker exec clickhouse-node3 bash -c 'clickhouse-client --queries-file /etc/clickhouse-server/node3.sql'")
