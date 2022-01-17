#!/bin/bash

# Check if rabbit is up and running before starting the service.


until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo ${RABBIT_HOST}
    echo ${RABBIT_PORT}
    echo "$(date) - waiting for rabbitmq..."
    sleep 1
done


until nc -z -v -w30 ${MYSQL_HOST} ${MYSQL_PORT}
do
      echo ${MYSQL_HOST}
    echo ${MYSQL_PORT}
  echo "Waiting for database connection..."
  # wait for 5 seconds before check again
  sleep 1
done

# Run Migrations

alembic upgrade head




# Run Service

nameko run --config config.yml category
