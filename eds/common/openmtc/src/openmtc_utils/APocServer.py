
if __name__ == "__main__":
    from futile.logging import get_logger, INFO, set_default_level
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

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

    class Handler(BaseHTTPRequestHandler):
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

            print("<end request>")

            self.send_response(status_code, response)
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
