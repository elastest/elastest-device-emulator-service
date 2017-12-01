#! /bin/sh

set -e

cd `dirname "${0}"`

for f in ./xsd/*; do
  if test -d "${f}"; then
    n="binding_"`basename "${f}" | cut -f1 -d'-' | sed -e "s/\\./_/g"`
    echo $n
    pyxbgen -m $n --binding-root=src/openmtc_onem2m/serializer/impl/xml/ "${f}"/*.xsd
  fi
done

