from coap.coapy.coapy import options
from openmtc_onem2m.exc import CSESyntaxError
from gevent.server import DatagramServer

if __name__ == "__main__":
    from futile.logging import get_logger, INFO, set_default_level
    from json import loads, dumps
    from base64 import b64decode
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    from openmtc_etsi.serializer import get_serializer as get_etsi_serializer
    from openmtc_onem2m.serializer import \
        get_serializer as get_onem2m_serializer

    USE_IPV6 = True

    set_default_level(INFO)
    logger = get_logger(__name__, INFO)

    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--port", type=int, default=8888,
                        help="port to run on")

    # parser.add_argument("-v", "--verbose", action="count", default=None,
    #                help="Increase verbosity in output. This option can be
    # specified multiple times.")
    args = parser.parse_args()

    def print_data(data, i=None):
        print "<representation%s>" % (i is not None and " " + str(i) or "",)
        try:
            data = b64decode(data)
        except ValueError:
            print "<Can't decode representation, not base64? printing raw>"
            print data
        else:
            print "<Base64 decoded data>"
            print data
            print "<End Base64 decoded data>"
            try:
                data = dumps(loads(data), indent=2)
            except (TypeError, ValueError):
                print "<No JSON could be decoded>"
            else:
                print "<pretty printed JSON>"
                print data
                print "<end pretty printed JSON>"

        print "<end representation%s>" % (i is not None and " " + str(i) or "",)

    class Handler(object):
        @staticmethod
        def handle_etsi_single_notification(data):
            data = data["representation"]["$t"]
            print_data(data)

            print("<EOF>")
            response = "OK"
            return 204, response

        @staticmethod
        def handle_etsi_aggregated_notification(data):
            print("<Received notifyCollection>")
            notify_responses = []
            for i, notify in enumerate(data["notify"]):
                data = notify["representation"]["$t"]
                print_data(data, i + 1)

            print("<EOF>")
            notify_response = {"targetID": "XXX", "primitiveType": "YYY",
                               "statusCode": "ZZZ"}
            notify_responses.append(notify_response)

            response = {
            "notifyCollectionResponse": {"notifyResponse": notify_responses}}
            return 204, response

        @staticmethod
        def handle_onem2m_single_notification(data):
            response = "OK"
            data = data["singleNotification"]
            if data.get("verificationRequest", False):
                # TODO(rst): check creator for notify permission
                return 204, "verified"

            return 204, response

        def handle_onem2m_aggregated_notification(self, data):
            response = "OK"
            return 204, response

        def process(self, msg):
            print("Request received:")
            print(msg.code, msg.uri)
            print

            data = msg.payload
            if not data:
                print("<no content>")
            else:
                print("<Raw data>")
                print(data)
                print("<EOF>")
                ct = msg.content_type
                if ct:
                    ct = ct.split(";", 1)[0]
                try:
                    model, data = (get_onem2m_serializer(ct)
                                   .decode_resource_values(data))
                except CSESyntaxError:
                    model, data = (get_etsi_serializer(ct)
                                   .decode_resource_values(data))
                except Exception as e:
                    logger.exception("Error decoding data")
                    print("<failed to decode data: %r>" % (e, ))
                    return
                if "notifyCollection" == model:
                    status_code, response = self.handle_etsi_aggregated_notification(data)
                elif "notify" == model:
                    status_code, response = self.handle_etsi_single_notification(data)
                elif "singleNotification" in data:
                    status_code, response = self.handle_onem2m_single_notification(data)
                elif "aggregatedNotification" in data:
                    status_code, response = self.handle_onem2m_aggregated_notification(data)
                else:
                    print("Don't understand notification")

            print("<end request>")

    print "Listening on port", args.port

    from coap import connection, constants

    _block1_pending_payload = {}

    def _handle_block1(block1, rx_record, remote, msg):
        """Handles the presence of the Block1 Option.

        Block1 informs the server that the payload of a client request is
        fragmented.
        This function aggregates the various fragments, and queries the client
        for the next fragment.

        :param block1: Block1 option Object
        :param rx_record: CoAP message transfer information
        :param remote: tuple(Client IP, Client PORT)
        :param msg: CoAP message
        :return: Completed payload or None if the payload is not complete
        """
        try:
            _block1_pending_payload[remote] += msg.payload
        except (KeyError, TypeError):
            if block1.block_number != 0:
                # We discard fragments with block number > 0 if we haven't
                # received the first one yet
                return None
            _block1_pending_payload[remote] = msg.payload

        if block1.more:
            msg = connection.Message(connection.Message.ACK,
                                     code=constants.CONTINUE)
            msg.addOption(block1)
            server.sendto(msg._pack(rx_record.transaction_id,
                                         rx_record.message.token), remote)
            return None
        payload = _block1_pending_payload[remote]
        _block1_pending_payload[remote] = None
        return payload

    def handle_request(message, remote):
        """Entry points of requests, converts a buffer into CoAP message
        transfer information

        :param message: Buffer containing a CoAP message
        :param remote: tuple(Client IP, Client Port)
        """

        rx_record = connection.ReceptionRecord(None, message, remote)

        block1 = rx_record.message.findOption(options.Block1)
        if block1:
            block_payload = _handle_block1(block1, rx_record, remote,
                                           rx_record.message)
            if not rx_record.message or not block_payload:
                return
            rx_record.message.payload = block_payload

        Handler().process(rx_record.message)

        response_msg = connection.Message(
            connection.Message.ACK,
            code=constants.VALID
        )

        if block1:
            response_msg.addOption(block1)
        server.sendto(response_msg._pack(rx_record.transaction_id,
                                         rx_record.message.token),
                           remote)

    address = USE_IPV6 and "::" or ""
    server = DatagramServer((address, args.port), handle_request)

    server.serve_forever()
    print("Exiting")
