#!/bin/sh

python setup-sdk.py install
sh openmtc-gevent/run_gscl &
sleep 1
sh mems-ipe
