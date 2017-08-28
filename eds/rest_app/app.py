#!/usr/bin/env python3
from swagger_server.encoder import FlaskJSONEncoder

import connexion
#from .encoder import FlaskJSONEncoder
import os
from connexion import NoContent
import flask
import signal
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
    app.app.json_encoder = FlaskJSONEncoder
    app.add_api('swagger.yaml')
    app.run(port=8080)