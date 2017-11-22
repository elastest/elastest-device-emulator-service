from urlparse import urlparse
from aplus import Promise
from socket import error as SocketError
from openmtc_server.plugins import TransportPlugin
from openmtc_server.transportdomain import (
    Request,
    RequestMethod,
    Response,
    ErrorResponse,
)
from openmtc.exc import ConnectionFailed
from openmtc_onem2m.serializer import OneM2MJsonSerializer, get_serializer
from openmtc_onem2m.model import OperationE
from openmtc_server.configuration import (
    Configuration,
    ListOption,
    SimpleOption,
    BooleanOption,
)
import paho.mqtt.client as mqtt
import simplejson as json
from simplejson.scanner import JSONDecodeError

__author__ = 'sho <stephan.hohmann@fokus.fraunhofer.de>'


class ConnectorConfiguration(Configuration):
    __name__ = 'Connector configuration'
    __options__ = {
        'interface':    SimpleOption(default=''),
        'host':         SimpleOption(default=None),
        'port':         SimpleOption(int),
        'is_wan':       BooleanOption(default=None),
    }


class MQTTTransportPluginGatewayConfiguration(Configuration):
    __name__ = 'MQTTTransportPluginGatewayConfiguration configuration'
    __options__ = {
        'connectors': ListOption(
            ConnectorConfiguration,
            default=(
                ConnectorConfiguration(port=5000, is_wan=False),
                ConnectorConfiguration(port=4000, is_wan=True)
            ),
        ),
    }


class MQTTTransportPluginBackendConfiguration(Configuration):
    __name__ = 'MQTTTransportPluginBackendConfiguration configuration'
    __options__ = {
        'connectors': ListOption(
            ConnectorConfiguration,
            default=(
                ConnectorConfiguration(port=15000, is_wan=False),
                ConnectorConfiguration(port=14000, is_wan=True)
            ),
        ),
    }


