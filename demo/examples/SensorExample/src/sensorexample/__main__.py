from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from openmtc_app.util import prepare_app, get_value
from openmtc_app.runner import AppRunner as Runner
from .sensor_example import SensorExample

# defaults
default_name = "SensorExample"
default_ep = "http://localhost:8000"

# args parser
parser = ArgumentParser(
    description="An IPE called SensorExample",
    prog="SensorExample",
    formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--name", help="Name used for the AE.")
parser.add_argument("-s", "--ep", help="URL of the local Endpoint.")

# args, config and logging
args, config = prepare_app(parser, __loader__, __name__, "config.json")

# variables
nm = get_value("name", (unicode, str), default_name, args, config)
cb = config.get("cse_base", "onem2m")
ep = get_value("ep", (unicode, str), default_ep, args, config)
poas = config.get("poas", ["http://auto:24545"])
originator_pre = config.get("originator_pre", "//openmtc.org/mn-cse-1")
ssl_certs = config.get("ssl_certs", {})

# start
app = SensorExample(
    name=nm, cse_base=cb, poas=poas,
    originator_pre=originator_pre, **ssl_certs
)
Runner(app).run(ep)

print ("Exiting....")
