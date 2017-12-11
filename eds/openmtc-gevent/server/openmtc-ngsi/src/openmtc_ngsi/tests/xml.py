
import unittest
from futile.StringIO import StringIO
from openmtc_ngsi.requests import EntityId

registerContextRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
   <registerContextRequest>
     <contextRegistrationList>
       <contextRegistration>
         <entityIdList>
           <entityId type="Room" isPattern="false">
             <id>ConferenceRoom</id>
           </entityId>
         </entityIdList>
         <contextRegistrationAttributeList>
           <contextRegistrationAttribute>
             <name>pressure</name>
             <type>BAR</type>
             <isDomain>false</isDomain>
             <metadata>
               <contextMetadata>
                 <name>ID</name>
                 <type>string</type>
                 <value>pressureInConferenceRoom</value>
               </contextMetadata>
               <contextMetadata>
                 <name>location</name>
                 <type>string</type>
                 <value>north-east corner</value>
               </contextMetadata>
             </metadata>
           </contextRegistrationAttribute>
         </contextRegistrationAttributeList>
         <providingApplication>http://192.168.100.1:70/application</providingApplication>
       </contextRegistration>
     </contextRegistrationList>
     <duration>PT1M</duration>
     <registrationId>1342519697T001</registrationId>
   </registerContextRequest>
 """
 
registerContextRequestXML2 = """<?xml version="1.0" encoding="UTF-8"?>
   <registerContextRequest>
     <contextRegistrationList>
       <contextRegistration>
         <entityIdList>
           <entityId type="Room" isPattern="false">
             <id>OfficeRoom</id>
           </entityId>
         </entityIdList>
         <contextRegistrationAttributeList>
           <contextRegistrationAttribute>
             <name>pressure</name>
             <type>BAR</type>
             <isDomain>false</isDomain>
             <metadata>
               <contextMetadata>
                 <name>ID</name>
                 <type>string</type>
                 <value>pressureInConferenceRoom</value>
               </contextMetadata>
               <contextMetadata>
                 <name>location</name>
                 <type>string</type>
                 <value>north-east corner</value>
               </contextMetadata>
             </metadata>
           </contextRegistrationAttribute>
         </contextRegistrationAttributeList>
         <providingApplication>http://192.168.100.1:70/application</providingApplication>
       </contextRegistration>
     </contextRegistrationList>
     <duration>PT1M</duration>
     <registrationId>1342519697T001</registrationId>
   </registerContextRequest>
 """
 
discoverContextAvailabilityRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
   <discoverContextAvailabilityRequest>
     <entityIdList>
       <entityId type="Room" isPattern="false">
         <id>ConferenceRoom</id>
       </entityId>
       <entityId type="Room" isPattern="false">
         <id>OfficeRoom</id>
       </entityId>
     </entityIdList>
     <attributeList>
       <attribute>temperature</attribute>
       <attribute>pressure</attribute>
       <attribute>occupancy</attribute>
       <attribute>lightstatus</attribute>
     </attributeList>
     <restriction>
       <attributeExpression>
       </attributeExpression>
       <scope>
         <operationScope>
           <scopeType></scopeType>
           <scopeValue></scopeValue>
         </operationScope>
       </scope>
     </restriction>
   </discoverContextAvailabilityRequest>
"""

subscribeContextAvailabilityRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
   <subscribeContextAvailabilityRequest>
     <entityIdList>
       <entityId type="Room" isPattern="false">
         <id>ConferenceRoom</id>
       </entityId>
       <entityId type="Room" isPattern="false">
         <id>OfficeRoom</id>
       </entityId>
     </entityIdList>
     <attributeList>
       <attribute>temperature</attribute>
       <attribute>pressure</attribute>
       <attribute>occupancy</attribute>
       <attribute>lightstatus</attribute>
     </attributeList>
     <restriction>
       <attributeExpression>
       </attributeExpression>
       <scope>
         <operationScope>
           <scopeType></scopeType>
           <scopeValue></scopeValue>
         </operationScope>
       </scope>
     </restriction>
     <reference>http://localhost/test_notify_9</reference>
   </subscribeContextAvailabilityRequest>
"""

subscribeContextAvailabilityNoAttrsRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
   <subscribeContextAvailabilityRequest>
     <entityIdList>
       <entityId type="Room" isPattern="false">
         <id>ConferenceRoom</id>
       </entityId>
       <entityId type="Room" isPattern="false">
         <id>OfficeRoom</id>
       </entityId>
     </entityIdList>
     <restriction>
       <attributeExpression>
       </attributeExpression>
       <scope>
         <operationScope>
           <scopeType></scopeType>
           <scopeValue></scopeValue>
         </operationScope>
       </scope>
     </restriction>
     <reference>http://localhost/test_notify_9/no_attrs</reference>
   </subscribeContextAvailabilityRequest>
"""

updateContextAvailabilityRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
   <updateContextAvailabilitySubscriptionRequest>
     <entityIdList>
       <entityId type="Room" isPattern="false">
         <id>ConferenceRoom</id>
       </entityId>
       <entityId type="Room" isPattern="false">
         <id>OfficeRoom</id>
       </entityId>
     </entityIdList>
     <attributeList>
       <attribute>temperature</attribute>
       <attribute>pressure</attribute>
       <attribute>occupancy</attribute>
       <attribute>lightstatus</attribute>
     </attributeList>
     <restriction>
       <attributeExpression>
       </attributeExpression>
       <scope>
         <operationScope>
           <scopeType></scopeType>
           <scopeValue></scopeValue>
         </operationScope>
       </scope>
     </restriction>
   </updateContextAvailabilitySubscriptionRequest>
"""

unsubscribeContextAvailabilityRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
    <unsubscribeContextAvailabilityRequest>
        <subscriptionId>/m2m/applications/subscriptions/subscription475820</subscriptionId>
    </unsubscribeContextAvailabilityRequest>
"""


class TestXMLParse(unittest.TestCase):
    def setUp(self):
        from openmtc_ngsi.xml import RequestParser
        self.parser = RequestParser()
            
    def test_RegisterContextRequest(self):
        from openmtc_ngsi.requests import RegisterContextRequest
        request = self.parser.parse_request(StringIO(registerContextRequestXML), RegisterContextRequest)
        self.assertIsInstance(request, RegisterContextRequest)
        self.assertIsInstance(request.contextRegistrationList, list)
        self.assertEqual(len(request.contextRegistrationList), 1)
        self.assertIsInstance(request.contextRegistrationList[0].entityIdList, list)
        self.assertEqual(len(request.contextRegistrationList[0].entityIdList), 1, len(request.contextRegistrationList[0].entityIdList))
        self.assertIsInstance(request.contextRegistrationList[0].entityIdList[0], EntityId)
        self.assertEqual(request.contextRegistrationList[0].entityIdList[0].type, "Room")
        
    def test_DiscoverContextAvailabilityRequest(self):
        from openmtc_ngsi.requests import DiscoverContextAvailabilityRequest
        request = self.parser.parse_request(StringIO(discoverContextAvailabilityRequestXML), DiscoverContextAvailabilityRequest)
        self.assertIsInstance(request, DiscoverContextAvailabilityRequest)
        self.assertIsInstance(request.entityIdList, list)
        self.assertEqual(len(request.entityIdList), 2)
        self.assertEqual(len(request.attributeList), 4)
        self.assertListEqual(request.attributeList, [ "temperature", "pressure", "occupancy", "lightstatus" ])

if __name__ == '__main__':
    unittest.main()
