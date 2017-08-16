import os
import sys
import json
spath = "../openmtc/lib/coap/coapy/coapy"
sys.path.append(os.path.abspath(spath))
from coap import connection
from coap import options
from coap import link
from coap import constants