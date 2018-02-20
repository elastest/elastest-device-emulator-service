import datetime

from connexion import NoContent
import call

devices = {}
URL_BASE = 'http://172.18.0.5:8080/eds/devices'
def get():
    #id = str(id)
    if call is None:
        return NoContent, 404
    print "this is 0",call
    #return call

def post(device):
    count = len(devices)
    name = str(name)
    #device['id'] = count + 1
    device['registered'] = datetime.datetime.now()
    devices[device['name']] = device
    return device, 201


def put(id, device):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = device

    return devices[id]


def delete(id):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    del devices[id]
    return NoContent, 204


# def get(id, device):
#     id = str(id)
#     if devices.get(id) is None:
#         return NoContent, 404
#     devices[id] = device
#
#     return devices[id]


def search():
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
   # return list(devices.values())
  return devices.values()
