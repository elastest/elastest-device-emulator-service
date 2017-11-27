#!/usr/bin/env python

import connexion
from connexion.resolver import RestyResolver
from flask import Flask

import signal

from healthcheck import HealthCheck, EnvironmentDump
import os
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop

from threading import Thread

import logging

logging.basicConfig(level=logging.INFO)


def add_check_api():
    app = Flask(__name__)
    health = HealthCheck(app, "/healthcheck")
    envdump = EnvironmentDump(app, "/environment")

    def health_check():

        # TODO check that the datasource backend is working
        # TODO check that the active resource backends are available
        url_ok = True
        maintenance = False
        if 1 + 1 == 2:
            return {'status', 'up'}
        elif url_ok:
            return {'status', 'up'}
        elif not maintenance:
            return {'status', 'out_of_service'}
        else:
            return {'status', 'down'}

    def application_data():
        return {'maintainer': 'ElasTest',
                'git_repo': 'https://github.com/elastest/elastest-device-emulator-service'}

    health.add_check(health_check)
    envdump.add_section("application", application_data)

    return app


def create_api():
    app = connexion.FlaskApp(__name__, port=9090)
    eds_app = app.add_api('api.yaml',
                          arguments={'title': 'ElasTest Device Emulator API'},
                          resolver=RestyResolver('api'))

    return eds_app

def shutdown_handler(signum=None, frame=None):
  #  LOG.info('Shutting down...')
    IOLoop.instance().stop()


if __name__ == '__main__':
    #app = connexion.App(__name__)
    #app.add_api('api.yaml',
     #                     arguments={'title': 'ElasTest Device Emulator API'},
      #                    resolver=RestyResolver('api'))
    app = create_api

    check_app = add_check_api()
    eds_port = os.environ.get('EDS_PORT', 8080)
    eds_server = HTTPServer(WSGIContainer(app))
    eds_server.listen(address='0.0.0.0', port=eds_port)
	#
    check_port = os.environ.get('EDS_CHECK_PORT', 9090)
    check_server = HTTPServer(WSGIContainer(check_app))
    check_server.listen(address='0.0.0.0', port=check_port)

    for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
        signal.signal(sig, shutdown_handler)

    IOLoop.instance().start()
    # app.run(host='0.0.0.0', port=8080)
    #  sleep 5
   # check_app.run(host='0.0.0.0', port=9090)
