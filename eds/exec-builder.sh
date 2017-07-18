#!/usr/bin/env bash

. ./util/shell-utils.sh

case $1 in
backend|be)
    name="backend"
    setup_file="setup-gevent-all.py"
    binary_prefix="openmtc-all"
    ;;
gateway|gw)
    name="gateway"
    setup_file="setup-gevent-all.py"
    binary_prefix="openmtc-all"
    ;;
help)
    usage
    exit 0
    ;;
*) # other images will be detected by scanning setup files
    name="$1"
    setup_file="setup-${name}.py"
    binary_prefix="openmtc-${name}"
    ;;
esac

separator_line () {
counter=${1-80}
printf '%'${counter}'s\n' | tr ' ' '#'
}

base_path=$(dirname $(get_realpath "${0}"))
docker_dist="${base_path}/dist/docker"

setup_file="${base_path}/${setup_file}"

################################################################################
# set target file
get_target_from_setup_file ()
{
# Each setup file is assumed to hold ".py" suffix, this gets
# removed here
local file_name=$(basename ${setup_file})
local module_name=${file_name%.py}

cd ${base_path}
python - << END_OF_PYTHON
from importlib import import_module
setup = import_module('${module_name}', '${module_name}')
print("%s-%s" % (setup.SETUP_NAME, setup.SETUP_VERSION))
END_OF_PYTHON
}

# construct target file
target_file="$(get_target_from_setup_file).docker.tar.gz"
target_file="${base_path}/dist/${target_file}"

################################################################################
# build binary_package
separator_line
printf "### Creating binary archive...\n"
printf "### Running \"python %s bdist\" now..." ${setup_file}
log_file="/tmp/$(basename ${setup_file})_error.log"

# clean up before
rm -f ${target_file}
rm -rf ${base_path}/build/*

# build
cd ${base_path}
python ${setup_file} bdist --plat-name docker >/dev/null 2>${log_file}

# clean up after
rm -rf ${base_path}/build/*

# check success
if [ -e ${target_file} ]; then
    printf "done\n"
else
    printf "error\n\n"
    cat ${log_file}
    exit 1
fi

rm ${log_file}

################################################################################
# clean binary_package
binary_archive="${base_path}/dist/${binary_prefix}.docker.tar.gz"
printf "### Stripping .py files..."
cp ${target_file} ${binary_archive}
gzip -d ${binary_archive}
tar --wildcards --delete -f ${binary_archive%".gz"} "*.py"
gzip ${binary_archive%".gz"}
printf "done\n"
rm ${target_file}
printf "### Created binary archive at %s.\n" ${binary_archive}
