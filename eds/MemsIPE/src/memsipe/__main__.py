from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from openmtc_app.util import prepare_app, get_value
from openmtc_app.flask_runner import SimpleFlaskRunner as Runner
from .mems_ipe import MemsIPE
import os
# defaults
default_name = "MemsIPE"
default_ep = "http://frontend:8000"

# args parser
parser = ArgumentParser(
    description="An IPE called MemsIPE",
    prog="MemsIPE",
    formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--name", help="Name used for the AE.")
parser.add_argument("-s", "--ep", help="URL of the local Endpoint.")

# args, config and logging
args, config = prepare_app(parser, __loader__, __name__, "config.json")

# variables
nm = get_value("name", (unicode, str), default_name, args, config)
cb = config.get("cse_base", "onem2m")
ep = get_value("ep", (unicode, str), default_ep, args, config)
host = config.get("host", "auto")
port = int(config.get("port"))

is_simulation = True
interval = 10

# start
app = MemsIPE(name=nm, cse_base=cb, is_simulation=is_simulation, interval=interval)
Runner(app, host=host, port=port).run(ep)

print ("Exiting....")
