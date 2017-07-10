##########################
Installing the OpenMTC SDK
##########################

Requirements
============

For developing applications with the OpenMTC Python SDK, a Python interpreter is obviously required. Only version 2.7 of the python language is supported. Note that currently, only the CPython implementation (the default interpreter) of Python has been tested. PyPy might work as well, possibly with some minor adjustments. Jython is known not to work since it lacks support for compiled extensions.

Additionally, the following Python packages must be installed:

* gevent (>=1.0)
* python_socketio
* werkzeug (>=0.9)
* flask (>=0.10)
* gevent_websocket
* urllib3
* iso8601
* decorator

It is higly recommended to install these packages through the `pip` tool and *not* via the operating system's package manager.

Note that for installing the ``gevent`` package, development headers for both `python` and `libev` as well as a C compiler and associated toolchain might be required. To install these along with the `pip` tool the following commands might be used:

* Debian based systems (including Ubuntu):
    ``$ apt-get install python-pip libev-dev python-dev gcc make automake``
* Redhat based systems (including Fedora, Centos):
    ``$ yum install python-pip libev-devel python-devel gcc make automake``

Afterwards, the follwing command line should suffice to install the required Python packages:

.. code-block:: sh

  $ pip install gevent python_socketio werkzeug flask gevent_websocket urllib3 iso8601 decorator

Recommended Software
--------------------

For any testing and experimenting, it is highly recommended to use the `ipython` interactive Python shell.

Installing
==========

To install the OpenMTC Python SDK itself the following steps need to be performed:

Change to the SDK's distribution directory:

.. code-block:: sh

    $ cd openmtc-app

Run the installer command:

.. code-block:: sh

    $ sudo python setup.py install

Testing the Installation
========================

The following command can be used to test if the OpenMTC Python SDK has been correctly installed:

.. code-block:: sh

    $ python -c "import openmtc; import openmtc_app"

If the SDK has been installed correctly, this command will exit succesfully (exit code ``0``) and not produce any output.


