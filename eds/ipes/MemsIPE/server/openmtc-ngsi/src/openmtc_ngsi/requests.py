from operator import attrgetter


class Attribute(object):
    def __init__(self, name, type=str, required=True):
        self.name = name
        self.type = type
        self.required = required
        self.is_list = not isinstance(type, __builtins__["type"])

    def convert(self, v):
        if self.is_list:
            if not isinstance(v, (tuple, list, set)):
                raise TypeError("Illegal value for list attribute: %r" % (v, ))
        elif not isinstance(v, self.type):
            v = self.type(v)
        return v


class MessageElement(object):
    def __init__(self, *args, **kw):
        for n in self.get_attribute_names():
            setattr(self, n, kw.pop(n, None))

    def __setattr__(self, k, v):
        if v is not None and k[0] != "_":
            v = self.get_attribute(k).convert(v)
        super(MessageElement, self).__setattr__(k, v)

    @property
    def values(self):
        values = {}
        for n in self.get_attribute_names():
            values[n] = getattr(self, n)
        return values

    @classmethod
    def get_attribute_names(cls):
        try:
            return map(attrgetter("name"), cls.__attributes__)
        except TypeError:
            print (cls, cls.__attributes__)
            raise

    @classmethod
    def get_attributes(cls):
        return cls.__attributes__

    @classmethod
    def get_attribute(cls, name):
        for a in cls.get_attributes():
            if a.name == name:
                return a
        raise AttributeError(name)

RequestElement = MessageElement


class Request(RequestElement):
    pass


class StatusCode(MessageElement):
    __attributes__ = (
        Attribute("code", int),
        Attribute("reasonPhrase"),
        Attribute("details")
    )

    reasons = {
        200: "Ok",
        400: "Bad request",
        403: "Forbidden",
        404: "ContextElement not found",
        470: "Subscription ID not found",
        471: "Missing parameter",
        472: "Invalid parameter",
        473: "Error in metadata",
        480: "Regular Expression for EntityId not allowed",
        481: "Entity Type required",
        482: "AttributeList required",
        500: "Receiver internal error"
    }

    def __init__(self, code=None, reasonPhrase=None, details=None, **kw):
        if code is not None:
            code = int(code)
            try:
                r = self.reasons[code]
            except KeyError:
                raise ValueError("Illegal status code: %s" % (code, ))
            reasonPhrase = reasonPhrase or r
        super(StatusCode, self).__init__(code=code, reasonPhrase=reasonPhrase,
                                         details=details, **kw)

        assert self.code is not None


class EntityId(RequestElement):
    __attributes__ = (
        Attribute("id"),
        Attribute("type"),
        Attribute("isPattern", bool)
    )


class ContextMetadata(RequestElement):
    __attributes__ = (
        Attribute("name"),
        Attribute("type"),
        Attribute("value")
    )


class ContextRegistrationAttribute(RequestElement):
    __attributes__ = (
        Attribute("name"),
        Attribute("type"),
        Attribute("isDomain"),
        Attribute("metadata", [ContextMetadata]),
    )


class ContextRegistration(RequestElement):
    __attributes__ = (
        Attribute("entityIdList", [EntityId]),
        Attribute("contextRegistrationAttributeList",
                  [ContextRegistrationAttribute]),
        Attribute("registrationMetaData", [ContextMetadata]),
        Attribute("providingApplication")
    )


class RegisterContextRequest(Request):
    __attributes__ = (
        Attribute("contextRegistrationList", [ContextRegistration]),
        Attribute("duration", required=False),
        Attribute("registrationId", required=False)
    )


class DiscoverContextAvailabilityRequest(Request):
    __attributes__ = (
        Attribute("entityIdList", [EntityId]),
        Attribute("attributeList", [str])
    )


class SubscribeContextAvailabilityRequest(Request):
    __attributes__ = (
        Attribute("entityIdList", [EntityId]),
        Attribute("attributeList", [str]),
        Attribute("reference"),
        Attribute("duration", int),
        Attribute("subscriptionId")
    )


class UpdateContextAvailabilitySubscriptionRequest(Request):
    __attributes__ = (
        Attribute("entityIdList", [EntityId]),
        Attribute("attributeList", [str]),
        Attribute("reference"),
        Attribute("duration", int),
        Attribute("subscriptionId")
    )


