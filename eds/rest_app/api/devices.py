import datetime
import requests
import json
#import connexion
from base64 import b64decode
from connexion import NoContent
import logging
import itertools


url1 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/x/latest/"
url2 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/y/latest/"
url3 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/z/latest/"

url = {url1, url2, url3}

res = [requests.get(i) for i in url]
d = [j.content for j in res]
dic = [json.loads(q) for q in d]
raw_data = [m["m2m:cin"]["con"] for m in dic]
regis = [k["m2m:cin"]["ct"] for k in dic]
registered = str(regis[0])
data = [de.encode("utf-8") for de in raw_data]

convert =[b64decode(pa) for pa in data]
a = {}
b = {}
c = {}

a = convert[0]
b = convert[1]
c = convert[2]

devices = {}



mems = {}
axis = {}

axis['x']= c
axis['y']= b
axis['z']= a


mems['id']= next(itertools.count(100))
mems['axis']= axis
devices['mems']= mems
devices['registered'] = registered
devices['servicename'] = 'MemsIPE' #'MemsIPE'  #request.form['servicename']

print devices

def get_all(servicename=None):
    return [device for device in devices.values() if not servicename or device['servicename'] == servicename]


def put(id, servicename):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = servicename

    return devices[id]


def delete(id):
    if id in devices:
        logging.info('Deleting device %s..', id)
        del devices[id]
        return NoContent, 204
    else:
        return NoContent, 404

def get(id):
    device = devices.get(id)
    return device or ('Not found', 404)

def search():
    return devices
