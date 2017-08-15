#!/usr/bin/env bash
cd ZigBeeIPE

. common/prep_env.sh
cd ../

PYTHONPATH=${PYTHONPATH}:$(readlink -f ../../openmtc-app/src)

echo PYTHONPATH: ${PYTHONPATH}

export PYTHONPATH
