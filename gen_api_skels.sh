#!/usr/bin/env bash

# assumes installation of swagger code gen
SWAGGER_CODE_GEN="java -jar ../modules/swagger-codegen-cli/target/swagger-codegen-cli.jar"

# generate the skeletons for the server process
# mapping object to # is the only way to remove this generation AFAIK
# -DsupportPython2=true <- only if required, by default no.
 $SWAGGER_CODE_GEN generate -i  ./api.yaml -l python-flask -o ./eds/rest_app/ -DpackageName=eds_api -D supportPython2=true --import-mappings object=#

# generate gRPC stubs
# python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path=. ./backend_osba_adapter.proto
