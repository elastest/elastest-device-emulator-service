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
from flask import Flask, jsonify
from base64 import b64decode
import requests
from requests.auth import HTTPDigestAuth
import json



if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')
    app.app.json_encoder = FlaskJSONEncoder
    app.add_api('swagger.yaml')
    app.run(port=8080)


    @app.route('/eds/MemsIPE/', methods=['GET'])
    def get_memsdata():
        url = "http://localhost:8000/onem2m/MemsIPE/sensor_data/x/"

        mems_data = requests.get(url)
        print ( str(mems_data.status_code))
        print (mems_data.text)

        return json.dumps(mems_data.text)
        print (mems_data)