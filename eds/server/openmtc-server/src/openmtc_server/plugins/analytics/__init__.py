from base64 import b64decode
from json import dumps, loads

from geventhttpclient.client import HTTPClient
import re

from openmtc_server.Plugin import Plugin
from openmtc_onem2m.model import Container as Con, ContentInstance as Cin, \
    EncodingType
from openmtc_etsi.model import Container, ContentInstance


class Analytics(Plugin):
    def __init__(self, api, config, *args, **kw):
        super(Analytics, self).__init__(api=api, config=config, *args, **kw)

        self._mongo_http = {
            'host': config.get('host', '192.168.149.59'),
            'port': config.get('port', 3000),
            'method': config.get('method', 'POST'),
            'path': config.get('path', '/store/measurement'),
            'headers': config.get('headers', {
                'content-type': 'application/json'
            })
        }

        self.__rest = HTTPClient(self._mongo_http['host'],
                                 self._mongo_http['port'],
                                 connection_timeout=120.0,
                                 concurrency=50,
                                 ssl=False)

        self.fmt_json_regex = re.compile(r'application/([\w]+\+)?json')

    def _init(self):
        # resource created
        self.events.resource_created.register_handler(
            self._handle_con_created, Con)
        self.events.resource_created.register_handler(
            self._handle_cin_created, Cin)
        self.events.resource_created.register_handler(
            self._handle_container_created, Container)
        self.events.resource_created.register_handler(
            self._handle_content_instance_created, ContentInstance)

        self._initialized()

    def _handle_con_created(self, con, req):
        pass

    def _handle_cin_created(self, cin, req):
        self.send_to_mongo_http(cin)

    def _handle_container_created(self, con, req):
        pass

    def _handle_content_instance_created(self, cin, req):
        pass

    def send_to_mongo_http(self, cin):
        response = None
        try:
            if "sensor_data" in cin.path:
                if hasattr(cin, 'contentInfo'):
                    fmt, encoding_type = cin.contentInfo.split(':')
                    if not re.search(self.fmt_json_regex, fmt):
                        # TODO(rst): handle non json data
                        return
                    if int(encoding_type) == EncodingType.plain.value:
                        data = cin.content
                    else:
                        try:
                            data = b64decode(cin.content)
                        except Exception as e:
                            self.logger.error("Error decoding content:" + str(e))
                else:
                    data = b64decode(cin.content)
                response = self.__rest.request(self._mongo_http['method'],
                                               self._mongo_http['path'], data,
                                               self._mongo_http['headers'])
        except Exception as e:
            self.logger.debug(e)
        else:
            if response is not None:
                response.release()
