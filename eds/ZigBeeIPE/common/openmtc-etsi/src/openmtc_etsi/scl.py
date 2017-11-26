"""
Created on 01.06.2013

@author: kca
"""

from futile.logging import LoggerMixin
from openmtc.model import StrEnum


class RequestIndicationMethod(StrEnum):
    retrieve = "retrieve"
    create = "create"
    delete = "delete"
    update = "update"
    notify = "notify"


class RequestIndication(LoggerMixin):
    internal = False
    aPoc_path = None

    def __init__(self, path, retarget=None, requestingEntity=None,
                 correlationID=None, rcat=0, trpdt=0, contactURI=None,
                 via=None, *args, **kw):
        super(RequestIndication, self).__init__(*args, **kw)

        self.path = path
        self.retarget = retarget
        self.requestingEntity = requestingEntity
        self.correlationID = correlationID
        self.rcat = rcat
        self.trpdt = trpdt
        self.contactURI = contactURI
        self.via = via or []

    # TODO: kca: write or find a "deprecated" decorator and use it here
    @property
    def type(self):
        return self.method

    @property
    def targetID(self):
        return self.path

    def __str__(self):
        return "RequestIndication: %s" % str(self.as_dict())

    def as_dict(self):
        return {
            "path": self.path,
            "method": self.method,
            "retarget": self.retarget,
            "requestingEntity": self.requestingEntity,
            "correlationID": self.correlationID,
            "rcat": self.rcat,
            "trpdt": self.trpdt,
            "contactURI": self.contactURI,
            "via": self.via,
        }


class RetrieveRequestIndication(RequestIndication):
    method = RequestIndicationMethod.retrieve

    def __init__(self, path, retarget=None, filterCriteria=None,
                 searchPrefix=None, maxSize=None, *args, **kw):
        super(RetrieveRequestIndication, self).__init__(path=path,
                                                        retarget=retarget,
                                                        *args, **kw)
        self.filterCriteria = filterCriteria
        self.searchPrefix = searchPrefix
        self.maxSize = maxSize

    def as_dict(self):
        d = super(RetrieveRequestIndication, self).as_dict()
        d.update({
            "filterCriteria": self.filterCriteria,
            "searchPrefix": self.searchPrefix,
            "maxSize": self.maxSize
        })
        return d


class DeleteRequestIndication(RequestIndication):
    method = RequestIndicationMethod.delete

    def __init__(self, path, retarget=None, requestingEntity=None,
                 correlationID=None, reason=None, *args, **kw):
        super(DeleteRequestIndication,
              self).__init__(path=path, retarget=retarget,
                             requestingEntity=requestingEntity,
                             correlationID=correlationID, *args, **kw)

        # TODO: internal use only. Move into openmtc_scl package
        assert reason in (None, "cascading", "expired", "read_access_lost")
        self.reason = reason

    @property
    def cascading(self):
        return self.reason == "cascading"

    @property
    def expired(self):
        return self.reason == "expired"

    @property
    def read_access_lost(self):
        return self.reason == "read_access_lost"

    def as_dict(self):
        return dict(super(DeleteRequestIndication, self).as_dict().items() +
                    {
                        "reason": self.reason
                    }.items())


class ResourceRequestIndication(RequestIndication):
    content_type = None

    def __init__(self, path, resource, content_type=None, typename=None, *args,
                 **kw):
        super(ResourceRequestIndication, self).__init__(path=path, *args, **kw)

        try:
            self.resource = resource.values
            self.typename = resource.typename
        except AttributeError:
            if not (bool(typename) ^ bool(content_type)):
                raise ValueError("Must specify exactly one of content_type (%s)"
                                 " or typename (%s)" % (content_type, typename))
            if typename:
                self.logger.warning("Specifying typename is deprecated")
            else:
                self.content_type = content_type
            self.typename = typename

            # when partial addressing sub resource can be a string
            self.resource = resource

    def as_dict(self):
        return dict(super(ResourceRequestIndication, self).as_dict().items() + {
            "resource": self.resource,
            "typename": self.typename,
            "content_type": self.content_type
        }.items())

    def set_resource(self, typename, data):
        self.typename = typename
        self.resource = data
        self.content_type = None


class CreateRequestIndication(ResourceRequestIndication):
    method = RequestIndicationMethod.create


class NotifyRequestIndication(ResourceRequestIndication):
    method = RequestIndicationMethod.notify


class NotifyCollectionRequestIndication(ResourceRequestIndication):
    method = RequestIndicationMethod.notify


class UpdateRequestIndication(ResourceRequestIndication):
    method = RequestIndicationMethod.update

    def __init__(self, path, resource, typename=None, content_type=None,
                 fields=(), do_announce=True, *args, **kw):
        self.fields = fields
        try:
            typename = resource.typename
        except AttributeError:
            pass
        else:
            if not fields:
                fields = [a.name for a in resource.attributes
                          if a.accesstype == a.RW]
            resource = dict([(f, getattr(resource, f)) for f in fields])

        super(UpdateRequestIndication, self).__init__(path=path,
                                                      resource=resource,
                                                      typename=typename,
                                                      content_type=content_type,
                                                      *args, **kw)

        # TODO: internal use only. Move into openmtc_scl package
        self.do_announce = do_announce

    def as_dict(self):
        return dict(super(ResourceRequestIndication, self).as_dict().items() + {
            "do_announce": self.do_announce
        }.items())
