from openmtc_etsi.model import LATEST_VERSION
from openmtc_server.exc import ConfigurationError


def prepare_config(config):
    try:
        global_config = config["global"]
    except KeyError:
        global_config = config["global"] = {}

    try:
        etsi_version = global_config["etsi_version"]
    except KeyError:
        etsi_version = global_config["etsi_version"] = LATEST_VERSION

    try:
        etsi_compatibility = global_config["etsi_compatibility"]
    except KeyError:
        global_config["etsi_compatibility"] = etsi_version
    else:
        if etsi_compatibility > etsi_version:
            raise ConfigurationError("'etsi_version' (%s) must be greater or "
                                     "equal to 'etsi_compatibility' (%s)" %
                                     (etsi_version, etsi_compatibility))

    global_config.setdefault("ignore_extra_attributes", False)

    return config
