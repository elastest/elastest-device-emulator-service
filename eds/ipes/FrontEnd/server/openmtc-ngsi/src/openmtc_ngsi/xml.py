from futile.etree.ElementTree import (ElementTree, ParseError, XML, Element,
                                      SubElement, tostring)

import openmtc_ngsi.requests
from futile.logging import LoggerMixin
from openmtc_ngsi.exc import InvalidRequest
from openmtc_ngsi.requests import RequestElement, EntityId


class NGSIXMLParser(LoggerMixin):
    def parse(self, input, expect=None):
        try:
            if isinstance(input, str):
                doc = XML(input)
            else:
                doc = ElementTree().parse(input)
        except ParseError as e:
            raise InvalidRequest("Error parsing request: %s" % (e,))

        expect = expect or self._get_message_type(doc.tag)

        return self._parse_object_checked(doc, expect)

    parse_request = parse

    @staticmethod
    def _get_message_type(name):
        try:
            return getattr(openmtc_ngsi.requests, name[0].upper() + name[1:])
        except AttributeError:
            raise InvalidRequest("Unknown element name: %s" % (name,))

    def _qn(self, name):
        return name

    @staticmethod
    def _get_tagname(cls):
        return cls.__name__[0].lower() + cls.__name__[1:]

    def _parse_object_checked(self, element, expect):
        if issubclass(expect, (str, int, float, bool)):
            return element.text or None

        if element.tag != self._get_tagname(expect):
            raise InvalidRequest("Wrong tag: %s. Expected %s." %
                                 (element.tag, self._get_tagname(expect)))

        return self._parse_object(element, expect)

    @staticmethod
    def _convert_bool(val):
        if not val:
            return False

        val = val.lower()
        if val not in ("1", "0", "t", "f", "true", "false", "y", "n",
                       "yes", "no"):
            raise InvalidRequest("Unacceptable value for bool: %s" % (val,))
        val = val[0] in ("1", "t", "y")
        return val

    def _parse_object(self, element, expect):
        values = {}
        for a in expect.__attributes__:
            child = element.find(self._qn(a.name))
            if child is None:
                if a.name in ("type", "isPattern"):
                    val = element.get(a.name)
                    if a.name == "isPattern" and val:
                        val = self._convert_bool(val)
                else:
                    val = None
            elif isinstance(a.type, list):
                val = self._parse_list(child, a.type[0])
            elif issubclass(a.type, RequestElement):
                val = self._parse_object(child, a.type)
            elif a.type is bool:
                val = self._convert_bool(val)
            else:
                try:
                    val = a.type(child.text)
                except (TypeError, ValueError):
                    raise InvalidRequest("Illegal value for type %s: %s" %
                                         (a.type, child.text))

            values[a.name] = val

        return expect(**values)

    def _parse_list(self, element, expect):
        return [self._parse_object_checked(child, expect) for child in element]


RequestParser = NGSIXMLParser


class NGSIXMLWriter(LoggerMixin):
    def serialize(self, response):
        tagname = type(response).__name__
        tagname = tagname[0].lower() + tagname[1:]
        root = Element(tagname)
        self._dump_object(root, response)
        return tostring(root, pretty_print=True)

    def _dump_list(self, parent, val):
        if val:
            for v in val:
                self._dump_object(SubElement(parent,
                                             self._get_tagname(v.__class__)), v)

    @staticmethod
    def _get_tagname(cls):
        return cls.__name__[0].lower() + cls.__name__[1:]

    def _dump_object(self, parent, o):
        for a in o.get_attributes():
            val = getattr(o, a.name)

            if isinstance(o, EntityId) and a.name == "type":
                parent.set(a.name, val or "Generic")
            elif a.name == "isPattern":
                parent.set(a.name, val or "false")
            elif val is not None:
                child = SubElement(parent, a.name)

                if isinstance(a.type, list):
                    val = self._dump_list(child, val)
                elif issubclass(a.type, RequestElement):
                    val = self._dump_object(child, val)
                elif val is not None:
                    if a.type is bool:
                        val = val.lower()
                    child.text = str(val)
