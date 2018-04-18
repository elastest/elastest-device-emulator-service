### Architecture:
 ![EDS screenshot examaple](image/eds_arch.jpg)

The entire application EDS consists of many services such as- memsipe, rest_app, and frontend. We divide the architecture as follows:
 - sensor/actuator based services/application which uses m2m communication protocol.
 - Application to visualize all the data and metrics coming from the sensor/actuator based services/application, which uses m2m communication protocol.
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
     * Run *prep-env.sh* from the console to install all OpenMTC dependencies and to create the environment for memsipe and frontend services.
          ```
       $cd eds/FrontEnd/openmtc-gevent
       $./prep-env.sh
       
          ```
    
   * Go to the rest_app directory and run following:
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
   ## Run the rest api
    ```
    $cd eds/rest_app
    $python eds.py
      
          ```  
   Open a browser and in the address bar write- localhost:6065/static/eds.html
   For rest_api frontend write: localhost:8080/eds/ui
   For api health check write localhost:9090/health
   ```
   {"status": "success", "timestamp": 1524044631.051784, "hostname": "c998dce9aceb", "results": [{"output": "up",
    "checker": "health_check", "expires": 1524044658.05173, "passed": "status", "timestamp": 1524044631.05173}]}
   
   ```
   
   For api environment check write: localhost:9090/environment
```
{"python": {"pythonpath": ["/usr/src/app", "/usr/local/lib/python27.zip", "/usr/local/lib/python2.7", 
"/usr/local/lib/python2.7/plat-linux2", "/usr/local/lib/python2.7/lib-tk", "/usr/local/lib/python2.7/lib-old", 
"/usr/local/lib/python2.7/lib-dynload", "/usr/local/lib/python2.7/site-packages"], 
"executable": "/usr/local/bin/python", "version": "2.7.14 (default, Jan 10 2018, 05:41:02) \n[GCC 5.3.0]", 
"packages": {"inflection": "0.3.1", "backports.ssl-match-hostname": "3.5.0.1", "Flask": "0.12.2", "kazoo": "2.4.0",
 "cached-property": "1.4.2", "dockerpty": "0.4.1", "singledispatch": "3.4.0.3", "jsonschema": "2.6.0",
  "Werkzeug": "0.14.1", "pip": "9.0.3", "clickclick": "1.2.2", "oauth2client": "4.1.2", "pykafka": "2.7.0", 
  "tabulate": "0.8.2", "oauthlib": "2.0.7", "pykube": "0.15.0", "backports-abc": "0.5", "ipaddress": "1.0.22",
   "six": "1.11.0", "pathlib": "1.0.1", "docker-pycreds": "0.2.2", "click": "6.7", "Jinja2": "2.10", "connexion": "1.4",
    "typing": "3.6.4", "chardet": "3.0.4", "itsdangerous": "0.24", "swagger-spec-validator": "2.1.0",
     "websocket-client": "0.47.0", "wheel": "0.30.0", "PyYAML": "3.12", "tornado": "5.0.2", "healthcheck": "1.3.2", 
     "urllib3": "1.22", "rsa": "3.4.2", "MarkupSafe": "1.0", "pytz": "2018.4", "tzlocal": "1.5.1", "httplib2": "0.11.3",
      "functools32": "3.2.3.post2", "python-dateutil": "2.7.2", "texttable": "0.9.1", "pyasn1-modules": "0.2.1",
       "docker": "3.2.1", "certifi": "2018.4.16", "enum34": "1.1.6", "idna": "2.6", "futures": "3.2.0", 
       "requests-oauthlib": "0.8.0", "setuptools": "39.0.1", "docker-compose": "1.21.0", "requests": "2.18.4", "docopt":
        "0.6.2", "pyasn1": "0.4.2"}, "version_info": {"micro": 14, "major": 2, "releaselevel": "final", "serial": 0, "minor": 7}},
         "process": {"environ": {"LANG": "C.UTF-8", "ci_env": "`bash <(curl -s https://codecov.io/env)`",
          "GPG_KEY": "********", "PYTHON_VERSION": "2.7.14", "PYTHON_PIP_VERSION": "9.0.3", "HOSTNAME": "c998dce9aceb",
           "EDS_PORT": "8080", "EDS_CHECK_PORT": "9090", "PATH": "/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HOME": "/root"}, "pid": 1, "cwd": "/usr/src/app", "argv": ["eds.py"], "user": "root"}, "config": {"JSON_AS_ASCII": true, "SESSION_COOKIE_PATH": null, "LOGGER_NAME": "check_api", "SECRET_KEY": "********", "APPLICATION_ROOT": null, "SERVER_NAME": null, "PREFERRED_URL_SCHEME": "http", "TESTING": false, "TEMPLATES_AUTO_RELOAD": null, "JSONIFY_MIMETYPE": "application/json", "SESSION_REFRESH_EACH_REQUEST": true, "TRAP_HTTP_EXCEPTIONS": false, "USE_X_SENDFILE": false, "SESSION_COOKIE_SECURE": false, "SESSION_COOKIE_DOMAIN": null, "SESSION_COOKIE_NAME": "session", "LOGGER_HANDLER_POLICY": "always", "DEBUG": false, "EXPLAIN_TEMPLATE_LOADING": false, "MAX_CONTENT_LENGTH": null, "JSONIFY_PRETTYPRINT_REGULAR": true, "PROPAGATE_EXCEPTIONS": null, "TRAP_BAD_REQUEST_ERRORS": false, "JSON_SORT_KEYS": "********", "SESSION_COOKIE_HTTPONLY": true, "PRESERVE_CONTEXT_ON_EXCEPTION": null}, "os": {"platform": "linux2", "name": "posix", "uname": ["Linux", "c998dce9aceb", "4.4.0-79-generic", "#100-Ubuntu SMP Wed May 17 19:58:14 UTC 2017", "x86_64"]}, "application": {"maintainer": "ElasTest", "git_repo": "https://github.com/elastest/elastest-device-emulator-service"}}
```


   
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
 
### Continuous Integration:
 * The Jenkins file for the EDS is accessible [here](https://github.com/elastest/elastest-device-emulator-service/blob/master/Jenkinsfile).
 * The Jenkins file for the end-to-end test of EDS is accessible [here](https://github.com/elastest/elastest-device-emulator-service/blob/master/e2e-test/Jenkinsfile).
