#!/usr/bin/env bash

. ../common/prep_env.sh

PYTHONPATH=${PYTHONPATH}:$(readlink -f openmtc-app/src)

echo PYTHONPATH: ${PYTHONPATH}

export PYTHONPATH
