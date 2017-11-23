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



```shell
$ curl http://localhost:2020/environment | jq '.'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  9774  100  9774    0     0   555k      0 --:--:-- --:--:-- --:--:--  596k
{
  "python": {
    "pythonpath": [
      "/home/sro/Desktop/final_eds/elastest-device-emulator-service/eds/rest_app",
      "/usr/lib/python2.7",
      "/usr/lib/python2.7/plat-x86_64-linux-gnu",
      "/usr/lib/python2.7/lib-tk",
      "/usr/lib/python2.7/lib-old",
      "/usr/lib/python2.7/lib-dynload",
      "/home/sro/.local/lib/python2.7/site-packages",
      "/usr/local/lib/python2.7/dist-packages",
      "/usr/local/lib/python2.7/dist-packages/virtualenv-15.1.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/openmtc_sdk-4.99.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/eds_api-1.0.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/typing-3.6.2-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/swagger_server-1.0.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/esm-0.1.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/connexion-1.0.129-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/swagger_client-1.0.0-py2.7.egg",
      "/usr/lib/python2.7/dist-packages",
      "/usr/lib/python2.7/dist-packages/gtk-2.0"
    ],
    "executable": "/usr/bin/python",
    "version": "2.7.12 (default, Nov 19 2016, 06:48:10) \n[GCC 5.4.0 20160609]",
    "packages": {
      "backports.ssl-match-hostname": "3.5.0.1",
      "Flask": "0.12.2",
      "funcy": "1.7.3",
      "Werkzeug": "0.12.2",
      "swagger-client": "1.0.0",
      "oauthlib": "2.0.2",
      "swagger-server": "1.0.0",
      "inflection": "0.3.1",
      "blist": "1.3.6",
      "Jinja2": "2.9.6",
      "decorator": "4.0.11",
      "itsdangerous": "0.24",
      "ipaddress": "1.0.16",
      "openmtc-sdk": "4.99.0",
      "MarkupSafe": "1.0",
      "nbxmpp": "0.5.3",
      "tzlocal": "1.4",
      "httplib2": "0.10.3",
      "Pillow": "3.1.2",
      "pluggy": "0.4.0",
      "ndg-httpsclient": "0.4.0",
      "iotop": "0.6",
      "Dtls": "1.0.1",
      "pbr": "1.8.0",
      "pyOpenSSL": "0.15.1",
      "mercurial": "3.7.3",
      "scapy": "2.2.0",
      "vboxapi": "1.0",
      "bzr-etckeeper": "0.0.0",
      "setupfiles": "0.0.50",
      "greenlet": "0.4.12",
      "nose": "1.3.7",
      "python-socketio": "1.7.1",
      "docker-py": "1.9.0",
      "funcsigs": "0.4",
      "gevent": "1.2.1",
      "jsonschema": "2.6.0",
      "codecov": "2.0.9",
      "gpio": "0.2.0",
      "click": "6.7",
      "tabulate": "0.8.1",
      "virtualenv": "15.1.0",
      "flask-htpasswd": "0.3.1",
      "passlib": "1.7.1",
      "adium-theme-ubuntu": "0.3.4",
      "ujson": "1.35",
      "pathlib": "1.0.1",
      "RPi.GPIO": "0.6.3",
      "requests-oauthlib": "0.8.0",
      "esm": "0.1.0",
      "swagger-spec-validator": "2.1.0",
      "uWSGI": "2.0.15",
      "setuptools": "36.2.7",
      "cached-property": "1.3.0",
      "pygobject": "3.20.0",
      "texttable": "0.8.1",
      "backports-abc": "0.5",
      "linecache2": "1.0.0",
      "logging": "0.4.9.6",
      "requests": "2.18.4",
      "docopt": "0.6.2",
      "pyasn1": "0.1.9",
      "daiquiri": "1.2.2",
      "kazoo": "2.4.0",
      "PyXB": "1.2.3",
      "XBee": "2.2.3",
      "unity-lens-photos": "1.0",
      "clickclick": "1.2.2",
      "connexion": "1.0.129",
      "docker-pycreds": "0.2.1",
      "traceback2": "1.4.0",
      "tox": "2.7.0",
      "log": "0.0.2",
      "freeopcua": "0.90.2",
      "py": "1.4.34",
      "typing": "3.5.2.2",
      "certifi": "2017.7.27.1",
      "numpy": "1.12.0",
      "websocket-client": "0.44.0",
      "python-engineio": "1.2.4",
      "rsa": "3.4.2",
      "trollius": "2.1",
      "iso8601": "0.1.11",
      "pytz": "2016.10",
      "functools32": "3.2.3.post2",
      "python-dateutil": "2.6.0",
      "pykafka": "2.6.0",
      "smbus": "1.1",
      "cryptography": "1.2.3",
      "pycrypto": "2.6.1",
      "mimeparse": "0.1.3",
      "chardet": "3.0.4",
      "serial-device": "0.4.post4",
      "py3": "0.0.0",
      "eds-api": "1.0.0",
      "dockerpty": "0.4.1",
      "singledispatch": "3.4.0.3",
      "pip": "9.0.1",
      "oauth2client": "4.1.2",
      "pyserial": "3.3",
      "strict-rfc3339": "0.7",
      "pykube": "0.15.0",
      "simplejson": "3.10.0",
      "docker-compose": "1.15.0",
      "six": "1.10.0",
      "smbus2": "0.2.0",
      "pymongo": "3.4.0",
      "pandas": "0.19.2",
      "mock": "1.3.0",
      "wheel": "0.29.0",
      "geventhttpclient": "1.3.1",
      "PyYAML": "3.12",
      "tornado": "4.5.1",
      "healthcheck": "1.3.2",
      "urllib3": "1.22",
      "paho-mqtt": "1.2",
      "epm-client": "1.0.0",
      "colorama": "0.3.9",
      "coverage": "4.4.1",
      "pyasn1-modules": "0.0.11",
      "gevent-websocket": "0.9.5",
      "tblib": "1.3.0",
      "enum34": "1.1.6",
      "futures": "3.0.5",
      "netifaces": "0.10.5",
      "simpy": "3.0.10",
      "docker": "2.4.2",
      "idna": "2.6"
    },
    "version_info": {
      "micro": 12,
      "major": 2,
      "releaselevel": "final",
      "serial": 0,
      "minor": 7
    }
  },
  "process": {
    "environ": {
      "LC_NUMERIC": "de_DE.UTF-8",
      "QT_QPA_PLATFORMTHEME": "appmenu-qt5",
      "XDG_GREETER_DATA_DIR": "/var/lib/lightdm-data/sro",
      "GNOME_DESKTOP_SESSION_ID": "this-is-deprecated",
      "LC_MEASUREMENT": "de_DE.UTF-8",
      "UPSTART_EVENTS": "xsession started",
      "XDG_CURRENT_DESKTOP": "Unity",
      "XDG_VTNR": "7",
      "QT_IM_MODULE": "ibus",
      "LOGNAME": "sro",
      "USER": "sro",
      "PATH": "/usr/bin:/usr/local/bin:/home/sro/bin:/home/sro/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin",
      "LC_PAPER": "de_DE.UTF-8",
      "GNOME_KEYRING_CONTROL": "********",
      "NODE_PATH": "/usr/lib/nodejs:/usr/lib/node_modules:/usr/share/javascript",
      "LD_LIBRARY_PATH": "/home/sro/Desktop/pycharm-2016.3.2/bin:",
      "LANG": "en_US.UTF-8",
      "TERM": "xterm-256color",
      "SHELL": "/bin/bash",
      "XDG_SESSION_PATH": "/org/freedesktop/DisplayManager/Session0",
      "XAUTHORITY": "/home/sro/.Xauthority",
      "LANGUAGE": "en_US",
      "INSTANCE": "",
      "LC_MONETARY": "de_DE.UTF-8",
      "QT_LINUX_ACCESSIBILITY_ALWAYS_ON": "1",
      "NLSPATH": "/usr/dt/lib/nls/msg/%L/%N.cat",
      "MANDATORY_PATH": "/usr/share/gconf/ubuntu.mandatory.path",
      "CLUTTER_IM_MODULE": "xim",
      "DISPLAY": ":0",
      "UPSTART_INSTANCE": "",
      "COMPIZ_CONFIG_PROFILE": "ubuntu",
      "SESSION": "ubuntu",
      "XFILESEARCHPATH": "/usr/dt/app-defaults/%L/Dt",
      "SESSIONTYPE": "gnome-session",
      "XMODIFIERS": "@im=ibus",
      "GIO_LAUNCHED_DESKTOP_FILE_PID": "6808",
      "JAVA_HOME": "/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java",
      "HOME": "/home/sro",
      "QT4_IM_MODULE": "xim",
      "GTK2_MODULES": "overlay-scrollbar",
      "XDG_SESSION_DESKTOP": "ubuntu",
      "GIO_LAUNCHED_DESKTOP_FILE": "/home/sro/.local/share/applications/jetbrains-pycharm.desktop",
      "XDG_RUNTIME_DIR": "/run/user/1000",
      "LC_IDENTIFICATION": "de_DE.UTF-8",
      "LC_ADDRESS": "de_DE.UTF-8",
      "SSH_AUTH_SOCK": "/run/user/1000/keyring/ssh",
      "GDMSESSION": "ubuntu",
      "IM_CONFIG_PHASE": "1",
      "UPSTART_JOB": "unity7",
      "UPSTART_SESSION": "unix:abstract=/com/ubuntu/upstart-session/1000/2441",
      "QT_ACCESSIBILITY": "1",
      "XDG_SEAT_PATH": "/org/freedesktop/DisplayManager/Seat0",
      "BASH_FUNC_generate_command_executed_sequence%%": "() {  printf '\\e\\7'\n}",
      "LESSOPEN": "| /usr/bin/lesspipe %s",
      "XDG_SESSION_ID": "c2",
      "DBUS_SESSION_BUS_ADDRESS": "unix:abstract=/tmp/dbus-VibE3DAiGP",
      "_": "/usr/bin/python",
      "DEFAULTS_PATH": "/usr/share/gconf/ubuntu.default.path",
      "GTK_IM_MODULE": "ibus",
      "DESKTOP_SESSION": "ubuntu",
      "GPG_AGENT_INFO": "/home/sro/.gnupg/S.gpg-agent:0:1",
      "LESSCLOSE": "/usr/bin/lesspipe %s %s",
      "GNOME_KEYRING_PID": "********",
      "XDG_SESSION_TYPE": "x11",
      "OLDPWD": "/home/sro/Desktop/final_eds/elastest-device-emulator-service",
      "LS_COLORS": "rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:",
      "GDM_LANG": "en_US",
      "LC_TELEPHONE": "de_DE.UTF-8",
      "GTK_MODULES": "gail:atk-bridge:unity-gtk-module",
      "SHLVL": "1",
      "PWD": "/home/sro/Desktop/final_eds/elastest-device-emulator-service/eds/rest_app",
      "JOB": "unity-settings-daemon",
      "LC_NAME": "de_DE.UTF-8",
      "LC_TIME": "de_DE.UTF-8",
      "XDG_CONFIG_DIRS": "/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg",
      "COMPIZ_BIN_PATH": "/usr/bin/",
      "XDG_DATA_DIRS": "/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop",
      "XDG_SEAT": "seat0"
    },
    "pid": 29006,
    "cwd": "/home/sro/Desktop/final_eds/elastest-device-emulator-service/eds/rest_app",
    "argv": [
      "resty.py"
    ],
    "user": "sro"
  },
  "config": {
    "JSON_AS_ASCII": true,
    "SESSION_COOKIE_PATH": null,
    "LOGGER_NAME": "__main__",
    "SECRET_KEY": "********",
    "APPLICATION_ROOT": null,
    "SERVER_NAME": null,
    "PREFERRED_URL_SCHEME": "http",
    "TESTING": false,
    "TEMPLATES_AUTO_RELOAD": null,
    "JSONIFY_MIMETYPE": "application/json",
    "SESSION_REFRESH_EACH_REQUEST": true,
    "TRAP_HTTP_EXCEPTIONS": false,
    "USE_X_SENDFILE": false,
    "SESSION_COOKIE_SECURE": false,
    "SESSION_COOKIE_DOMAIN": null,
    "SESSION_COOKIE_NAME": "session",
    "LOGGER_HANDLER_POLICY": "always",
    "DEBUG": false,
    "EXPLAIN_TEMPLATE_LOADING": false,
    "MAX_CONTENT_LENGTH": null,
    "JSONIFY_PRETTYPRINT_REGULAR": true,
    "PROPAGATE_EXCEPTIONS": null,
    "TRAP_BAD_REQUEST_ERRORS": false,
    "JSON_SORT_KEYS": "********",
    "SESSION_COOKIE_HTTPONLY": true,
    "PRESERVE_CONTEXT_ON_EXCEPTION": null
  },
  "os": {
    "platform": "linux2",
    "name": "posix",
    "uname": [
      "Linux",
      "sro-thinkpad",
      "4.4.0-79-generic",
      "#100-Ubuntu SMP Wed May 17 19:58:14 UTC 2017",
      "x86_64"
    ]
  },
  "application": {
    "maintainer": "ElasTest",
    "git_repo": "https://github.com/elastest/elastest-device-emulator-service"
  }
}
sro@sro-thinkpad:~/Desktop/final_eds/elastest-device-emulator-service/eds/ZigBeeIPE$ 
sro@sro-thinkpad:~/Desktop/final_eds/elastest-device-emulator-service/eds/ZigBeeIPE$ curl http://localhost:2020/environment | jq 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  9774  100  9774    0     0   803k      0 --:--:-- --:--:-- --:--:--  867k
{
  "python": {
    "pythonpath": [
      "/home/sro/Desktop/final_eds/elastest-device-emulator-service/eds/rest_app",
      "/usr/lib/python2.7",
      "/usr/lib/python2.7/plat-x86_64-linux-gnu",
      "/usr/lib/python2.7/lib-tk",
      "/usr/lib/python2.7/lib-old",
      "/usr/lib/python2.7/lib-dynload",
      "/home/sro/.local/lib/python2.7/site-packages",
      "/usr/local/lib/python2.7/dist-packages",
      "/usr/local/lib/python2.7/dist-packages/virtualenv-15.1.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/openmtc_sdk-4.99.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/eds_api-1.0.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/typing-3.6.2-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/swagger_server-1.0.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/esm-0.1.0-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/connexion-1.0.129-py2.7.egg",
      "/usr/local/lib/python2.7/dist-packages/swagger_client-1.0.0-py2.7.egg",
      "/usr/lib/python2.7/dist-packages",
      "/usr/lib/python2.7/dist-packages/gtk-2.0"
    ],
    "executable": "/usr/bin/python",
    "version": "2.7.12 (default, Nov 19 2016, 06:48:10) \n[GCC 5.4.0 20160609]",
    "packages": {
      "backports.ssl-match-hostname": "3.5.0.1",
      "Flask": "0.12.2",
      "funcy": "1.7.3",
      "Werkzeug": "0.12.2",
      "swagger-client": "1.0.0",
      "oauthlib": "2.0.2",
      "swagger-server": "1.0.0",
      "inflection": "0.3.1",
      "blist": "1.3.6",
      "Jinja2": "2.9.6",
      "decorator": "4.0.11",
      "itsdangerous": "0.24",
      "ipaddress": "1.0.16",
      "openmtc-sdk": "4.99.0",
      "MarkupSafe": "1.0",
      "nbxmpp": "0.5.3",
      "tzlocal": "1.4",
      "httplib2": "0.10.3",
      "Pillow": "3.1.2",
      "pluggy": "0.4.0",
      "ndg-httpsclient": "0.4.0",
      "iotop": "0.6",
      "Dtls": "1.0.1",
      "pbr": "1.8.0",
      "pyOpenSSL": "0.15.1",
      "mercurial": "3.7.3",
      "scapy": "2.2.0",
      "vboxapi": "1.0",
      "bzr-etckeeper": "0.0.0",
      "setupfiles": "0.0.50",
      "greenlet": "0.4.12",
      "nose": "1.3.7",
      "python-socketio": "1.7.1",
      "docker-py": "1.9.0",
      "funcsigs": "0.4",
      "gevent": "1.2.1",
      "jsonschema": "2.6.0",
      "codecov": "2.0.9",
      "gpio": "0.2.0",
      "click": "6.7",
      "tabulate": "0.8.1",
      "virtualenv": "15.1.0",
      "flask-htpasswd": "0.3.1",
      "passlib": "1.7.1",
      "adium-theme-ubuntu": "0.3.4",
      "ujson": "1.35",
      "pathlib": "1.0.1",
      "RPi.GPIO": "0.6.3",
      "requests-oauthlib": "0.8.0",
      "esm": "0.1.0",
      "swagger-spec-validator": "2.1.0",
      "uWSGI": "2.0.15",
      "setuptools": "36.2.7",
      "cached-property": "1.3.0",
      "pygobject": "3.20.0",
      "texttable": "0.8.1",
      "backports-abc": "0.5",
      "linecache2": "1.0.0",
      "logging": "0.4.9.6",
      "requests": "2.18.4",
      "docopt": "0.6.2",
      "pyasn1": "0.1.9",
      "daiquiri": "1.2.2",
      "kazoo": "2.4.0",
      "PyXB": "1.2.3",
      "XBee": "2.2.3",
      "unity-lens-photos": "1.0",
      "clickclick": "1.2.2",
      "connexion": "1.0.129",
      "docker-pycreds": "0.2.1",
      "traceback2": "1.4.0",
      "tox": "2.7.0",
      "log": "0.0.2",
      "freeopcua": "0.90.2",
      "py": "1.4.34",
      "typing": "3.5.2.2",
      "certifi": "2017.7.27.1",
      "numpy": "1.12.0",
      "websocket-client": "0.44.0",
      "python-engineio": "1.2.4",
      "rsa": "3.4.2",
      "trollius": "2.1",
      "iso8601": "0.1.11",
      "pytz": "2016.10",
      "functools32": "3.2.3.post2",
      "python-dateutil": "2.6.0",
      "pykafka": "2.6.0",
      "smbus": "1.1",
      "cryptography": "1.2.3",
      "pycrypto": "2.6.1",
      "mimeparse": "0.1.3",
      "chardet": "3.0.4",
      "serial-device": "0.4.post4",
      "py3": "0.0.0",
      "eds-api": "1.0.0",
      "dockerpty": "0.4.1",
      "singledispatch": "3.4.0.3",
      "pip": "9.0.1",
      "oauth2client": "4.1.2",
      "pyserial": "3.3",
      "strict-rfc3339": "0.7",
      "pykube": "0.15.0",
      "simplejson": "3.10.0",
      "docker-compose": "1.15.0",
      "six": "1.10.0",
      "smbus2": "0.2.0",
      "pymongo": "3.4.0",
      "pandas": "0.19.2",
      "mock": "1.3.0",
      "wheel": "0.29.0",
      "geventhttpclient": "1.3.1",
      "PyYAML": "3.12",
      "tornado": "4.5.1",
      "healthcheck": "1.3.2",
      "urllib3": "1.22",
      "paho-mqtt": "1.2",
      "epm-client": "1.0.0",
      "colorama": "0.3.9",
      "coverage": "4.4.1",
      "pyasn1-modules": "0.0.11",
      "gevent-websocket": "0.9.5",
      "tblib": "1.3.0",
      "enum34": "1.1.6",
      "futures": "3.0.5",
      "netifaces": "0.10.5",
      "simpy": "3.0.10",
      "docker": "2.4.2",
      "idna": "2.6"
    },
    "version_info": {
      "micro": 12,
      "major": 2,
      "releaselevel": "final",
      "serial": 0,
      "minor": 7
    }
  },
  "process": {
    "environ": {
      "LC_NUMERIC": "de_DE.UTF-8",
      "QT_QPA_PLATFORMTHEME": "appmenu-qt5",
      "XDG_GREETER_DATA_DIR": "/var/lib/lightdm-data/sro",
      "GNOME_DESKTOP_SESSION_ID": "this-is-deprecated",
      "LC_MEASUREMENT": "de_DE.UTF-8",
      "UPSTART_EVENTS": "xsession started",
      "XDG_CURRENT_DESKTOP": "Unity",
      "XDG_VTNR": "7",
      "QT_IM_MODULE": "ibus",
      "LOGNAME": "sro",
      "USER": "sro",
      "PATH": "/usr/bin:/usr/local/bin:/home/sro/bin:/home/sro/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin",
      "LC_PAPER": "de_DE.UTF-8",
      "GNOME_KEYRING_CONTROL": "********",
      "NODE_PATH": "/usr/lib/nodejs:/usr/lib/node_modules:/usr/share/javascript",
      "LD_LIBRARY_PATH": "/home/sro/Desktop/pycharm-2016.3.2/bin:",
      "LANG": "en_US.UTF-8",
      "TERM": "xterm-256color",
      "SHELL": "/bin/bash",
      "XDG_SESSION_PATH": "/org/freedesktop/DisplayManager/Session0",
      "XAUTHORITY": "/home/sro/.Xauthority",
      "LANGUAGE": "en_US",
      "INSTANCE": "",
      "LC_MONETARY": "de_DE.UTF-8",
      "QT_LINUX_ACCESSIBILITY_ALWAYS_ON": "1",
      "NLSPATH": "/usr/dt/lib/nls/msg/%L/%N.cat",
      "MANDATORY_PATH": "/usr/share/gconf/ubuntu.mandatory.path",
      "CLUTTER_IM_MODULE": "xim",
      "DISPLAY": ":0",
      "UPSTART_INSTANCE": "",
      "COMPIZ_CONFIG_PROFILE": "ubuntu",
      "SESSION": "ubuntu",
      "XFILESEARCHPATH": "/usr/dt/app-defaults/%L/Dt",
      "SESSIONTYPE": "gnome-session",
      "XMODIFIERS": "@im=ibus",
      "GIO_LAUNCHED_DESKTOP_FILE_PID": "6808",
      "JAVA_HOME": "/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java",
      "HOME": "/home/sro",
      "QT4_IM_MODULE": "xim",
      "GTK2_MODULES": "overlay-scrollbar",
      "XDG_SESSION_DESKTOP": "ubuntu",
      "GIO_LAUNCHED_DESKTOP_FILE": "/home/sro/.local/share/applications/jetbrains-pycharm.desktop",
      "XDG_RUNTIME_DIR": "/run/user/1000",
      "LC_IDENTIFICATION": "de_DE.UTF-8",
      "LC_ADDRESS": "de_DE.UTF-8",
      "SSH_AUTH_SOCK": "/run/user/1000/keyring/ssh",
      "GDMSESSION": "ubuntu",
      "IM_CONFIG_PHASE": "1",
      "UPSTART_JOB": "unity7",
      "UPSTART_SESSION": "unix:abstract=/com/ubuntu/upstart-session/1000/2441",
      "QT_ACCESSIBILITY": "1",
      "XDG_SEAT_PATH": "/org/freedesktop/DisplayManager/Seat0",
      "BASH_FUNC_generate_command_executed_sequence%%": "() {  printf '\\e\\7'\n}",
      "LESSOPEN": "| /usr/bin/lesspipe %s",
      "XDG_SESSION_ID": "c2",
      "DBUS_SESSION_BUS_ADDRESS": "unix:abstract=/tmp/dbus-VibE3DAiGP",
      "_": "/usr/bin/python",
      "DEFAULTS_PATH": "/usr/share/gconf/ubuntu.default.path",
      "GTK_IM_MODULE": "ibus",
      "DESKTOP_SESSION": "ubuntu",
      "GPG_AGENT_INFO": "/home/sro/.gnupg/S.gpg-agent:0:1",
      "LESSCLOSE": "/usr/bin/lesspipe %s %s",
      "GNOME_KEYRING_PID": "********",
      "XDG_SESSION_TYPE": "x11",
      "OLDPWD": "/home/sro/Desktop/final_eds/elastest-device-emulator-service",
      "LS_COLORS": "rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:",
      "GDM_LANG": "en_US",
      "LC_TELEPHONE": "de_DE.UTF-8",
      "GTK_MODULES": "gail:atk-bridge:unity-gtk-module",
      "SHLVL": "1",
      "PWD": "/home/sro/Desktop/final_eds/elastest-device-emulator-service/eds/rest_app",
      "JOB": "unity-settings-daemon",
      "LC_NAME": "de_DE.UTF-8",
      "LC_TIME": "de_DE.UTF-8",
      "XDG_CONFIG_DIRS": "/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg",
      "COMPIZ_BIN_PATH": "/usr/bin/",
      "XDG_DATA_DIRS": "/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop",
      "XDG_SEAT": "seat0"
    },
    "pid": 29006,
    "cwd": "/home/sro/Desktop/final_eds/elastest-device-emulator-service/eds/rest_app",
    "argv": [
      "resty.py"
    ],
    "user": "sro"
  },
  "config": {
    "JSON_AS_ASCII": true,
    "SESSION_COOKIE_PATH": null,
    "LOGGER_NAME": "__main__",
    "SECRET_KEY": "********",
    "APPLICATION_ROOT": null,
    "SERVER_NAME": null,
    "PREFERRED_URL_SCHEME": "http",
    "TESTING": false,
    "TEMPLATES_AUTO_RELOAD": null,
    "JSONIFY_MIMETYPE": "application/json",
    "SESSION_REFRESH_EACH_REQUEST": true,
    "TRAP_HTTP_EXCEPTIONS": false,
    "USE_X_SENDFILE": false,
    "SESSION_COOKIE_SECURE": false,
    "SESSION_COOKIE_DOMAIN": null,
    "SESSION_COOKIE_NAME": "session",
    "LOGGER_HANDLER_POLICY": "always",
    "DEBUG": false,
    "EXPLAIN_TEMPLATE_LOADING": false,
    "MAX_CONTENT_LENGTH": null,
    "JSONIFY_PRETTYPRINT_REGULAR": true,
    "PROPAGATE_EXCEPTIONS": null,
    "TRAP_BAD_REQUEST_ERRORS": false,
    "JSON_SORT_KEYS": "********",
    "SESSION_COOKIE_HTTPONLY": true,
    "PRESERVE_CONTEXT_ON_EXCEPTION": null
  },
  "os": {
    "platform": "linux2",
    "name": "posix",
    "uname": [
      "Linux",
      "sro-thinkpad",
      "4.4.0-79-generic",
      "#100-Ubuntu SMP Wed May 17 19:58:14 UTC 2017",
      "x86_64"
    ]
  },
  "application": {
    "maintainer": "ElasTest",
    "git_repo": "https://github.com/elastest/elastest-device-emulator-service"
  }
}

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

