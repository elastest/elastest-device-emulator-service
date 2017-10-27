import sys
import os
if 'threading' in sys.modules and not os.environ.get('SUPPORT_GEVENT'):
    raise Exception('threading module loaded before monkey patching!')
os.environ.setdefault("GEVENT_RESOLVER", "thread")
import gevent.monkey
gevent.monkey.patch_all()

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from openmtc_app.util import prepare_app, get_value
from openmtc_app.flask_runner import SimpleFlaskRunner as Runner
from .zig_bee_ipe import ZigBeeIPE

# defaults
default_name = "ZigBeeIPE"
default_ep = "http://frontend:8000"
default_device = "/dev/ttyACM0"

# args parser
parser = ArgumentParser(
    description="An IPE for ZigBee devices connected to a XBee USB adapter",
    prog="ZigBeeGip",
    formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--name", help="Name used for the AE.")
parser.add_argument("-s", "--ep", help="URL of the local Endpoint.")
parser.add_argument("-d", "--usb-device", help="Device Node of the XBee.")

# args, config and logging
args, config = prepare_app(parser, __loader__, __name__, "config.json")

# variables
nm = get_value("name", (unicode, str), default_name, args, config)
cb = config.get("cse_base", "onem2m")
ep = get_value("ep", (unicode, str), default_ep, args, config)
host = config.get("host", "auto")
port = int(config.get("port"))
device = get_value('usb_device', (unicode, str), default_device, args, config)
s = config.get("sim", False)
p = int(config.get("sim_period"))

# start
app = ZigBeeIPE(usb_device=device, sim=s, sim_period=p,
                name=nm, cse_base=cb)
Runner(app, host=host, port=port).run(ep)

print ("Exiting....")
