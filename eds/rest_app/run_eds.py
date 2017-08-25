# -*- coding: utf-8 -*-
# Copyright © 2017-2019 Zuercher Hochschule fuer Angewandte Wissenschaften.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import signal
import connexion
import flask
import os
from healthcheck import HealthCheck, EnvironmentDump
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

#import logging
import adapters.log
from eds_api.encoder import JSONEncoder

#LOG = logging.basicConfig(level=logging.INFO)
LOG = adapters.log.get_logger(name=__name__)

def add_check_api():
    app = flask.Flask('check_api')
    health = HealthCheck(app, "/healthcheck")
    envdump = EnvironmentDump(app, "/environment")

    def health_check():

        # check that the DB is working
        # check that the active backends are available
        if 1 + 1 == 2:
            return True, "addition works"
        else:
            return False, "the universe is broken"

    def application_data():
        return {'maintainer': 'ElasTest',
                'git_repo': 'https://github.com/elastest/elastest-device-emulator-service'}

    health.add_check(health_check)
    envdump.add_section("application", application_data)

    return app


def create_api():
    eds_app = connexion.App('eds_api', specification_dir='./swagger/')
    eds_app.app.json_encoder = JSONEncoder
    eds_app.add_api(
        'swagger.yaml', strict_validation=True,
        arguments={'title': 'Emulators for the sensor, actuator and smart devices behaviors'
                   }
    )
    LOG.info('OSBA API and ElasTest extensions API created.')
    return eds_app


def shutdown_handler(signum=None, frame=None):
    LOG.info('Shutting down...')
    IOLoop.instance().stop()


if __name__ == '__main__':
    eds_app = create_api()
    check_app = add_check_api()

    eds_port = os.environ.get('EDS_PORT', 8080)
    eds_server = HTTPServer(WSGIContainer(eds_app))
    eds_server.listen(address='0.0.0.0', port=eds_port)
    LOG.info('EDS available at http://{IP}:{PORT}'.format(IP='0.0.0.0', PORT=eds_port))

    check_port = os.environ.get('EDS_CHECK_PORT', 5000)
    check_server = HTTPServer(WSGIContainer(check_app))
    check_server.listen(address='0.0.0.0', port=check_port)
    LOG.info('EDS Health available at http://{IP}:{PORT}'.format(IP='0.0.0.0', PORT=check_port))

    for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
       signal.signal(sig, shutdown_handler)

    LOG.info('Press CTRL+C to quit.')
    IOLoop.instance().start()