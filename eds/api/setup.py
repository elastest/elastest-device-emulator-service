# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "api"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="ElasTest Device Emulator service(EDS)",
    author_email="rowshan@tu-berlin.de",
    url="",
    keywords=["Swagger", "ElasTest Device Emulator service(EDS)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    Emulators for the sensor, actuator and smart devices behaviors
    """
)

