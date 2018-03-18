#!/bin/sh

# create the EDS Orchestrator app
./create-app-structure -d -a eds_orch EDSOrch
# copy the relevant files to the application

# create Temperature Sensor app
./create-app-structure -d TemperatureSensor

# create Simple Actuator app
./create-app-structure -d SimpleActuator

sh /usr/local/bin/configure-and-start &

sleep 1

until $(curl --output /dev/null --silent --fail http://localhost:8000/onem2m); do
	printf '.'
	sleep 1
done

sh
