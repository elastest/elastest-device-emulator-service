from json import dumps, load, loads

import openmtc_ngsi.requests
from futile.logging import LoggerMixin
from openmtc_ngsi.exc import InvalidRequest
from openmtc_ngsi.requests import (MessageElement, RequestElement, EntityId,
                                   ContextRegistrationResponse,
                                   ContextRegistration)


class NGSIJSONWriter(LoggerMixin):
    def serialize(self, response, pretty=True):

        result = self._dump_object(response)
        return dumps(result, check_circular=False,
                     indent=(pretty and 2 or None))

    def _dump_list(self, o):
        # tagname = type(o).__name__
        # tagname = tagname[0].lower() + tagname[1:]
        l = []
        # result = {tagname: l}
        # result =l
        for v in o:
            if isinstance(v, MessageElement):
                v = self._dump_object(v)
            l.append(v)
        return l
        # return result

    def _get_tagname(self, cls):
        return cls.__name__[0].lower() + cls.__name__[1:]

    def _dump_object(self, o):
        # tagname = type(o).__name__
        # tagname = tagname[0].lower() + tagname[1:]
        # if tagname.endswith("Id") or tagname.endswith("bute"):
        return self._do_dump_object(o)
        # return {
        #     tagname: self._do_dump_object(o)
        # }

    def _do_dump_object(self, o):
        result = {}
        for a in o.get_attributes():
            val = getattr(o, a.name)

            if isinstance(o, EntityId) and a.name == "type":
                result[a.name] = val or "Generic"
            elif val is not None:
                if isinstance(a.type, list):
                    val = self._dump_list(val)

                elif isinstance(o, ContextRegistrationResponse):
                    # HACK
                    if isinstance(val, ContextRegistration):
                        val = self._dump_object(val)
                        result[a.name] = { }
                        for k in val.keys():
                            result[a.name][k] = val[k]
                        continue

                    else:
                        result[a.name] = self._dump_object(val)

                elif issubclass(a.type, RequestElement):
                    val = self._dump_object(val)
                    for k in val.keys():
                        result[k] = val[k]
                    continue
                if a.name == "contextElementList":
                    result["contextElements"] = val
                elif (a.name == "contextAttributeList" or
                      a.name == "contextRegistrationAttributeList"):
                    result["attributes"] = val
                # Notify ctx availability rq
                elif a.name == "contextRegistrationResponseList":  # TODO
                    result["contextRegistrationResponses"] = val
                elif a.name == "entityIdList":  # TODO
                    result["entities"] = val
                elif a.name == "type":
                    continue
                elif a.name == "contextValue":
                    tmpval = loads(val)
                    for k in tmpval.keys():
                        result["type"] = k
                        result["value"] = tmpval[k]

                elif a.name == "metadata":
                    continue
                else:
                    result[a.name] = val
        return result


class NGSIJSONReader(LoggerMixin):
    def parse(self, input, expect=None):
        try:
            if isinstance(input, str):
                doc = loads(input)
            else:
                doc = load(input)
        except Exception as e:
            raise InvalidRequest("Error parsing request: %s" % (e, ))

        if not isinstance(doc, dict):  # or len(doc) != 1:
            raise InvalidRequest("Invalid json input: %s", doc)

        expect = expect or self._get_message_type(doc.keys()[0])

        return self._parse_object_checked(doc, expect)
    parse_request = parse

    def _parse_object_checked(self, element, expect):
        if issubclass(expect, (str, int, float, bool)):
            return element

        if not isinstance(element, dict):  # or len(element) != 1:
            raise InvalidRequest("Invalid json input: %s", element)

        if element.keys()[0] != self._get_tagname(expect):
            raise InvalidRequest("Wrong tag: %s. Expected %s." %
                                 (element.keys()[0], self._get_tagname(expect)))

        return self._parse_object(element.values()[0], expect)

    @staticmethod
    def _convert_bool(val):
        if isinstance(val, bool):
            return val

        if not val:
            return False

        val = str(val).lower()
        if val not in ("1", "0", "t", "f", "true", "false", "y", "n",
                       "yes", "no"):
            raise InvalidRequest("Unacceptable value for bool: %s" % (val, ))
        val = val[0] in ("1", "t", "y")
        return val

    def _parse_list(self, element, expect):
        if not isinstance(element, dict):  # or len(element) != 1:
            raise InvalidRequest("Invalid json input: %s", element)
        if issubclass(expect, MessageElement):
            if element.keys()[0] != self._get_tagname(expect):
                raise InvalidRequest("Wrong tag: %s. Expected %s." %
                                     (element.keys()[0],
                                      self._get_tagname(expect)))

            return [self._parse_object(child, expect)
                    for child in element.values()[0]]
        else:
            return element.values()[0]

    def _parse_object(self, element, expect):
        values = {}
        for a in expect.__attributes__:
            val = element.get(a.name)
            if val is not None:
                if a.name == "isPattern" and val:
                    val = self._convert_bool(val)
                elif isinstance(a.type, list):
                    val = self._parse_list(val, a.type[0])
                elif issubclass(a.type, RequestElement):
                    val = self._parse_object(val, a.type)
                elif a.type is bool:
                    val = self._convert_bool(val)
                else:
                    try:
                        val = a.type(val)
                    except (TypeError, ValueError):
                        raise InvalidRequest("Illegal value for type %s: %s" %
                                             (a.type, val))

            values[a.name] = val

        return expect(**values)

    @staticmethod
    def _get_message_type(name):
        try:
            return getattr(openmtc_ngsi.requests, name[0].upper() + name[1:])
        except AttributeError:
            raise InvalidRequest("Unknown element name: %s" % (name, ))

    @staticmethod
    def _get_tagname(cls):
        return cls.__name__[0].lower() + cls.__name__[1:]
