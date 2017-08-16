from collections import namedtuple
from openmtc.model import StrEnum


class ETSIEndpointType(StrEnum):
    mId = "mId"
    mIa = "mIa"
    dIa = "dIa"


class ETSIEndpoint(namedtuple("ETSIEndpointBase",
                              ("reference_point", "base_uri"))):
    """
    def __new__(self, reference_point, base_uri):
        if reference_point not in (None, "mId", "mIa", "dIa"):
            raise ValueError("Invalid reference point: %s" %
                             (reference_point, ))

        return namedtuple.__new__(self, reference_point=reference_point,
                                  base_uri=base_uri)
    """

    def internal(self):
        return self.reference_point is None

    @property
    def is_mId(self):
        return self.reference_point == ETSIEndpointType.mId
