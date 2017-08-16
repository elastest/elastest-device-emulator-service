#!/usr/bin/env bash
#cd ZigBeeIPE

. ZigBeeIPE/common/prep_env.sh


PYTHONPATH=${PYTHONPATH}:$(readlink -f ../../openmtc-app/src)

echo PYTHONPATH: ${PYTHONPATH}

export PYTHONPATH
