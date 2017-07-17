#! /usr/bin/env python

# Coap Client example
# Called with coapurl.sh
import sys
from urlparse import urlparse
from argparse import ArgumentParser

from coap import CoapClient
from coap.coapy.coapy import constants
from futile.logging import get_logger, DEBUG, INFO, WARNING


VALID_HEADERS = ['accept', 'content-format']

# if debug is necessary
# import logging
# logging.basicConfig(level=logging.DEBUG)

logger = get_logger("coapurl")

description = "A simple CoAP command line client inspired by curl."

parser = ArgumentParser(description=description, add_help=True)

parser.add_argument("--version", action='version')
parser.add_argument("-X", "--request",
                    choices=("GET", "POST", "PUT", "DELETE"),
                    help="Specify request command to use.")
parser.add_argument("-d", "--data", help="CoAP POST data")
parser.add_argument("-H", "--header", action="append",
                    help="Custom header to pass to server.")
parser.add_argument("--host",
                    help="Use this as host instead of parsing it from the uri.")
parser.add_argument("-v", "--verbose", action="count", default=0,
                    help="Increase verbosity in output. This option can be "
                         "specified multiple times.")
parser.add_argument("-i", action='store_true')
parser.add_argument("uri")

args = parser.parse_args()

if args.verbose >= 2:
    logger.setLevel(DEBUG)
    if args.verbose >= 3:
        import futile.logging

        futile.logging.set_default_level(DEBUG)
elif args.verbose == 1:
    logger.setLevel(INFO)
else:
    logger.setLevel(WARNING)

try:
    uri = args.uri
    if "://" not in uri:
        uri = "coap://" + uri
    info = urlparse(uri)
    if info.scheme and info.scheme not in ("coap", "coaps"):
        raise ValueError("Unhandled URI scheme: %s" % (info.scheme, ))
    if not info.netloc:
        raise ValueError("No host specified")
    path = info.path.split("/", 1)[-1] or ""
    if info.query:
        path += "?%s" % (info.query, )
    uri = "coap://%s" % (info.netloc, )
except Exception as e:
    logger.error("Malformed URI: %s", e)
    sys.exit(2)

client = CoapClient(uri)

_TransactionTypeMap = {0: 'CON',
                       1: 'NON',
                       2: 'ACK',
                       3: 'RST'}

_transaction_type_str = lambda t: '%s (%s)' % (_TransactionTypeMap[t], t)

_CodeMap = {}

_code_str = lambda c: '%s (%s)' % (_CodeMap[c], c)

_code_list = [
    '2.01 Created',
    '2.02 Deleted',
    '2.03 Valid',
    '2.04 Changed',
    '2.05 Content',
    '4.00 Bad Request',
    '4.01 Unauthorized',
    '4.02 Bad Option',
    '4.03 Forbidden',
    '4.04 Not Found',
    '4.05 Method Not Allowed',
    '4.06 Not Acceptable',
    '4.12 Precondition Failed',
    '4.13 Request Entity Too Large',
    '4.15 Unsupported Content-Format',
    '5.00 Internal Server Error',
    '5.01 Not Implemented',
    '5.02 Bad Gateway',
    '5.03 Service Unavailable',
    '5.04 Gateway Timeout',
    '5.05 Proxying Not Supported'
]


def fill_code_map():
    for x in _code_list:
        code = int(x[0]) * 32 + int(x[2:4])
        _CodeMap[code] = x

fill_code_map()

if args.request:
    method = args.request
elif args.data:
    method = "POST"
else:
    method = "GET"

payload = args.data

try:
    kw = {}
    if args.host:
        if '//' in args.host:
            host_url = urlparse(args.host)
        else:
            host_url = urlparse('//' + args.host)
        kw["uri_host"] = host_url.hostname
        if host_url.port:
            kw["uri_port"] = host_url.port
    if args.header:
        for header in args.header:
            if isinstance(header, str):
                header_split = header.split(':')
                header_key = header_split[0].strip()
                if header_key.lower() in VALID_HEADERS:
                    header_value = header_split[1].strip()
                    if header_key.lower() == 'content-format':
                        header_key = 'content_type'
                    else:
                        header_key = header_key.replace('-', '_')
                    kw[header_key] = header_value
                else:
                    print('header %s not accepted' % header_key.lower())
    response = client.request(method, path, payload, **kw).get()

    def handle_success():
        if args.i:
            print('Version: ' + str(response.version))
            print('Type: ' + _transaction_type_str(response.transaction_type))
            print('Token Length: ' + str(len(response.token)))
            print('Code: ' + _code_str(response.code))
            # print('Message ID (decimal): ' + str())
            print('Token: ' + str(response.token.encode('hex')))

            if len(response.options):
                for option in response.options:
                    print(str(option))

            print('')

        print(response.payload)

    def handle_error():
        print(constants.codes[response.code])

    if response.code > 100:
        handle_error()
    else:
        handle_success()

except Exception as e:
    print(e)
    sys.exit(1)


