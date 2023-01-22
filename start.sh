#!/bin/bash
fetchstatus() {
        HEAD http://localhost:8000 | grep '404\ Not Found' | wc -l
}
export $(grep -v '^#' .env | xargs)

docker compose up -d

status=$(fetchstatus)
until [ $status = "1" ]; do
  echo "waiting for fastapi service, sleep for 5 seconds"
  sleep 5
  status=$(fetchstatus)
done
echo "fastapi service is working, continue"

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic views

python3 clickhouse/initial.py
python3 etl/process.py
