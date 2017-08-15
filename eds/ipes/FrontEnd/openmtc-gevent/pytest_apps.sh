#!/bin/sh

cd $(dirname ${0})

. ./prep-env.sh

exec py.test ../apps -v
