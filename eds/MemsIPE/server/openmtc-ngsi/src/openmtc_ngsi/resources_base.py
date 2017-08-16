from flask.helpers import make_response

from flask.ext.restful import Resource, Api

from openmtc_ngsi.xml import NGSIXMLParser, NGSIXMLWriter

_xml_writer = NGSIXMLWriter()


class NGSIConvenienceApi(Api):
    def __init__(self, *args, **kw):
        # kw["default_mediatype"] = "application/xml"
        super(NGSIConvenienceApi, self).__init__(*args, **kw)

    def mediatypes(self):
        return ["application/xml"]


api = NGSIConvenienceApi()


@api.representation("application/xml")
def output_xml(data, code, headers=None):
    dumped = _xml_writer.serialize(data)
    resp = make_response(dumped, code)
    if headers is not None:
        resp.headers.extend(headers)
    return resp


class NGSIResource(Resource):
    parser = NGSIXMLParser()

    def dispatch_request(self, *args, **kwargs):
        import openmtc_ngsi.wsgi_flask
        self.ngsi9 = openmtc_ngsi.wsgi_flask.ngsi9
        self.ngsi10 = openmtc_ngsi.wsgi_flask.ngsi10
        return super(NGSIResource, self).dispatch_request(*args, **kwargs)
