from openmtc_server.configuration import Configuration, SimpleOption,\
    LowerCaseEnumOption, BooleanOption, ConnectorSpecConfiguration, ListOption
from openmtc_etsi.model import SCLType


class MIDConfiguration(Configuration):
    __name__ = "mId configuration"
    __options__ = {"enabled": BooleanOption(default=True),
                   "connectors": ListOption(ConnectorSpecConfiguration,
                                            default=(ConnectorSpecConfiguration(is_wan=True),))}


class DIAConfiguration(Configuration):
    __name__ = "dIa configuration"
    __options__ = {"enabled": BooleanOption(default=True),
                   "connectors": ListOption(ConnectorSpecConfiguration,
                                            default=(ConnectorSpecConfiguration(is_wan=False),))}


class MIAConfiguration(Configuration):
    __name__ = "mIa configuration"
    __options__ = {"enabled": BooleanOption(default=True),
                   "connectors": ListOption(ConnectorSpecConfiguration,
                                            default=(ConnectorSpecConfiguration(is_wan=False),))}


class ETSIConfiguration(Configuration):
    __name__ = "etsi configuration"
    __options__ = {"scl_base": SimpleOption(str, default="m2m"),
                   "default_content_type": SimpleOption(str,
                                                        default="application/json"),
                   "scl_type": LowerCaseEnumOption(SCLType),
                   "dIa": SimpleOption(DIAConfiguration,
                                       default=None),
                   "mIa": SimpleOption(MIAConfiguration,
                                       default=None),
                   "mId": SimpleOption(MIDConfiguration,
                                       default=None)}
