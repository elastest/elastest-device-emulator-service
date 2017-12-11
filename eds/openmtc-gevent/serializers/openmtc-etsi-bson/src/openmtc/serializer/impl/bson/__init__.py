from openmtc.serializer.DictSerializer import DictSerializer
try:
    from bson import dumps, loads
except ImportError:
    from bson.json_util import dumps, loads
from openmtc.serializer import register_serializer


class BSONSerializer(DictSerializer):
    def __init__(self, *args, **kw):
        super(BSONSerializer, self).__init__(*args, **kw)

        self.dumps = self.pretty_dumps = dumps
        self.loads = loads

    load_file = DictSerializer.read_load

register_serializer("application/bson", BSONSerializer)
register_serializer("application/ubson", BSONSerializer)
register_serializer("application/x-bson", BSONSerializer)
