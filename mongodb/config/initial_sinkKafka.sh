#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d @sink-properties.json http://localhost:8083/connectors | jq