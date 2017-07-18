#!/usr/bin/env python

from setuptools import setup
from distutils.core import setup
from glob import glob
import sys

from utils import (get_packages, OpenMTCSdist, OpenMTCBuildPy,
                   OpenMTCBuildPyBinary, OpenMTCSdistBinary,
                   create_openmtc_user, move_config_files, enable_init_files)


# name and version
SETUP_NAME = "openmtc-all"
SETUP_VERSION = "4.99.0"
SETUP_DESCRIPTION = "The OpenMTC NSCL and GSCL (GEvent version)"

# meta
SETUP_AUTHOR = "Konrad Campowsky"
SETUP_AUTHOR_EMAIL = "konrad.campowsky@fraunhofer.fokus.de"
SETUP_URL = "http://www.openmtc.org"
SETUP_LICENSE = "Fraunhofer FOKUS proprietary"

# requirements
SETUP_REQUIRES = [
    "urllib3", "gevent (>=1.0)", "iso8601 (>=0.1.5)", "werkzeug (>=0.9)",
    "blist", "simplejson", "ujson", "python_socketio", "gevent_websocket",
    "flask", "pyxb (==1.2.3)", "enum34", "dtls", "geventhttpclient"
    # server only
    "funcy", "netifaces", "decorator", "mimeparse"
]
SETUP_INSTALL_REQUIRES = [
    "urllib3", "gevent >= 1.0", "iso8601 >= 0.1.5", "werkzeug >= 0.9",
    "blist", "simplejson", "ujson", "python_socketio", "gevent_websocket",
    "flask", "pyxb == 1.2.3", "enum34", "dtls", "geventhttpclient",
    # server only
    "funcy", "netifaces", "decorator", "mimeparse"
]

# packages
PACKAGES = ["aplus", "coap", "openmtc", "openmtc_utils", "openmtc_etsi",
            "openmtc_onem2m", "futile", "openmtc_app", "openmtc_gevent",
            "openmtc.serializer.impl.bson", "openmtc.serializer.impl.msgpack",
            "openmtc_cse", "openmtc_scl", "openmtc_server"]
PACKAGE_DIR = {
    "": "common/openmtc/lib",
    "openmtc": "common/openmtc/src/openmtc",
    "openmtc_utils": "common/openmtc/src/openmtc_utils",
    "openmtc_etsi": "common/openmtc-etsi/src/openmtc_etsi",
    "openmtc_onem2m": "common/openmtc-onem2m/src/openmtc_onem2m",
    "futile": "futile/src/futile",
    "openmtc_app": "openmtc-app/src/openmtc_app",
    "openmtc_gevent": "openmtc-gevent/src/openmtc_gevent",
    "openmtc.serializer.impl.bson":
        "serializers/openmtc-etsi-bson/src/openmtc/serializer/impl/bson",
    "openmtc.serializer.impl.msgpack":
        "serializers/openmtc-etsi-msgpack/src/openmtc/serializer/impl/msgpack",
    "openmtc_onem2m.serializer.impl.xml":
        "serializers/openmtc-onem2m-xml/src/openmtc_onem2m/serializer/impl/xml",
    "openmtc_cse": "server/openmtc-cse/src/openmtc_cse",
    "openmtc_scl": "server/openmtc-scl/src/openmtc_scl",
    "openmtc_server": "server/openmtc-server/src/openmtc_server"
}
all_packages = []
EXCLUDE = ["plugins_eu_projects", "plugins_deprecated"]
for package in PACKAGES:
    all_packages.extend(get_packages(package, PACKAGE_DIR, EXCLUDE))

# scripts
SETUP_SCRIPTS = glob("openmtc-gevent/bin/*")

# package data
PACKAGE_DATA = {}

# data files
DB_DIR = "/var/lib/openmtc"
LOG_DIR = "/var/log/openmtc"
LOG_ROTATE_DIR = "/etc/logrotate.d"
LOG_ROTATE_FILES = ("openmtc-gevent/etc/logrotate.d/openmtc",)
INIT_DIR = "/etc/init.d"
INIT_DIST_FILES = ("openmtc-gevent/etc/init.d/openmtc-gscl",
                   "openmtc-gevent/etc/init.d/openmtc-nscl")
CONFIG_FILES = ("config-nscl.json", "config-gscl.json")
CONFIG_DIR = "/etc/openmtc/gevent"
CONFIG_DIST_FILES = ("openmtc-gevent/etc/conf/config-nscl.json.dist",
                     "openmtc-gevent/etc/conf/config-gscl.json.dist")
DATA_FILES = [
    (DB_DIR, ""),
    (LOG_DIR, ""),
    (LOG_ROTATE_DIR, LOG_ROTATE_FILES),
    (INIT_DIR, INIT_DIST_FILES),
    (CONFIG_DIR, CONFIG_DIST_FILES),
]

# handle binary only
binary_only = "--binary-only" in sys.argv
if binary_only:
    sys.argv.remove("--binary-only")
    CMD_CLASS = {'build_py': OpenMTCBuildPyBinary, 'sdist': OpenMTCSdistBinary}
else:
    CMD_CLASS = {'build_py': OpenMTCBuildPy, 'sdist': OpenMTCSdist}

if __name__ == "__main__":
    ############################################################################
    # setup
    setup(name=SETUP_NAME,
          version=SETUP_VERSION,
          description=SETUP_DESCRIPTION,
          author=SETUP_AUTHOR,
          author_email=SETUP_AUTHOR_EMAIL,
          url=SETUP_URL,
          license=SETUP_LICENSE,
          requires=SETUP_REQUIRES,
          install_requires=SETUP_INSTALL_REQUIRES,
          package_dir=PACKAGE_DIR,
          packages=all_packages,
          scripts=SETUP_SCRIPTS,
          package_data=PACKAGE_DATA,
          data_files=DATA_FILES,
          cmdclass=CMD_CLASS,
          py_modules=["pyio"]
          )

    ############################################################################
    # install
    if "install" in sys.argv:
        # only do this during install
        enable_init_files(INIT_DIR, INIT_DIST_FILES)

        move_config_files(CONFIG_DIR, CONFIG_FILES)

        create_openmtc_user(DB_DIR, LOG_DIR)
