### Architecture:
 ![EDS screenshot examaple](image/eds_arch.jpg)

The entire application EDS consists of many services such as- zigbeeipe, memsipe, rest_app, and frontend. We devide the architecture as follows:
 - sensor/actuator based services/application which uses m2m communication protocol.
 - Application to visualize all the data and metices coming from the sesor/actuator based services/application, which uses m2m communication protocol.
 - Simple restfull communication based service or application
 
### Prepare development environment:

First install the following development tools:
 - [PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=linux)
 - [Python 2.7 and 3+](http://docs.python-guide.org/en/latest/starting/install3/linux/)
 - Latest version of [Docker](https://docs.docker.com/engine/installation/)
 
Now, clone the repository from [here](https://github.com/elastest/elastest-device-emulator-service/blob/master/).
 
### Development procedure:

  * Using  *PyCharm IDE*:
    * Load/open the projects from IDE:
      * Import *EDS* project from local repository using File > Open --> select the project name elastest-device-emulator-service
     
      
   * From *IDE and console*:
     * Run *prep-env.sh* from the console to install all openmtc dependencies and to create the environment for zigbeeipe,memsipe and frontend services.
          ```
       $cd eds/FrontEnd/openmtc-gevent
       $./prep-env.sh
       
          ```
    
   * Go to the rest_app directory and run foolowing:
      ```
      pip install -r requirements.txt
      
      ```
     This will install all the dependencies to run the service properly and even to integrate the service with other Elastest component such as EMP and ESM.
   
### Locally:
   ## Run the gateway
    ```
    $cd eds/FrontEnd/openmtc-gevent
    $./run_gscl
      
          ```
   ## Run the application/frontend
    ```
    $cd eds/FrontEnd
    $./frontend
      
          ```
   ## Run the sensor application/memsipe
    ```
    $cd eds/MemsIPE
    $./mems-ipe
      
          ```  
          
   Open a browser and in the address bar write- localhost:6065/static/eds.html
   
   
## Run from Docker:
 This method allows docker to setup containers
and connect them in a custom network named **elastest_elastest**. In order to run the docker-compose file at first we need to 
  create the custom network. All the sensors register after 10 seconds with 
FrontEnd. 

Create custom network:
```shell
docker network create elastest_elastest
```

Start EDS using:  
```shell
chmod +x script/*
./script/startup-linux.sh
```
To stop EDS:
```shell
./script/teardown-linux.sh 
```

Check the ip for the diffferent application running from the docker:
```shell
docker network inspect elastest_elastest​
```
It gives the following output:
```
[
    {
        "Name": "elastest_elastest",
        "Id": "5309f972799c6a61fefc073b0d51a04aeddf0d49c129412526deaa472bcda426",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",

            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Containers": {
            "4fa0d8acfa556e28760522caa56219248336fb4b8c69277b00744bcb299eec15": {
                "Name": "eds_zigbeeipe_1",
                "EndpointID": "235f27a5214e66fb8a9afde11d7257f8beb7c0f85a4345e021682fa1d82cc982",
                "MacAddress": "02:42:ac:12:00:05",
                "IPv4Address": "172.18.0.5/16",
                "IPv6Address": ""
            },
            "788a38e739834e1befb86441900be503d6d021d6762ad766acfa25a96b6c5504": {
                "Name": "eds_frontend_1",
                "EndpointID": "ec928f6ebb4c4fa355cf1422c2aa17e9088e1e5b8d0f58e4e5c39a7bdbf93fa8",
                "MacAddress": "02:42:ac:12:00:04",
                "IPv4Address": "172.18.0.4/16",
                "IPv6Address": ""
            },
            "a0fc7d243e17e54fb08ee44dd3f7054babc7d9db47abc90945c84efbef55294e": {
                "Name": "eds_rest_app_1",
                "EndpointID": "5e9fd7857e8a79cd17f4f6c1fd48c09694d760c34d33813050ce3b605697f2af",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            },
            "e442540c2a448a1eb4c4bb1739db3862de762069ae9d0164056b297407a6226d": {
                "Name": "eds_memsipe_1",
                "EndpointID": "90827aae65f32a6fb0bfccf56b0fa56b5671261164d9cbee1bfac871323b1922",
                "MacAddress": "02:42:ac:12:00:03",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
    ]
```


Take the ip for the frontend service and write in the browser address bar : frontend_ip:6065/static/eds.html


### Docker images:
The following docker images are currently used in order to make the EDS work successfully:
 - elastest/eds-frontend: a service used as a GUI or frontend inorder to show all the sensors data in a graph view 
 formate as well as has capability to actuate sesor and actuator. The image associated to this service is accessible [here](https://hub.docker.com/r/elastest/eds-frontend/)
 - elastest/eds-api: a service contain restfull api that communicate with the elastest component. This service is based on
 OpenAPI specification.The image associated to this service is accessible [here](https://hub.docker.com/r/elastest/eds-api/)
 - elastest/eds-memsipe: a service with uses accelometers data such as x,y and z axes. The image associated to this service is accessible [here](https://hub.docker.com/r/elastest/eds-zigbeeipe/)
 - elastest/eds-zigbeeipe: a service for zigbee sensor protocol data such as vibration, temperature, movement etc. The image associated to this service is accessible [here](https://hub.docker.com/r/elastest/eds-memsipe/)
 
### Continuous Integration:
 * The Jenkins file for the EDS is accessible [here](https://github.com/elastest/elastest-device-emulator-service/blob/master/Jenkinsfile).
 * The Jenkins file for the end-to-end test of EDS is accessible [here](https://github.com/elastest/elastest-device-emulator-service/blob/master/e2e-test/Jenkinsfile).