class UnsubscribeContextAvailabilityRequest(Request):
    __attributes__ = (
        Attribute("subscriptionId"),
    )


class ContextAttribute(MessageElement):
    __attributes__ = (
        Attribute("name"),
        Attribute("type"),
        Attribute("contextValue"),
        Attribute("metadata", [ContextMetadata])
    )


class ContextElement(MessageElement):
    __attributes__ = (
        Attribute("entityId", EntityId),
        Attribute("attributeDomainName"),
        Attribute("contextAttributeList", [ContextAttribute]),
        Attribute("domainMetadata", [ContextMetadata])
    )


class UpdateContextRequest(Request):
    __attributes__ = (
        Attribute("contextElementList", [ContextElement]),
        Attribute("updateAction")
    )


class QueryContextRequest(Request):
    __attributes__ = (
        Attribute("entityIdList", [EntityId]),
        Attribute("attributeList", [str])
    )


class SubscribeContextRequest(Request):
    __attributes__ = (
        Attribute("entityIdList", [EntityId]),
        Attribute("attributeList", [str]),
        Attribute("reference"),
        Attribute("duration", int),
    )


class UnsubscribeContextRequest(Request):
    __attributes__ = (
        Attribute("subscriptionId"),
    )


class UpdateContextSubscriptionRequest(Request):
    __attributes__ = (
        Attribute("duration", int),
        Attribute("subscriptionId"),
    )


class Response(MessageElement):
    pass


class RegisterContextResponse(Response):
    __attributes__ = (
        Attribute("duration", int),
        Attribute("registrationId"),
        Attribute("errorCode", StatusCode)
    )


class ContextRegistrationResponse(MessageElement):
    __attributes__ = (
        Attribute("contextRegistration", ContextRegistration),
        Attribute("errorCode", StatusCode)
    )


class DiscoverContextAvailabilityResponse(Response):
    __attributes__ = (
        Attribute("contextRegistrationResponseList",
                  [ContextRegistrationResponse]),
        Attribute("errorCode", StatusCode)
    )


class SubscribeContextAvailabilityResponse(Response):
    __attributes__ = (
        Attribute("duration", int),
        Attribute("subscriptionId"),
    )


class UnsubscribeContextAvailabilityResponse(Response):
    __attributes__ = (
        Attribute("statusCode", StatusCode),
        Attribute("subscriptionId"),
    )


class UpdateContextAvailabilitySubscriptionResponse(Response):
    __attributes__ = (
        Attribute("duration", int),
        Attribute("subscriptionId"),
    )


class ContextElementResponse(MessageElement):
    __attributes__ = (
        Attribute("statusCode", StatusCode),
        Attribute("contextElement", ContextElement),
    )


class UpdateContextResponse(Response):
    __attributes__ = (
        Attribute("errorCode", StatusCode),
        Attribute("contextResponseList", [ContextElementResponse]),
    )


class QueryContextResponse(Response):
    __attributes__ = (
        Attribute("errorCode", StatusCode),
        Attribute("contextResponseList", [ContextElementResponse]),
    )


class NotifyContextAvailabilityRequest(Request):
    __attributes__ = (
        Attribute("subscriptionId"),
        Attribute("contextRegistrationResponseList",
                  [ContextRegistrationResponse]),
        Attribute("errorCode", StatusCode)
    )


class SubscribeResponse(MessageElement):
    __attributes__ = (
        Attribute("subscriptionId"),
        Attribute("duration", int),
        Attribute("throttling", int),
    )


class SubscribeError(MessageElement):
    __attributes__ = (
        Attribute("subscriptionId"),
        Attribute("errorCode", StatusCode),
    )


class SubscribeContextResponse(Response):
    __attributes__ = (
        Attribute("subscribeResponse", SubscribeResponse),
        Attribute("subscribeError", SubscribeError),
    )


class UnsubscribeContextResponse(Response):
    __attributes__ = (
        Attribute("subscriptionId"),
        Attribute("statusCode", StatusCode),
    )


class UpdateContextSubscriptionResponse(Response):
    __attributes__ = (
        Attribute("subscribeResponse", SubscribeResponse),
        Attribute("subscribeError", SubscribeError),
    )


class NotifyContextRequest(Request):
    __attributes__ = (
        Attribute("subscriptionId"),
        Attribute("originator"),
        Attribute("contextResponseList", [ContextElementResponse]),
    )
