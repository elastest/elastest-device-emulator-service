function initDashboard(socket, configuredSensorList) {
    var config = getConfigFromList(configuredSensorList);

    var initialSensors = true;
    var initialActuators = true;

    function handleNewSensor(sensor) {
        if (_.has(config, sensor.ID)) {
            var confSensor = config[sensor.ID];
            if (!confSensor.created) {
                confSensor.dev = sensor['dev_name'];
                confSensor.sensor = sensor.n;
                confSensor.unit = sensor.u;
                confSensor.data = _.map(sensor.data, function (val) {
                    return {
                        x: new Date(parseFloat(val.t) * 1000),
                        y: val.v
                    }
                });
                confSensor.maxLen = sensor['max_data'];
                initSensorTile(confSensor);
                createChart(confSensor);
                confSensor.created = true;
            } else { // handle reconnected sensors
                confSensor.data.concat(_.map(sensor.data, function (val) {
                    return {
                        x: new Date(parseFloat(val.t) * 1000),
                        y: val.v
                    }
                }));
                while (confSensor.maxLen < confSensor.data.length) {
                    confSensor.data.shift();
                }
                updateChart(confSensor)
            }
        }
    }

    function handleSensorData(sensorData) {
        if (_.has(config, sensorData.ID)) {
            var confSensor = config[sensorData.ID];
            if (confSensor.created) {
                confSensor.data.push({
                    x: new Date(parseFloat(sensorData.data.t) * 1000),
                    y: sensorData.data.v
                });
                if (confSensor.maxLen < confSensor.data.length) {
                    confSensor.data.shift();
                }
                updateChart(confSensor);
            } // todo(rst): check if else createChart is necessary
        }
    }

    function actuate(tile, command) {
        socket.emit('pushContent', configuredSensorList[tile], command);
    }

    // quick hack for having it usable in the helper file
    window.actuate = actuate;

    function handleNewActuator(actuator) {
        if (_.has(config, actuator.ID)) {
            var confActuator = config[actuator.ID];
            if (!confActuator.created) {
                confActuator.dev = actuator['dev_name'];
                confActuator.actuator = actuator.n;
                initActuatorTile(confActuator);
                confActuator.created = true;
            }
        }
    }

    socket.on('connect', function () {
        console.log('Socket - Connected.');
        console.log('SessionId:', socket.id);

        socket.on('sensorList', function (sensorList) {
            _.each(sensorList, handleNewSensor);

            if (initialSensors) {
                initialSensors = false;
                socket.on('sensorData', handleSensorData);
                socket.on('newSensor', handleNewSensor)
            }
        });

        socket.emit('getSensorList');

        socket.on('actuatorList', function (actuatorList) {
            _.each(actuatorList, handleNewActuator);

            if (initialActuators) {
                initialActuators = false;
                socket.on('newActuator', handleNewActuator)
            }
        });

        socket.emit('getActuatorList');
    });

    $("#btnAdd1").on('click',function() {
        console.log("Motor Started");
        socket.emit("motor_start")


    });
    $("#btnAdd2").on('click',function() {
        console.log("Motor Stopped");
        socket.emit("motor_stop")
    });

}
