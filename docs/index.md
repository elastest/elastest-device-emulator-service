[![][ElasTest Logo]][ElasTest]

Copyright © 2017-2019 Technishce Universitaet Berlin. Licensed under
[Apache 2.0 License].

# ElasTest Device Emulator Service

Elastest Device-Emulator Service (EDS) emulates the behaviors of 
the sensors, actuators and smart devices. 

EDS follows a Service Oriented Architecture (SOA). The service in this context
 is a light-weight micro-service. Furthermore, several micro-services are 
linked together to achieve the goals of EDS. The aim of a micro-service in EDS
is to run the functions of an emulator for a device which could be a sensor,
actuator or a smart device.
  
Additionally a micro-service called FrontEnd connects to the other 
micro-services to provide a common interface for the user to access all micro-
services. 

The micro-services use [oneM2M](http://onem2m.org) for communication. Furthermore
an Interworking Proxy (IPE) is used to transfer data from a non-oneM2M domain 
to oneM2M domain. The available micro-services supporting oneM2M in the present
release of EDS are:


* MemsIPE : Provides simulated data from the accelerometer sensor containing 
values for x, y and z components of acceleration. 
* FrontEnd : Provides a user interface to interact with MemsIPE and ZigBeeIPE.
A user interface (UI) displays the data from micro-services. 
* rest_app : Provides an interaction UI using RESTful API.In order to use the 
facility of the EDS, its API is used. The API is based upon the 
latest (2.12) version of the Open Service Broker API. To this end there are some 
specific ElasTest extensions added.

EDS runs each micro-service in a docker container, the containers are linked 
together to link the micro-services.

# Clone the Project
```shell
#Clone the project to your system
#Alternatively, you can download the zip file from Github and unzip it
git clone git@github.com:elastest/elastest-device-emulator-service.git

#Change working directory to main project folder
cd elastest-device-emulator-service
```

# How to run
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

# Basic usage
The Frontend operates a gateway which accepts curl requests to return the 
simulated sensor data posted by MemsIPE and ZigBeeIPE in the JSON format on port 8000.
All the data that follows are simulated through EDS.

Request to show registered oneM2M IPEs:

```shell

$ curl http://172.18.0.5:8000/onem2m -s | jq '.'


{
  "m2m:cb": {
    "ch": [

      {
        "typ": 2,
        "nm": "FrontEnd",
        "val": "ae0"
      },
      {
        "typ": 2,
        "nm": "MemsIPE",
        "val": "ae1"
      }
    ],
    "csi": "/mn-cse-1",
    "ri": "cb0",
    "ty": 5,
    "lt": "2017-10-19T09:54:35.095747+00:00",
    "srt": [
      16,
      23,
      4,
      5,
      3,
      2
    ],
    "cst": 2,
    "rn": "onem2m",
    "ct": "2017-10-19T09:54:35.095747+00:00",
    "poa": [
      "http://127.0.0.1:8000",
      "http://[::1]:8000",
      "http://172.18.0.5:8000"
    ]
  }
}


```
### Requests to ZigBeeIPE

Request to access ZigBeeIPE:

```shell
$ curl http://localhost:8000/onem2m/ZigBeeIPE -s | jq '.'
Output:
{
  "m2m:ae": {
    "ri": "ae1",
    "nl": "dummy",
    "rr": false,
    "ty": 2,
    "et": "2017-08-29T16:45:39.003547+00:00",
    "ch": [
      {
        "typ": 3,
        "nm": "devices",
        "val": "cnt0"
      }
    ],
    "lt": "2017-08-29T16:25:39.012676+00:00",
    "api": "dummy",
    "aei": "CZigBeeIPE",
    "pi": "cb0",
    "rn": "ZigBeeIPE",
    "poa": [
      "http://10.50.0.2:5001"
    ],
    "ct": "2017-08-29T15:26:39.806291+00:00"
  }
}

```

Request to show available devices on ZigBeeIPE:

```shell
$ curl http://localhost:8000/onem2m/ZigBeeIPE/devices -s | jq '.'

{
  "m2m:cnt": {
    "ch": [
      {
        "typ": 3,
        "nm": "ZBS122S000001",
        "val": "cnt1"
      },
      {
        "typ": 3,
        "nm": "ZBS122S000000",
        "val": "cnt6"
      }
    ],
    "mni": 30,
    "cr": "CZigBeeIPE",
    "et": "2017-08-29T16:55:39.048780+00:00",
    "ty": 3,
    "lt": "2017-08-29T16:35:39.098708+00:00",
    "rn": "devices",
    "ct": "2017-08-29T15:26:39.900545+00:00",
    "ri": "cnt0",
    "cni": 0,
    "cbs": 0,
    "pi": "ae1",
    "st": "0"
  }
}

```
Request to access list of sensors in ID ZBS122S000001. This returns available
sensors namely light, pressure, movement, humidity and temperature.

```shell
$ curl http://localhost:8000/onem2m/ZigBeeIPE/devices/ZBS122S000001/sensor_data -s | jq '.'

{
  "m2m:cnt": {
    "ch": [
      {
        "typ": 3,
        "nm": "brightness",
        "val": "cnt17"
      },
      {
        "typ": 3,
        "nm": "pressure",
        "val": "cnt19"
      },
      {
        "typ": 3,
        "nm": "movement",
        "val": "cnt21"
      },
      {
        "typ": 3,
        "nm": "humidity",
        "val": "cnt20"
      },
      {
        "typ": 3,
        "nm": "temperature",
        "val": "cnt18"
      }
    ],
    "mni": 30,
    "cr": "CZigBeeIPE",
    "et": "2017-08-29T17:05:50.104399+00:00",
    "ty": 3,
    "lt": "2017-08-29T16:45:50.148437+00:00",
    "rn": "sensor_data",
    "ct": "2017-08-29T15:26:50.508627+00:00",
    "ri": "cnt16",
    "cni": 0,
    "cbs": 0,
    "pi": "cnt1",
    "st": "0"
  }
}

```

Request to receive latest data from the temperature sensor. Please note that the 
reply from the curl request is base64 decoded.

```shell

$ curl http://localhost:8000/onem2m/ZigBeeIPE/devices/ZBS122S000001/sensor_data/temperature/latest \
-s | jq -r '.["m2m:cin"].con' | base64 -d | jq '.'

[
  {
    "bn": "urn:dev:xbee:ZBS122S000001",
    "v": 17.5,
    "u": "Cel",
    "t": "1504025850.892",
    "n": "temperature"
  }
]

```
Request to receive latest data from the humidity sensor. Please note that the 
reply from the curl request is base64 decoded. Furthermore this can be repeated 
for the remaining sensors.

```shell

$ curl http://localhost:8000/onem2m/ZigBeeIPE/devices/ZBS122S000001/sensor_data/humidity/latest \
-s | jq -r '.["m2m:cin"].con' | base64 -d | jq '.'

[
  {
    "bn": "urn:dev:xbee:ZBS122S000001",
    "v": 84,
    "u": "%RH",
    "t": "1504026051.652",
    "n": "humidity"
  }
]

```
### Requests to MemsIPE

Request to show available sensors in MemsIPE:

```shell
$ curl http://localhost:8000/onem2m/MemsIPE/sensor_data/ -s | jq '.'

{
  "m2m:cnt": {
    "ch": [
      {
        "typ": 3,
        "nm": "x",
        "val": "cnt3"
      },
      {
        "typ": 3,
        "nm": "y",
        "val": "cnt4"
      },
      {
        "typ": 3,
        "nm": "z",
        "val": "cnt5"
      }
    ],
    "mni": 10,
    "cr": "CMemsIPE",
    "et": "2017-08-29T17:15:39.122764+00:00",
    "lbl": [
      "sensor_data",
      "openmtc:device"
    ],
    "ty": 3,
    "lt": "2017-08-29T16:55:39.171379+00:00",
    "rn": "sensor_data",
    "ct": "2017-08-29T15:26:39.996691+00:00",
    "ri": "cnt2",
    "cni": 0,
    "cbs": 0,
    "pi": "ae2",
    "st": "0"
  }
}

```
Request to receive the latest reading from the z axis of the accelerometer. 
Please note that the returned value is to be base64 decoded. A similar approach
can be followed for x and y axes.

```shell

curl http://localhost:8000/onem2m/MemsIPE/sensor_data/z/latest -s | jq -r '.["m2m:cin"].con' | base64 -d | jq '.'

[
  {
    "bn": "urn:dev1:memsipe",
    "v": 0.016461689528667167,
    "u": "g",
    "t": "1504026602.834",
    "n": "z"
  }
]

```

### Access EDS FrontEnd user interface

This user interface displays plots in real time the data received from various 
senors of the ZigBeeIPE and MemsIPE. This can be accessed on a browser using the 
link:

```shell
http://localhost:6065/static/eds.html
```

### Access API UI 
Swagger UI provides the RESTful API available with EDS. The linking of API to 
different IPE is to be done. 

```shell
http://localhost:8080/eds/ui/
```

### Using the Health API
There are two endpoints that are available to check the health of the EDS

* `http://$localhost:$EDS_CHECK_PORT/healthcheck`: this current performs a very simple check. 
* `http://$localhost:$EDS_CHECK_PORT/environment`: returns environment settings which the EDS is loaded with.

Both endpoints only support GET. Below is the output of issuing the HTTP GET to each endpoint.

#### /health Endpoint


```shell
$  curl http://localhost:2020/healthcheck
{"status": "success", "timestamp": 1511454626.521588, "hostname": "sro-thinkpad", "results": [{"output": "up", "checker": "health_check", "expires": 1511454653.521551, "passed": "status", "timestamp": 1511454626.521551}]}
```


# Development documentation
TBD

# Source

Source code for other ElasTest projects can be found in the [GitHub ElasTest
Group].

# News

Check the [ElasTest Blog] and follow us on Twitter [@elastestio][ElasTest Twitter].

# Issue tracker

Issues and bug reports should be posted to the [GitHub ElasTest Bugtracker].

# Licensing and distribution

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# Contribution policy

You can contribute to the ElasTest community through bug-reports, bug-fixes,
new code or new documentation. For contributing to the ElasTest community,
you can use GitHub, providing full information about your contribution and its
value. In your contributions, you must comply with the following guidelines

* You must specify the specific contents of your contribution either through a
  detailed bug description, through a pull-request or through a patch.
* You must specify the licensing restrictions of the code you contribute.
* For newly created code to be incorporated in the ElasTest code-base, you
  must accept ElasTest to own the code copyright, so that its open source
  nature is guaranteed.
* You must justify appropriately the need and value of your contribution. The
  ElasTest project has no obligations in relation to accepting contributions
  from third parties.
* The ElasTest project leaders have the right of asking for further
  explanations, tests or validations of any code contributed to the community
  before it being incorporated into the ElasTest code-base. You must be ready
  to addressing all these kind of concerns before having your code approved.

# Support

The ElasTest project provides community support through the [ElasTest Public
Mailing List] and through [StackOverflow] using the tag *elastest*.


<p align="center">
  <img src="http://elastest.io/images/logos_elastest/ue_logo-small.png"><br>
  Funded by the European Union
</p>

[Apache 2.0 License]: http://www.apache.org/licenses/LICENSE-2.0
[ElasTest]: http://elastest.io/
[ElasTest Blog]: http://elastest.io/blog/
[ElasTest Doc]: http://elastest.io/docs/
[ElasTest Logo]: http://elastest.io/images/logos_elastest/elastest-logo-gray-small.png
[ElasTest Public Mailing List]: https://groups.google.com/forum/#!forum/elastest-users
[ElasTest Twitter]: https://twitter.com/elastestio
[GitHub ElasTest Group]: https://github.com/elastest
[GitHub ElasTest Bugtracker]: https://github.com/elastest/bugtracker
[StackOverflow]: http://stackoverflow.com/questions/tagged/elastest
[Universidad Rey Juan Carlos]: https://www.urjc.es/

