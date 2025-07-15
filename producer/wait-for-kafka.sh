#!/bin/bash

host="kafka"
port="9092"

echo "Waiting for Kafka at $host:$port..."

while ! nc -z $host $port; do
  echo "Kafka is unavailable - sleeping"
  sleep 2
done

echo "Kafka is up - executing producer"
python producer.py
