from signal import SIGTERM, SIGINT

from flask import (Flask, request, abort, redirect, url_for,
                   Response as FlaskResponse)

from gevent import signal as gevent_signal
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from socketio import Server as SioServer, Middleware as SioMiddleware

from futile.net.http.exc import HTTPError
from openmtc_app.runner import AppRunner


class Response(FlaskResponse):
    pass


class SimpleFlaskRunner(AppRunner):
    def __init__(self, m2m_app, host=None, port=None, listen_on="0.0.0.0",
                 *args, **kw):
        super(SimpleFlaskRunner, self).__init__(m2m_app=m2m_app, *args, **kw)

        self.host = host or "auto"
        self.port = port or 5050
        self.listen_on = listen_on
        self.flask_app = Flask(type(self.m2m_app).__module__)

    def _set_auto_host(self):
        try:
            import socket
            from urlparse import urlparse
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            netloc = urlparse(self.m2m_ep).netloc.split(':')
            s.connect((netloc[0], int(netloc[1])))
            self.host = s.getsockname()[0]
            s.close()
        except:
            self.host = "127.0.0.1"

    def _get_server(self):
        return WSGIServer((self.listen_on, self.port), self.flask_app)

    def _run(self):
        if self.host == "auto":
            self._set_auto_host()

        self.base_uri = "http://%s:%s" % (self.host, self.port)
        self.m2m_app.run(self, self.m2m_ep)

        _server = self._get_server()
        self.logger.debug("Serving on %s:%s", self.listen_on, self.port)
        gevent_signal(SIGTERM, _server.stop)
        gevent_signal(SIGINT, _server.stop)
        _server.serve_forever()

    def add_route(self, route, handler, methods=("POST", "GET")):
        def wrapper():
            try:
                return handler(request)
            except HTTPError as e:
                self.logger.exception("Aborting")
                abort(e.status)

        self.logger.debug("Adding route: %s -> %s" % (route, handler))
        self.flask_app.add_url_rule(route, view_func=wrapper,
                                    endpoint=route + str(handler),
                                    methods=methods)


class FlaskRunner(SimpleFlaskRunner):
    def __init__(self, m2m_app, host="127.0.0.1", port=None,
                 listen_on="0.0.0.0", *args, **kw):
        super(FlaskRunner, self).__init__(m2m_app=m2m_app, host=host, port=port,
                                          listen_on=listen_on, *args, **kw)

        @self.flask_app.route("/")
        def home():
            return redirect(url_for('static', filename='motor.html'))

        self.sio_app = SioServer(async_mode='gevent')

        @self.sio_app.on('connect')
        def connect(sid, environ):
            self.logger.debug('client connected: %s' % sid)

    def _get_server(self):
        return WSGIServer((self.listen_on, self.port),
                          SioMiddleware(self.sio_app, self.flask_app),
                          handler_class=WebSocketHandler)

    def emit(self, event, message=None, sid=None):
        self.sio_app.emit(event, message, room=sid)

    def get_handler_decorator(self, name):
        return self.sio_app.on(name)

    def add_message_handler(self, name, handler, client=False, response=False):

        def wrapper(*args, **kw):
            if not client:
                args = args[1:]
            if response:
                return handler(*args, **kw)
            else:
                handler(*args, **kw)

        self.sio_app.on(name, wrapper)
