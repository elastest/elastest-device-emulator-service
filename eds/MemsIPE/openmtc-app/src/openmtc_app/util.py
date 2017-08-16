from base64 import decodestring as b64_decodes
from json import loads as json_loads, load as json_load
from operator import getitem
from threading import Thread
import sys
import futile

from openmtc.exc import OpenMTCError


def go(target, args):
    """ Starts target function in a seperate thread.
        NOTE: based on threading.Thread.

        @param target: function which the thread should execute
        @param args: (sequence of) arguments for target
        @return: pointer to the thread object
    """
    thread = Thread(target=target, args=args)
    thread.start()
    return thread


def decode_json_content(content):
    """ Decodes the value of content["$t"] as base64 JSON.
        NOTE: content["contentType"] should be "application/json".

        @param content: dict containing $t base64 JSON
        @return: decoded JSON object
    """
    if ("contentType" in content and
            not content["contentType"] == "application/json"):
        # TODO non JSON case
        raise OpenMTCError("NOT IMPLEMENTED")
    temp = content["$t"]
    temp = b64_decodes(temp)
    temp = json_loads(temp)

    return temp


def prepare_app(parser, loader, name, default_config_file):
    parser.add_argument("-v", "--verbose", action="count", default=None,
                        help="Increase verbosity in output. This option can be"
                             " specified multiple times.")
    args = parser.parse_args()

    module = loader.fullname.split("." + name).pop(0)

    futile.logging.set_default_level(futile.logging.DEBUG)
    logger = futile.logging.get_logger(name)

    config_locations = (".", "/etc/openmtc/" + module)

    try:
        import os.path
        for d in config_locations:
            config_file = os.path.join(os.path.abspath(d),
                                       default_config_file)
            logger.debug("Trying config file location: %s", config_file)
            if os.path.isfile(config_file):
                break
        else:
            raise Exception("Configuration file %s not found in any of these "
                            "locations: %s" % default_config_file,
                            config_locations)
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(2)

    try:
        with open(config_file) as f:
            logger.info("Reading configuration file %s.", config_file)
            config = json_load(f)
    except IOError as e:
        logger.warning("Failed to read configuration file %s: %s",
                       config_file, e)
        config = {}
    except Exception as e:
        logger.critical("Error reading configuration file %s: %s",
                        config_file, e)
        sys.exit(2)

    if "logging" in config:  # TODO init logging
        log_conf = config["logging"]
        if args.verbose is None:
            futile.logging.set_default_level(log_conf.get("level") or
                                             futile.logging.WARNING)
        elif args.verbose >= 2:
            futile.logging.set_default_level(futile.logging.DEBUG)
        else:
            futile.logging.set_default_level(futile.logging.INFO)
        logfile = log_conf.get("file")
        if logfile:
            futile.logging.add_log_file(logfile)
    else:
        futile.logging.set_default_level(futile.logging.DEBUG)

    return args, config


def get_value(name, value_type, default_value, args, config):
    try:
        value = (getattr(args, name.replace(".", "_"), None) or
                 reduce(getitem, name.split("."), config))
    except KeyError:
        value = None
    value = value if isinstance(value, value_type) else default_value
    return value
