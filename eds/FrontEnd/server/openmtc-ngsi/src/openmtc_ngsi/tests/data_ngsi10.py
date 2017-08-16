
updateContextRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
    <updateContextRequest>
        <contextElementList>
            <contextElement>
                <entityId type="Room" isPattern="False"><id>ConferenceRoom</id></entityId>
                <contextAttributeList>
                    <contextAttribute>
                        <name>pressure</name>
                        <metadata>
                            <contextMetadata>
                                <name>timestamp</name>
                                <type>string</type>
                                <value>2013-07-02T11:33:05+01:00</value>
                            </contextMetadata>
                            <contextMetadata>
                                <name>expires</name>
                                <type>string</type>
                                <value>2013-08-02T11:33:05+01:00</value>
                            </contextMetadata>
                        </metadata>
                        <contextValue>1.2</contextValue>
                   </contextAttribute>
                </contextAttributeList>
            </contextElement>
        </contextElementList>
        <updateAction>UPDATE</updateAction>
    </updateContextRequest>
"""

queryContextRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
<queryContextRequest>
  <entityIdList>
    <entityId type="Room">
      <id>ConferenceRoom</id>
    </entityId>
    <entityId>
      <id>urn:username:sergio</id>
    </entityId>
  </entityIdList>
  <attributeList>
    <attribute>pressure</attribute>
    <attribute>cell</attribute>
  </attributeList>
  <restriction>
    <attributeExpression>//contextValue[starts-with(cgi,'222')]</attributeExpression>
  </restriction>
</queryContextRequest>"""

subscribeContextRequestXML = """<?xml version="1.0" encoding="UTF-8"?>
   <subscribeContextRequest>
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
     <reference>http://localhost/test_notify_10</reference>
   </subscribeContextRequest>
"""