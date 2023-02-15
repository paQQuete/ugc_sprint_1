#!/bin/bash
fetchstatus() {
        HEAD http://localhost:8000 | grep '404\ Not Found' | wc -l
}
#export $(grep -v '^#' .env.local | xargs)

#up all services
docker compose -f docker-compose.full.yml up -d --build

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
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic ugcViews
sleep 1

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic ugcMovie_likes
sleep 1

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic ugcReview_likes
sleep 1

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic ugcReviews
sleep 1

docker exec zookeeper-kafka \
  kafka-topics --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --if-not-exists --topic ugcBookmarks
sleep 1

#initialized database tables and engines
python3 clickhouse/initial.py
python3 etl/clickhouse.py
