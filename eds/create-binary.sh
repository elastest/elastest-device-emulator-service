#!/usr/bin/env bash

. ./util/shell-utils.sh

# base_path=$(dirname $(readlink -f "${0}"))
base_path=$(dirname $(get_realpath "${0}"))

binary_archive_suffix="_binary_$(date +%Y-%m-%d).tar.gz"

################################################################################
# set setup_file
declare -a setup_array

setup_array=($(find ${base_path} -name "setup-*.py"))
array_length=${#setup_array[@]}

# print possibilities
for i in $(seq 1 ${array_length}); do
    echo [${i}] $(basename ${setup_array[$[${i}-1]]})
done

# read choice
while true; do
    read -n 1 -p "Choose the setup script: " choice

    [[ ${choice} =~ ^[0-9]+$ ]] && \
        [ ${choice} -gt 0 -a ${choice} -le ${array_length} ] && \
        echo && break

    echo " Wrong choice. Do it again."
done

setup_file=${setup_array[$[${choice}-1]]}

################################################################################
# set target_file
# get target name from setup call
target_name=$(grep -m 1 -E "name=" ${setup_file} | \
    tr -d " ,'\"" | awk -F "=" '{print $2;}')

# fix if name was set by variable
if [ "x${target_name}" == "xSETUP_NAME" ]; then
    target_name=$(grep -m 1 -E "^\s*SETUP_NAME\s*=\s*" ${setup_file} | \
        tr -d " ,'\"" | awk -F "=" '{print $2;}')
fi

# fix if constructed variable
if [[ "${target_name}" == *"+NAME" ]]; then
    target_name_prefix=$(grep -m 1 -E "^\s*NAME\s*=\s*" ${setup_file} | \
        tr -d " ,'\"" | awk -F "=" '{print $2;}')
    target_name=${target_name%"+NAME"}${target_name_prefix}
fi

# get target version from setup call
target_version=$(grep -m 1 -E "version=" ${setup_file} | \
    tr -d " ,'\"" | awk -F "=" '{print $2;}')

# fix if version was set by variable
if [ "x${target_version}" == "xSETUP_VERSION" ]; then
    target_version=$(grep -m 1 -E "^SETUP_VERSION = " ${setup_file} | \
        tr -d " ,'\"" | awk -F "=" '{print $2;}')
fi

# construct target file
target_file="${target_name}-${target_version}.linux-$(uname -m).tar.gz"
target_file="${base_path}/dist/${target_file}"

################################################################################
# build binary_package
echo -n "Running \"python ${setup_file} bdist\" now..."
log_file="/tmp/$(basename ${setup_file})_error.log"

# clean up before
rm -f ${target_file}
rm -rf ${base_path}/build/*

# build
cd ${base_path}
python ${setup_file} bdist >/dev/null 2>${log_file}

# clean up after
rm -rf ${base_path}/build/*

# check success
if [ -e ${target_file} ]; then
    echo "done"
else
    echo "error"
    echo
    cat ${log_file}
    exit 1
fi

rm ${log_file}

################################################################################
# clean binary_package
binary_archive="${target_file%".tar.gz"}${binary_archive_suffix}"
echo -n "Stripping .py files..."
cp ${target_file} ${binary_archive}
gzip -d ${binary_archive}
tar --wildcards --delete -f ${binary_archive%".gz"} "*.py"
gzip ${binary_archive%".gz"}
echo "done"

echo "Created binary archive at ${binary_archive}"
