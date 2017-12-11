from werkzeug.datastructures import Accept
import openmtc_server.api as api


class OpenMTCAccept(Accept):
    def best_match(self, matches, default=None):
        """Returns the best match from a list of possible matches based
        on the quality of the client.  If two items have the same quality,
        the one is returned that comes first.

        :param matches: a list of matches to check for
        :param default: the value that is returned if none match
        """
        best_quality = -1
        result = default
        result_source = None
        for server_item in matches:
            for client_item, quality in self:
                if quality <= best_quality:
                    break
                if self._value_matches(server_item, client_item):
                    best_quality = quality
                    result = server_item
                    result_source = client_item

        if result_source in ("*", "*/*"):
            result = api.config["global"].get("default_content_type",
                                              "application/json")
        return result

    def _value_matches(self, value, item):
        return item == "*/*" or \
            super(OpenMTCAccept, self)._value_matches(value, item)

