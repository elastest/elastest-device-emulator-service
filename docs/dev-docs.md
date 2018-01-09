Architecture: Architecture of the component specifying the relation with other ElasTest components
Prepare development environment: How to prepare the development environment to develop this TSS. For example, what tools are required, in which version, etc.
Development procedure: All information useful to develop the component. For example, how to execute the component in the IDE, how to compile it, etc.
Docker images: Description of the docker images used for the component. If the components can be developed outside ElasTest and needs some docker containers to simulate the other ElasTest components, should be described here.
Continuous Integration: The description of the jobs used in ElasTest CI. What are used for, when are executed, etc. 

###Architecture:
 ![EDS screenshot examaple](image/eds_arch.jpg)

The entire application EDS consists of many services such as- zigbeeipe, memsipe, rest_app, and frontend. We devide the architecture as follows:
 - sensor/actuator based services/application which uses m2m communication protocol.
 - Application to visualize all the data and metices coming from the sesor/actuator based services/application, which uses m2m communication protocol.
 - Simple restfull communication based service or application
 
###Prepare development environment:
 First make sure that EDS can work with ESM  and EMP.
 Install the following development tools:
 - [PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=linux)
 - [Python 2.7 and 3+](http://docs.python-guide.org/en/latest/starting/install3/linux/)
 - [OpenMTC code]
 
 Last, clone the repositories in a local folder:

```
git clone https://github.com/elastest/elastest-device-emulator-service
git clone https://github.com/elastest/elastest-service-manager.git
git clone https://github.com/elastest/elastest-monitoring-platform.git
```
 
###Development procedure:

  * Using  *PyCharm IDE*:
    * Load/open the projects from IDE:
      * Import *EDS* project from local repository using File > Open --> select the project name elastest-device-emulator-service
      *
      
   * From *IDE and console*:
     * Run *prep-env.sh* from the console to install all openmtc dependencies and to create the environment for zigbeeipe,memsipe and frontend services.
     * Go to the rest_app directory and run foolowing:
      ```
      pip install -r requirements.txt
      
      ```
     This will install all the dependencies to run the service properly and even to integrate the service with other Elastest component such as EMP and ESM.
   
     
###Docker images:
The following docker images are currently used in order to make the EDS work successfully:
 - elastest/eds-frontend: a service used as a GUI or frontend inorder to show all the sensors data in a graph view 
 formate as well as has capability to actuate sesor and actuator. The image associated to this service is accessible [here](https://hub.docker.com/r/elastest/eds-frontend/)
 - elastest/eds-api: a service contain restfull api that communicate with the elastest component. This service is based on
 OpenAPI specification.The image associated to this service is accessible [here](https://hub.docker.com/r/elastest/eds-api/)
 - elastest/eds-memsipe: a service with uses accelometers data such as x,y and z axes. The image associated to this service is accessible [here](https://hub.docker.com/r/elastest/eds-zigbeeipe/)
 - elastest/eds-zigbeeipe: a service for zigbee sensor protocol data such as vibration, temperature, movement etc. The image associated to this service is accessible [here](https://hub.docker.com/r/elastest/eds-memsipe/)