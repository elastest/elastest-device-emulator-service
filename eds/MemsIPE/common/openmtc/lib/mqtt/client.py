#!/usr/bin/env python

import paho.mqtt.client as mqtt
from urlparse import urlparse


class Client:
    """
    A simple test client for the oneM2M/MQTT protocol binding
    """
    __portmap = {
        'mqtt':         1883,
        'mqtts':        8883,
        'secure-mqtt':  8883,
    }

    def __init__(self, url, client_id, subscribe=False, verbosity=0):
        """
        :param urlparse.ParseResult url:
        :param string client_id:
        :param integer verbosity:
        """
        if url.scheme not in self.__portmap:
            raise NotImplementedError(
                '%s is not a supported protocol; scheme must be one of %s'
                % (
                    url.scheme,
                    ''.join(self.__portmap.keys()),
                )
            )

        def on_log(client, userdata, level, buf):
            if level <= verbosity:
                print '>>', buf

        def on_disconnect(client, userdata, rc):
            """
            :param mqtt.Client client:
            :param All userdata:
            :param int rc:
            :return void:
            """
            if not rc == mqtt.MQTT_ERR_SUCCESS:
                print '!! Involuntary connection loss - %s (code %d)' % (mqtt.error_string(rc), rc)

        def on_connect(client, userdata, rc):
            """
            :param mqtt.Client client:
            :param All userdata:
            :param integer rc:
            :return void:
            """
            topics = [
                (self._build_topic(receiver=self._client_id), 1),
            ]

            if subscribe:
                topics += [
                    (self._build_topic(originator=self._client_id, type='resp'), 1),
                    ('$SYS/#', 1),
                ]

            self._client.subscribe(topics)

        def on_message(client, userdata, message):
            """
            :param mqtt.Client client:
            :param All userdata:
            :param  mqtt.MQTTMessage message:
            :return void:
            """
            print '<< message received on topic', message.topic
            print str(message.payload)

        self._client_id = client_id
        self._client = mqtt.Client(
            clean_session=False,
            client_id=''.join([
                'C' if client_id[0].lower() in ['c', 'm'] else 'A',
                '::',
                client_id.replace('/', ':'),
            ]),
        )

        self._client.on_log = on_log
        self._client.on_disconnect = on_disconnect
        self._client.on_connect = on_connect
        self._client.on_message = on_message

        self._client.connect(
            url.hostname,
            url.port or self.__portmap[url.scheme],
        )

    def __enter__(self):
        self._client.loop_start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.loop_stop()
        self._client._clean_session = True
        self._client.reconnect()
        self._client.disconnect()

    def publish(self, target, data):
        """
        :param string target:
        :param string data:
        :return:
        """
        def message_callback(client, userdata, message):
            print '<<', message.payload

        self._client.message_callback_add(
            self._build_topic(self._client_id, target, type='resp'),
            message_callback,
        )
        self._client.publish(
            self._build_topic(self._client_id, target),
            data,
            1,
        )

    @staticmethod
    def _build_topic(originator='+', receiver='+', type='req'):
        """
        Helper function to create topic strings

        :param string originator:
        :param string receiver:
        :param string type:
        :return string:
        """
        return ''.join([
            '/oneM2M/',
            type,
            '/',
            originator,
            '/',
            receiver
        ]).rstrip('/')

if __name__ == '__main__':
    from argparse import ArgumentParser
    from time import sleep

    parser = ArgumentParser(
        description='A simple MQTT/oneM2M client',
        add_help=True,
    )
    parser.add_argument('url')
    parser.add_argument('--version', action='version', version='1.0')
    parser.add_argument('--client-id', type=str, help='Sets the client_id', default='cse-0')
    parser.add_argument('--publish', '-P', type=str)
    parser.add_argument('--subscribe', '-S', action='store_true')
    parser.add_argument('-v', '--verbose', action="count")

    args = parser.parse_args()
    if not (args.publish or args.subscribe):
        parser.error('At least one of --subscribe or --publish is required')

    url = urlparse(args.url)

    print "== Waiting for messages. Hit <Ctrl>+[C] to exit."
    with Client(url, args.client_id, args.subscribe, args.verbose) as client:
        if args.publish:
            client.publish(url.path.split('/')[-1], args.publish)

        try:
            while True:
                sleep(0.1)
        except KeyboardInterrupt:
            pass
