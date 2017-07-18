__author__ = 'ren-local'

from socketio import socketio_manage
from openmtc_scl.plugins.transport_gevent_socketio.namespaces import GlobalNamespace


class Application(object):
    """This simple Application only sets up GlobalNamespace.
    """
    def __init__(self):
        self.buffer = []
        # Dummy request object to maintain state between Namespace
        # initialization.
        self.request = {}

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].strip('/')

        print "path: %s" % (path, )

        # browser access
        if not path:
            start_response('200 OK', [('Content-Type', 'text/html')])
            return ['<h1>Socket.IO runs here! </h1>']

        self.request["start_response"] = start_response

        # socket.io access
        if path.startswith("socket.io"):

            # set GlobalNamespace on root ('/')
            socketio_manage(environ, {
                '': GlobalNamespace
            }, self.request)

        else:
            return self.not_found(start_response)

    @staticmethod
    def not_found(start_response):
        start_response('404 Not Found', [])
        return ['<h1>Not Found</h1>']