import base64
import json

from openmtc_onem2m.model import (ContentInstance)
from openmtc_server.Plugin import Plugin

from pymongo import MongoClient

client = MongoClient()
db = client.openiotfogHistoryDBPlugin

def parseandsaveinDB(content):
    result = db.allsensordata.insert_one(content)
    result = db[content['bn']].insert_one(content)

def saveinDB(container, contentlist):
    resourcepath = {'container': container}

    for content in contentlist:
        content.update(resourcepath)
        # print content
        parseandsaveinDB(content)

class HistoricalData(Plugin):
    def __init__(self, api, config, *args, **kw):
        super(HistoricalData, self).__init__(api, config, *args,
                                     **kw)

    def _init(self):
        self.events.resource_created.register_handler(
            self._get_all_contentInstances, ContentInstance)
        self._initialized()

    def _get_all_contentInstances(self, cin, req):
        """
                :type cin: ContentInstance
                :return:
                """
        if isinstance(cin, ContentInstance):
            #Get content of the contentInstance
            media_type, encoding_type = cin.contentInfo.split(':')
            content = cin.content
            try:
                if int(encoding_type) == 1:
                    content = base64.b64decode(content)
                if media_type == 'application/json':
                    content = json.loads(content)

            except ValueError:
                pass
            self.get_targeted_content(cin, content)

    def get_targeted_content(self, cin, Content):
            if "sensor_data" in cin.path:
                #print cin.parent_path # path of the parent of the CI
                #print Content
                # print Content[0]['u']
                # print Content[0]['v']
                # print Content[0]['bn']
                # print Content[0]['t']
                # print Content[0]['n']
                saveinDB(cin.parent_path,Content)
            else:
                pass
                # print "historical data handler plugin: content not valid"

