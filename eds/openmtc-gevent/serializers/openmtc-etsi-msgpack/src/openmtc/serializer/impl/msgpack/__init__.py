from openmtc.serializer.DictSerializer import DictSerializer
from msgpack import dumps, loads, load
from openmtc.serializer import register_serializer


class MSGPackSerializer(DictSerializer):
    def __init__(self, *args, **kw):
        super(MSGPackSerializer, self).__init__(*args, **kw)

        self.dumps = self.pretty_dumps = dumps
        self.loads = loads
        self.load_file = load

register_serializer("application/x-msgpack", MSGPackSerializer)
register_serializer("application/msgpack", MSGPackSerializer)
