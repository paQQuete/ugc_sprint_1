#!/bin/bash
fetchstatus() {
        HEAD http://localhost:8000 | grep '404\ Not Found' | wc -l
}
#export $(grep -v '^#' .env | xargs)

#up all services
docker compose up -d --build

#wait for services alive
status=$(fetchstatus)
until [ $status = "1" ]; do
  echo "waiting for fastapi service, sleep for 5 seconds"
  sleep 5
  status=$(fetchstatus)
done
echo "fastapi service is working, continue"


#create Kafka topics
docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic views
sleep 1

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic movie_likes
sleep 1

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic review_likes
sleep 1

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic reviews
sleep 1

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic bookmarks
sleep 1

#initialized database tables and engines
python3 clickhouse/initial.py
python3 etl/process.py
