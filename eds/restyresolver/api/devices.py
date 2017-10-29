import datetime
#import zigbees
#import mems

from connexion import NoContent

devices = {}


def post(device):
    count = len(devices)
    device['id'] = count + 1
    device['registered'] = datetime.datetime.now()
    devices[device['id']] = device
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


def get(id):
    id = int(id)
    if devices.get(id) is None:
        return NoContent, 404

    return devices[id]


def search():
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
    return list(devices.values())
