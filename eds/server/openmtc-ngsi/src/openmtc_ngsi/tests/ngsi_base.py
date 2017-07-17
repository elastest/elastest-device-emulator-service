import unittest
from openmtc.exc import SCLConflict
from openmtc_ngsi.ngsi import NGSI_9
from openmtc_ngsi.exc import NGSIError
from openmtc_ngsi.tests.xml import registerContextRequestXML
from openmtc_ngsi.requests import RegisterContextRequest
from openmtc_ngsi.ngsi_json import NGSIJSONWriter
from futile.StringIO import StringIO
from futile.logging import LoggerMixin
from subprocess import Popen
from os.path import expanduser
from time import sleep
from futile.net.http.client.RestClient import RestClient
from threading import Thread
from futile import NOT_SET
from futile.threading import Event
from openmtc_ngsi.xml import RequestParser, NGSIXMLWriter
from tempfile import mkdtemp
from shutil import rmtree
from os.path import dirname, abspath

SCL_PATH = dirname(abspath(__file__)) + "/../../../../gscl"

class TimeoutExpired(Exception):
    pass

class NotificationHandler(LoggerMixin):
    data = NOT_SET
    
    def __init__(self, num = 9, count = 1):
        self.event = Event()
        self.num = num
        self.count = count
    
    def __call__(self, num, data):
        if int(num) == self.num:
            self.count -= 1
            if self.count == 0:
                self.data = data
                self.event.set()
        
    def wait(self, timeout = 10):
        self.logger.debug("Waiting for notification")
        if not self.event.wait(timeout):
            self.logger.error("Timeout waiting for notification")
            raise TimeoutExpired("Timeout waiting for notification")
        self.logger.debug("Notification arrived.")       


class TestCaseBase(LoggerMixin, unittest.TestCase):
    scl_process = None
    mongo_process = None
    tempdir = None
    
    def setUp(self):
        super(TestCaseBase, self).setUp()
        
        self.tempdir = mkdtemp()
        try:
            self.mongo_process = self._start(["mongod", "--smallfiles", 
                        "--dbpath=" + self.tempdir, "--bind_ip=127.0.0.1", 
                        "--port=37017", "--quiet", "--nojournal"])
            try:
                self.scl_process = self._start([ expanduser(SCL_PATH), "--dbport=37017" ])
            except:
                self._kill(self.mongo_process)
                self.mongo_process = None
                raise
        except:
            rmtree(self.tempdir)
            self.tempdir = None
            raise
    
    def _start(self, cmd):
        process = Popen(cmd)
        sleep(5)
        
        rv = process.poll()
        if rv is not None:
            raise Exception("%s died with exit code %d." % (cmd, rv, ))
        
        return process
        
    def _kill(self, process):
        if process:
            try:
                process.terminate()
                process.wait()
            except:
                self.logger.excetion("Failed to terminate child process.")
        
    def tearDown(self):
        self._kill(self.scl_process)
        self._kill(self.mongo_process)
        self.scl_process = None
        self.mongo_process = None
        if self.tempdir:
            rmtree(self.tempdir)
            self.tempdir = None
        
class HTTPTestCaseBase(TestCaseBase):
    ngsi_uri = "http://localhost:5050"
    parser = RequestParser()
    writer  = NGSIXMLWriter()
    
    def setUp(self):
        super(HTTPTestCaseBase, self).setUp()
        
        self._start_flask()

        self.client = RestClient(self.ngsi_uri, content_type = "application/xml")
            
        
    def _start_flask(self):
        self.flask_thread = Thread(target = self._run_flask)
        self.flask_thread.start()     
        sleep(1)
        
    def _run_flask(self):
        import openmtc_ngsi.wsgi_flask
        openmtc_ngsi.wsgi_flask.reset()
        openmtc_ngsi.wsgi_flask.main()
                
    def tearDown(self):
        try:
            if self.flask_thread:
                import openmtc_ngsi.wsgi_flask
                openmtc_ngsi.wsgi_flask._server.shutdown()
                openmtc_ngsi.wsgi_flask._server.server_close()
                self.flask_thread.join(3)
                if self.flask_thread.isAlive():
                    raise Exception("Failed to stop flask")
                openmtc_ngsi.wsgi_flask._after_notify_hook = None
        finally:
            super(HTTPTestCaseBase, self).tearDown()
            
    def _send_request(self, path, data, name = None):
        if not isinstance(data, basestring):
            data = self.writer.serialize(data)
        name = name or self.ngsi_name
        path = name + path
        with self.client.post(path, data) as response:
            return self.parser.parse_request(response)
    
    def _register(self):
        return self._send_request("/registerContext", registerContextRequestXML, "/NGSI9")
        
    def _install_notification_handler(self, count = 1, handler = None):
        import openmtc_ngsi.wsgi_flask
        handler = handler or NotificationHandler(num = self.num, count = count)
        openmtc_ngsi.wsgi_flask._after_notify_hook = handler
        return handler
        

class NGSITestCaseBase(TestCaseBase):
    def __init__(self, *args, **kw):
        super(NGSITestCaseBase, self).__init__(*args, **kw)
        
        self._created = []

    def setUp(self):
        super(NGSITestCaseBase, self).setUp()
        #self.scl_process = Popen(expanduser(SCL_PATH))
        
        #self.scl_process.wait(10)
        
        #raise Exception(self.scl_process.returncode)
        
        from openmtc_ngsi.xml import RequestParser
        self.parser = RequestParser()
        self.ngsi9 = NGSI_9()
        self.json_serializer = NGSIJSONWriter()
    
    def tearDown(self):
#        self.scl_process.send_signal(SIGTERM)
#        self.scl_process.wait(15)
        for path in self._created:
            self.ngsi9.scl.delete(path)
            
        super(NGSITestCaseBase, self).tearDown()
    
    def _register(self):
        request = self.parser.parse_request(StringIO(registerContextRequestXML), RegisterContextRequest)
        response = self.ngsi9.registerContext(request)
        self._created.append(response._m2m_path)
        return response
        
    def _safe_register(self):
        try:
            self._register()
        except NGSIError as e:
            if not isinstance(e[0], SCLConflict):
                raise
            
    def _log_message_element(self, me):
        json = self.json_serializer.serialize(me, True)
        self.logger.info("%s: %s", type(me).__name__, json)
