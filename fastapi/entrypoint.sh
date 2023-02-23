#!/bin/bash

cd /opt/fastapi/src

while ! nc -zv $KAFKABROKER_HOST $KAFKABROKER_PORT; do
      sleep 0.1
      echo "sleep, waiting Kafka Broker is up"
done
echo "Kafka Broker host is up, wanna sleep more"
sleep 120
echo "Ready to go"

gunicorn main:app --workers 6 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
