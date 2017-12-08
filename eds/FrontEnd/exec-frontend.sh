#!/bin/sh
sh openmtc-gevent/run_gscl &
until $(curl --output /dev/null --silent --head --fail http://localhost:8000/onem2m); do
  printf '.'
  sleep 5
done
sh frontend
