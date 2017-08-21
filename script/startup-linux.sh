#!/bin/bash

echo "Starting up using docker-compose"

docker-compose --project-name eds up -d  --force-recreate
