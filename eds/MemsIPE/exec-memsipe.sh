#!/bin/sh

apt-get install -y python-pip libev-dev python-dev gcc make automake
pip install -r openmtc-gevent/dependencies.txt
python setup-sdk.py install
sh openmtc-gevent/run_gscl &
sleep 1
sh mems-ipe
