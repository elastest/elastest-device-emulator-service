#!/bin/sh

openmtc_path=/usr/local/src/openmtc
# create the EDS Orchestrator app
./create-app-structure -d -a eds_orch EDSOrch
# copy the relevant files to the application
cp /tmp/EDSOrch/__init__.py ${openmtc_path}/apps/EDSOrch/src/eds_orch/
cp /tmp/EDSOrch/eds_orch.py ${openmtc_path}/apps/EDSOrch/src/eds_orch/

# create Temperature Sensor app
./create-app-structure -d TemperatureSensor
cp /tmp/TemperatureSensor/__init__.py ${openmtc_path}/apps/TemperatureSensor/src/temperaturesensor/
cp /tmp/TemperatureSensor/temperature_sensor.py ${openmtc_path}/apps/TemperatureSensor/src/temperaturesensor/


# create Simple Actuator app
./create-app-structure -d SimpleActuator
cp /tmp/SimpleActuator/__init__.py ${openmtc_path}/apps/SimpleActuator/src/simpleactuator/
cp /tmp/SimpleActuator/simple_actuator.py ${openmtc_path}/apps/SimpleActuator/src/simpleactuator/


sh /usr/local/src/openmtc/openmtc-gevent/run-gateway &

sleep 1

until $(curl --output /dev/null --silent --fail http://localhost:8000/onem2m); do
	printf '.'
	sleep 1
done

sh ${openmtc_path}/apps/eds_orch
