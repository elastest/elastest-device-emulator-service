### Description:
Elastest Device Emulator Service (EDS), the main goal of this service is to emulate behaviors of sensors, actuators and 
smart devices  which is suitable for ElasTest platform. This service shall enable the creation of device models suitable
for exposing the appropriate interfaces and behavior. It is a test support service for ElasTest platform which provides 
additional functionality for testing used by the testers.
 
### Features:
* Simualted behaviors of the sensors, actuators and smartdevices.  
* Getting all the incoming data from the emulated devices to a GUI as well as actuate and monitor then from the 
GUI.
* More features will be added and updated here soon.


### How to use from GUI:
Right now user can see only the simulated behaviors of the emulated sensors in a graphical form. Later they will have 
monitoring capabilites as well.
#### How to run:
* Run EDS using docker-compose: This method allows docker to setup containers
and connect them in a custom network named **elastest_elastest**. All the IPEs register after 10 seconds with 
FrontEnd.

Start EDS using:  
```shell
chmod +x script/*
./script/startup-linux.sh
```
To stop EDS:
```shell
./script/teardown-linux.sh 
```

* Run EDS on local machine : This is explained in the development documenation, as
it requires changing the default network configuration.

The EDS FrontEnd UI can be accessed from port 6065, FrontEnd gateway from port
8000 and rest_app on port 8080. 

It is important for MemsIPE to have "/dev/i2c-1" device node available on the 
host machine. Please make sure to stop and remove the stale containers. If running using
docker compose, it is advisable to remove docker bridge with name "build_eds_netowrk" 
before running startup-linux.sh script.

