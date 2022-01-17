#!/bin/bash

# Check if rabbit is up and running before starting the service.


until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo ${RABBIT_HOST}
    echo ${RABBIT_PORT}
    echo "$(date) - waiting for rabbitmq..."
    sleep 2
done
# Run Migrations


# Run Service

nameko run  --config config.yml gateway
