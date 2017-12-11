from openmtc_app.util import prepare_app, get_value
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from openmtc_app.flask_runner import FlaskRunner as Runner

from .front_end import FrontEnd

# defaults
default_name = 'FrontEnd'
default_ep = 'http://localhost:6000'

# args parser
parser = ArgumentParser(
    description="App for EDS frontend that subscribes to contains and displays "
                "sensor data on web page",
    prog="FrontEnd",
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

# start
app = FrontEnd(name=nm, cse_base=cb)
Runner(app, host=host, port=port).run(ep)

print ("Exiting....")
