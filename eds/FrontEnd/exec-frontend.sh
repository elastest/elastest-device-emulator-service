#!/bin/sh
sh openmtc-gevent/run_gscl &
sleep 1
until $(curl --output /dev/null --silent --fail http://localhost:8000/); do
  printf '.'
  sleep 1
done
sh frontend
