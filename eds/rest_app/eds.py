#!/usr/bin/env python
import logging
import os
import requests
import signal
import flask
import connexion
from connexion.resolver import RestyResolver
import urllib
from healthcheck import HealthCheck, EnvironmentDump
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from adapters import log
import call

LOG = log.get_logger(name=__name__)




def add_check_api():
    app = flask.Flask('check_api')
    health = HealthCheck(app, "/healthcheck")
    envdump = EnvironmentDump(app, "/environment")

    def health_check():


        def onem2m_url_ok():
            url= 'http://localhost:8000/onem2m'
            r = requests.response(url)
            return r.status_code == 200


        def mems_url_ok():
            url = 'http://localhost:8000/onem2m/MemsIPE'
            r = requests.response(url)
            return r.status_code == 200


        #maintenance = False
        if 1 + 1 == 2 and onem2m_url_ok and mems_url_ok:
            return {'status', 'up'}
            #elif url_ok:
            #    return {'status', 'up'}
            #elif not maintenance:
            #   return {'status', 'out_of_service'}
        else:
            return {'status', 'down'}

    def application_data():
        return {'maintainer': 'ElasTest',
                'git_repo': 'https://github.com/elastest/elastest-device-emulator-service'}

    health.add_check(health_check)
    envdump.add_section("application", application_data)

    return app


def shutdown_handler(signum=None, frame=None):
    LOG.info('Shutting down...')
    IOLoop.instance().stop()

if __name__ == '__main__':
    eds_app = connexion.FlaskApp(__name__)
    eds_app.add_api('api1.yaml',
                arguments={'title': 'ElasTest Device Emulator API'},
                resolver=RestyResolver('api'))

    eds_ip = os.environ.get('EDS_IP', '0.0.0.0')
    eds_port = os.environ.get('EDS_PORT', 8080)
    eds_server = HTTPServer(WSGIContainer(eds_app))
    eds_server.listen(address=eds_ip, port=eds_port)
    LOG.info('ESM available at http://{IP}:{PORT}'.format(IP=eds_ip, PORT=eds_port))

    check_ip = os.environ.get('EDS_CHECK_IP', '0.0.0.0')
    check_port = os.environ.get('EDS_CHECK_PORT', 9090)
    check_server = HTTPServer(WSGIContainer(add_check_api()))
    check_server.listen(address=check_ip, port=check_port)
    LOG.info('ESM Health available at http://{IP}:{PORT}'.format(IP=check_ip, PORT=check_port))

    for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
        signal.signal(sig, shutdown_handler)

    LOG.info('Press CTRL+C to quit.')
    IOLoop.instance().start()

    eds_app.route('/eds/devices')
    def get():
        return call

    # app.run(port=9090)
    #add_check_api().run(host= '0.0.0.0', port=8080)
