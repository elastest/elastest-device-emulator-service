import datetime
import devices
from connexion import NoContent

#devices = {}




def get(id, device):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = device

    return devices[id]


def search():
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
    return list(devices.values())
