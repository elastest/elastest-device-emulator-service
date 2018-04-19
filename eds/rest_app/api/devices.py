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


def post(name):
    count = len(devices)
    print(count)
    name['id'] = count + 1
    name['registered'] = datetime.datetime.now()
    devices[name['name']] = name
    return name, 201


def put(name):
    name = str(name)
    if devices.get(name) is None:
        return NoContent, 404
        devices[name] = name

    return devices[name]


def delete(name):
    name = str(name)
    if devices.get(name) is None:
        return NoContent, 404
    del devices[name]
    return NoContent, 204


def get(name):
    name = str(name)
    if devices.get(name) is None:
        return NoContent, 404

    return devices[name]


def search():
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
    return devices
