import datetime
import requests
import json
from base64 import b64decode
from connexion import NoContent

raw_data = requests.get("http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/x/latest/")
array = raw_data.content
print array
final_data = json.loads(array)
print final_data
devices = b64decode(final_data["m2m:cin"]["con"])
print devices

#devices= final_data


def post(servicename):
    count = len(devices)
    print(count)
    servicename['id'] = count + 1
    servicename['registered'] = datetime.datetime.now()
    devices[servicename['device']] = servicename
    return servicename, 201


def put(id, servicename):
    id = str(id)
    if devices.get(servicename) is None:
        return NoContent, 404
        devices[servicename] = servicename

    return devices[servicename]


def delete(servicename):
    id = str(id)
    if devices.get(servicename) is None:
        return NoContent, 404
    del devices[servicename]
    return NoContent, 204


def get(id,servicename):
    id = str(id)
    if devices.get(servicename) is None:
        return NoContent, 404

    return devices[servicename]


def search():
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
    return devices
