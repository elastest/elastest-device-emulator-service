#!/bin/sh
sh openmtc-gevent/run_gscl &
until $(curl --output /dev/null --silent --head --fail http://localhost:6065/onem2m); do
  printf '.'
  sleep 1
done
sh frontend
