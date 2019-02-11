# Working procedure
Install OpenMTC, follow the documentation given in [Installation of OpenMTC
SDK](https://fiware-openmtc.readthedocs.io/en/latest/install-sdk/index.html).

Copy all the contents in this folder to the **apps** directory of OpenMTC
repository.

Assuming you are already in the OpenMTC repository do the following:
## Start the gateway
execute in a separate terminal:  
```./openmtc-gevent/run-gateway -v```

## Start the sensor
execute in a separate terminal:  
```./apps/sensor-example -v```

## Start the actuator
execute in a separate terminal:  
```./apps/actuator-example -v```  


## Start the logic
execute in a separate terminal:  
```./apps/logic-example -v```

## The complete system is setup
For more information you can look into the source code. For sensor example you
can look into the path:  
```apps/SensorExample/src/sensorexample/sensor_example.py```
