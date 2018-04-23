import datetime
import requests
from flask import Flask, render_template, flash, request
import simplejson
from base64 import b64decode
from connexion import NoContent
import itertools


url1 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/x/latest/"
url2 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/y/latest/"
url3 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/z/latest/"

url = {url1, url2, url3}

res = [requests.get(i) for i in url]
d = [j.content for j in res]

dic = [simplejson.loads(q) for q in d]
#print dic
raw_data = [m["m2m:cin"]["con"] for m in dic]
registered = [k["m2m:cin"]["ct"] for k in dic]
data = [de.encode("utf-8") for de in raw_data]

convert =[b64decode(pa) for pa in data]
a = {}
b = {}
c = {}

a = convert[0]
b = convert[1]
c = convert[2]

devices = {}

app = Flask(__name__)

devices['registered'] = datetime.datetime.now()
devices['servicename'] ='' #'MemsIPE'  #request.form['servicename']
mems = {}
axis = {}

axis['x']= c
axis['y']= b
axis['z']= a


mems['id']= next(itertools.count(100))
mems['axis']= axis
devices['mems']= mems


def post(servicename):
    count = len(devices)
    print(count)
    servicename['id'] = count + 1
    servicename['registered'] = datetime.datetime.now()
    devices[servicename['id']] = servicename
    return servicename, 201


def put(id, servicename):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = servicename

    return devices[id]


def delete(id):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    del devices[id]
    return NoContent, 204


def get(id, servicename):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = servicename
    return devices[id]

def search():
    return devices
