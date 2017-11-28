import datetime

from connexion import NoContent

devices = {}

@app.route('eds/devices')
def post(device):
    count = len(devices)
    device['id'] = count + 1
    device['registered'] = datetime.datetime.now()
    devices[device['id']] = device
    return device, 201

@app.route('eds/devices')
def put(id, device):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = device

    return json.dumps(devices[id])

@app.route('eds/devices')
def delete(id):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    del devices[id]
    return NoContent, 204

@app.route('eds/devices')
def get(id, device):
    id = str(id)
    if devices.get(id) is None:
        return NoContent, 404
    devices[id] = device

    return devices[id]


def search():
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
    return list(devices.values())
