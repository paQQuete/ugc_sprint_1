#!/bin/bash

cd /opt/fastapi/src

while ! nc -zv $KAFKABROKER_HOST $KAFKABROKER_PORT; do
      sleep 0.1
      echo "sleep, waiting Kafka Broker is up"
done
echo "Kafka Broker host is up, wanna sleep more"
sleep 120
echo "Ready to go"

uvicorn main:app --host 0.0.0.0 --port 8000