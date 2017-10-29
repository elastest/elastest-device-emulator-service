#!/bin/bash

echo "Starting up using docker-compose"

#docker network create elastest_elastest
docker-compose --project-name eds up -d  --force-recreate
