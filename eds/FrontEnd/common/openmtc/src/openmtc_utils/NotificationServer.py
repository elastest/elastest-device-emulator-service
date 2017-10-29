from openmtc_etsi.exc import SCLValueError
from openmtc_onem2m.exc import CSESyntaxError

if __name__ == "__main__":
    from futile.logging import get_logger, INFO, set_default_level
    from json import loads, dumps
    from base64 import b64decode
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    from openmtc_etsi.serializer import get_serializer as get_etsi_serializer
    from openmtc_onem2m.serializer import \
        get_serializer as get_onem2m_serializer

    USE_IPV6 = True

    set_default_level(INFO)
    logger = get_logger(__name__, INFO)

    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--port", type=int, default=9999,
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

    class Handler(BaseHTTPRequestHandler):
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

            response = {"notifyCollectionResponse": {
                "notifyResponse": notify_responses}}
            return 204, response

        @staticmethod
        def handle_onem2m_notification(data):
            response = "OK"
            data = data["notificationEvent"]["representation"]
            if data.get("verificationRequest", False):
                # TODO(rst): check creator for notify permission
                return 204, "verified"
            print(data)

            return 204, response

        @staticmethod
        def handle_onem2m_aggregated_notification(data):
            response = "OK"
            return 204, response

        def do_GET(self):
            print("Request received:")
            print(self.requestline)
            print(self.headers)
            print
            status_code = 204
            response = "OK"
            try:
                l = int(self.headers["Content-Length"])
            except KeyError:
                print("<no content>")
            else:
                data = self.rfile.read(l)
                print("<Raw data>")
                print(data)
                print("<EOF>")
                ct = self.headers.get("Content-Type")
                if ct:
                    ct = ct.split(";", 1)[0]
                try:
                    model, data = (get_onem2m_serializer(ct)
                                   .decode_resource_values(data))
                except CSESyntaxError:
                    try:
                        model, data = (get_etsi_serializer(ct)
                                       .decode_resource_values(data))
                    except SCLValueError as e:
                        logger.exception("Error decoding data")
                        print("<failed to decode data: %r>" % (e, ))
                        return
                except Exception as e:
                    logger.exception("Error decoding data")
                    print("<failed to decode data: %r>" % (e, ))
                    return
                if "notifyCollection" == model:
                    status_code, response = self.handle_etsi_aggregated_notification(data)
                elif "notify" == model:
                    status_code, response = self.handle_etsi_single_notification(data)
                elif "notificationEvent" in data:
                    status_code, response = self.handle_onem2m_notification(data)
                elif "aggregatedNotification" in data:
                    status_code, response = self.handle_onem2m_aggregated_notification(data)
                else:
                    print("Don't understand notification")

            print("<end request>")

            self.send_response(status_code, response)
            self.send_header("X-M2M-RSC", 2000)
            self.end_headers()

        do_POST = do_PUT = do_DELETE = do_GET

    print "Listening on port", args.port

    if USE_IPV6:
        from socket import AF_INET6

        class HTTPServerV6(HTTPServer):
            address_family = AF_INET6

        server_address = ('::', args.port)
        httpd = HTTPServerV6(server_address, Handler)
    else:
        server_address = ('', args.port)
        httpd = HTTPServer(server_address, Handler)

    try:
        httpd.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        pass

    print("Exiting")