class MQTTTransportPlugin(TransportPlugin):
    """
    This class provides for a transport over the MQTT protocol as described in TS 0010
    """
    MQTT_QOS_LEVEL = 1

    __portmap = {
        'mqtt':         1883,
        'mqtts':        8883,
        # The correct (i.e. registered with IANA) servicename for SSL/TLS-wrapped MQTT is 'secure-mqtt' in an effort
        # to prevent confusion with MQTT-S/N. But as the entire world seems to insist on using 'mqtts' (including
        # TS 0010, sec. 6.6) ... We are supporting both names here for maximum compliance and robustness.
        'secure-mqtt':  8883,
    }

    __request_field_map = {
        'op':   'method',
        'to':   'path',
        'fr':   'originator',
        'rqi':  'id',
        'pc':   'payload',
    }

    __response_field_map = {
        'rsc':  'status_code',
        'rqi':  'id',
        'pc':   'payload',
        # 'to':   '',
        # 'fr':   '',
    }

    def __init__(self, api, config, *args, **kw):
        super(MQTTTransportPlugin, self).__init__(api, config, *args, **kw)
        self._clients = {}
        self._serializer = OneM2MJsonSerializer()

    def _init(self):
        self.api.register_client(tuple(self.__portmap.keys()), self.send_request)
        self._initialized()

    @staticmethod
    def attach(client):
        """
        Static wrapper function to attach callback handlers to a given client.

        Functions attached in this manner are expected to have the same name as the handler they seek to implement.
        :param mqtt.Client client:
        :return fun:
        """
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                func(self, *args, **kwargs)
            setattr(client, func.__name__, func)
            return wrapper
        return decorator

    @staticmethod
    def _build_topic(originator='+', receiver='+', type='req'):
        """
        Helper function to create topic strings

        :param string originator:
        :param string receiver:
        :param string type:
        :return string:
        """
        def mask(id):
            return id.lstrip('/').replace('/', ':')
        return ''.join([
            '/oneM2M/',
            type,
            '/',
            mask(originator),
            '/',
            mask(receiver),
        ])

    def _serialize(self, data):
        """
        :param All data:
        :return string:
        """
        return self._serializer.dumps(data)

    def _deserialize(self, string):
        """
        :param string string:
        :return All:
        """
        return self._serializer.loads(string)

    def _get_client(self, parsed_url, client_id):
        """
        :param urlparse.ParseResult parsed_url:
        :param string client_id:
        :return mqtt.Client:
        """
        port = parsed_url.port or self.__portmap[parsed_url.scheme]
        key = (parsed_url.hostname, port, client_id)

        try:
            return self._clients[key]
        except KeyError:
            client = mqtt.Client(
                clean_session=False,
                client_id=''.join([
                    'C' if client_id[0].lower() in ['c', 'm'] else 'A',
                    '::',
                    client_id.replace('/', ':'),
                ]),
            )

            @self.attach(client)
            def on_connect(client, userdata, rc):
                """
                :param mqtt.Client client:
                :param All userdata:
                :param integer rc:
                :return void:
                """
                def message_callback(client, userdata, message):
                    """
                    Catch requests and

                    :param mqtt.Client client:
                    :param All userdata:
                    :param mqtt.MQTTMessage message:
                    :return void:
                    """
                    def send_response(status_code=2000, id=0, payload=None, to=None, _from=None):
                        """
                        :param dict response:
                        :return:
                        """
                        payload = {
                            'rsc': status_code,
                            'rqi': id,
                            'pc': payload,
                            'fr': _from,
                            'to': to,
                        }.copy()

                        client.publish(
                            self._build_topic(message.topic.split('/')[-2], client_id, type='resp'),
                            self._serialize({
                                k: v for k, v in payload.items() if v is not None
                            }),
                            self.MQTT_QOS_LEVEL
                        )

                    try:
                        message = self._deserialize(message.payload)
                    except JSONDecodeError as e:
                        self.logger.error('Got request with damaged payload: %s' % (e.message, ))
                        send_response(status_code=4000)
                        return

                    try:
                        message['op'] = RequestMethod[OperationE.__dict__['_member_names_'][message['op'] - 1].lower()]
                        request_params = {
                            self.__request_field_map[k]: v for k, v in message.items()
                            if k in self.__request_field_map and v is not None
                        }
                        response = self.api.handle_request(Request(**request_params))
                    except KeyError:
                        send_response(status_code=4005)
                        return
                    except ErrorResponse:
                        send_response(status_code=5000)
                        return

                    send_response(
                        status_code=response.status_code,
                        id=response.id,
                        payload=response.payload or None,
                        _from=client_id
                    )

                topic = self._build_topic(receiver=client_id)
                client.subscribe([
                    (
                        topic,
                        self.MQTT_QOS_LEVEL,
                    ),
                    (
                        self._build_topic(originator=client_id, type='resp'),
                        self.MQTT_QOS_LEVEL,
                    ),
                ])
                client.message_callback_add(topic, message_callback)

            @self.attach(client)
            def on_disconnect(client, userdata, rc):
                """
                :param mqtt.Client client:
                :param All userdata:
                :param int rc:
                :return void:
                """
                if not rc == mqtt.MQTT_ERR_SUCCESS:
                    self.logger.error(
                        'Involuntary connection loss - %s (code %d)'
                        % (mqtt.error_string(rc), rc)
                    )

            @self.attach(client)
            def on_message(client, userdata, message):
                """
                :param mqtt.Client client:
                :param All userdata:
                :param  mqtt.MQTTMessage message:
                :return void:
                """
                self.logger.debug('message received on topic ' + message.topic)

            @self.attach(client)
            def on_log(client, userdata, level, buf):
                """
                :param mqtt.Client client:
                :param All userdata:
                :param integer level:
                :param string buf:
                :return void:
                """
                self.logger.debug('pahomqtt-%d: %s' % (level, buf))

            try:
                client.connect(parsed_url.hostname, port)
            except SocketError as e:
                raise ConnectionFailed(e.message)

            self._clients[key] = client
            client.loop_start()
            return client

    def send_request(self, request):
        """
        :param openmtc_server.transportdomain.Request request:
        :return Promise:
        """
        p = Promise()
        parsed_url = urlparse(request.path)
        target_id = parsed_url.path.split('/')[-1]

        client_id = request.originator.split('/')[-1] if request.originator else \
            'cse-0'  # TODO: make this configurable

        client = self._get_client(parsed_url, client_id)
        topic = self._build_topic(client_id, target_id, 'resp')

        def message_callback(client, userdata, message):
            """
            One-time function to catch and process responses to our request.
            Unsubscribes from the topic gracefully.
            :param mqtt.Client client:
            :param All userdata:
            :param mqtt.MQTTMessage message:
            :return void:
            """
            client.message_callback_remove(topic)
            try:
                message = json.loads(message.payload)
            except JSONDecodeError as e:
                self.logger.error('Got response with damaged payload: ' + e.message)
                p.reject(e)

            response = {
                self.__response_field_map[k]: v for k, v in message.items()
                if k in self.__response_field_map and v is not None
            }
            p.fulfill(Response(**response))

        payload = {
            'op': OperationE[request.method.name.capitalize()],
            'to': request.path,
            'fr': request.originator or client_id,
            'rqi': request.id,
            'pc': request.payload,
        }.copy()

        client.publish(
            self._build_topic(client_id, target_id),
            get_serializer(request.content_type).dumps({
                k: v for k, v in payload.items() if v is not None
            }),
            self.MQTT_QOS_LEVEL
        )

        client.message_callback_add(topic, message_callback)

        return p

    def _stop(self):
        for client in self._clients.values():
            client.loop_stop()
            # TODO: this is abominable. But for the time being, there seems to be no elegant solution to this.
            client._clean_session = True
            # TS 0010, sec. 6.3 mandates a reconnect in order to leave a clean state with the MQTT broker
            client.reconnect()
            client.disconnect()
        super(MQTTTransportPlugin, self)._stop()
