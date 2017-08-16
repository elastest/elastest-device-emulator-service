import pkgutil
import spec
import futile.logging
from futile.logging import get_logger, DEBUG
from futile.net.http.client.RestClient import RestClient
from importlib import import_module
import sys
from openmtc_etsi.serializer.xml import XMLSerializer
from pprint import pprint
from traceback import print_stack

SCL_URI = "http://localhost:4000"

client = RestClient(SCL_URI, content_type="application/xml",
                    headers={"Accept": "application/xml"})

futile.logging.set_default_level(DEBUG)

logger = get_logger(__name__, DEBUG)

serializer = XMLSerializer()


specs = []

for importer, modname, ispkg in pkgutil.iter_modules(spec.__path__):
    specs.append(modname)

specs.sort()


def test(mod):
    try:
        if not do_test(mod):
            print "Test failed"
            return False
    except AttributeError as e:
        print "Test module", mod, "does not declare", e
    except Exception as e:
        logger.exception("huhu")
        print_stack()
        print "Test failed: ", e
    else:
        return True


def prune_dict(d):
    ignore_attrs = ("expirationTime", )
    d = d.values()[0]
    for k in d:
        if k in ignore_attrs:
            d[k] = None


def compare_response(want, have):
    want = want.strip()

    want_dict = serializer.load_string(want)
    have_dict = serializer.load(have)

    prune_dict(want_dict)
    prune_dict(have_dict)

    if want_dict != have_dict:
        print "Response does not match expectation:"
        print "want:"
        pprint(want_dict)
        print "==============="
        print "have:"
        pprint(have_dict)
        return False

    return True


def do_test(mod):
    method = mod.method
    path = mod.path
    want = mod.response
    data = None if method in ("DELETE", "GET") else mod.request.strip()
    response = client.request(method, path, data)
    if not compare_response(want, response):
        return False
    return True


for spec in specs:
    fullmodname = __package__ + ".spec." + spec
    print "Testing: ", fullmodname
    module = import_module(fullmodname)
    if not test(module):
        print "Failed."
        sys.exit(1)
    print "OK."
