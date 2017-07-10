from openmtc_etsi.serializer import get_serializer
from base64 import b64decode


def decode_content(request_indication):
    resource = request_indication.resource
    try:
        resource = request_indication.resource = resource.read()
    except AttributeError:
        pass

    serializer = get_serializer(request_indication.content_type)
    # TODO: kca: properly handle encodings
    return serializer.decode_resource_values(resource)


def get_decoded_content(content):
    text_content = content.textContent
    if text_content is not None:
        return text_content
    return b64decode(content.binaryContent)
