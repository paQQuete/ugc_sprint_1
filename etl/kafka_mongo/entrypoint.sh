#!/bin/bash

export $(cat .env.cloud | xargs)

echo "Waiting for Kafka broker..."
    while ! nc -z "$KAFKA_HOST" "$KAFKA_PORT"; do
      sleep 0.5
    done
    echo "Kafka Broker started"

echo "Waiting for MongoDB..."
    while ! nc -z "$MONGO_HOST" "$MONGO_PORT"; do
      sleep 0.5
    done
    echo "MongoDB started"

#sleep 60

# shellcheck disable=SC2164
declare -a curdir=$(pwd)
declare -a conf_gen=$(pwd)

curdir+="/main.py"
conf_gen+="/utils/conf_gen.py"

python3 $conf_gen

cd ./utils/conf/topics
declare -a topicsl
for FILE in *; do
  topicsl+=("$FILE")
done

for TOPIC in "${topicsl[@]}"; do
   cd ../../..
   echo $TOPIC
   python3 $curdir -t $TOPIC &
done

while true
do
  sleep 60
done
