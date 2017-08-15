
method = "GET"

path = "/m2m/applications/app"

response_orig = """
<?xml version="1.0"?>
<tns:application xmlns:tns="http://uri.etsi.org/m2m" tns:id="app">
  <tns:applicationStatus>ONLINE</tns:applicationStatus>
  <tns:expirationTime>2012-11-19T18:39:05</tns:expirationTime>
  <tns:lastModifiedTime>2012-11-12T19:59:05</tns:lastModifiedTime>
  <tns:containersReference>
              /gsclBase/applications/app/containers
  </tns:containersReference>
  <tns:groupsReference>
              /gsclBase/applications/app/groups
  </tns:groupsReference>
  <tns:accessRightsReference>
              /gsclBase/applications/app/accessRights
  </tns:accessRightsReference>
  <tns:subscriptionsReference>/ 
             /gsclBase/applications/app/subscriptions
  </tns:subscriptionsReference>
</tns:application>
"""

response = """
<?xml version="1.0"?>
<tns:application xmlns:tns="http://uri.etsi.org/m2m" appId="app">
  <tns:expirationTime>2012-11-19T18:39:05</tns:expirationTime>
  <tns:lastModifiedTime>2012-11-12T19:59:05</tns:lastModifiedTime>
  <tns:containersReference>
              /gsclBase/applications/app/containers
  </tns:containersReference>
  <tns:groupsReference>
              /gsclBase/applications/app/groups
  </tns:groupsReference>
  <tns:accessRightsReference>
              /gsclBase/applications/app/accessRights
  </tns:accessRightsReference>
  <tns:subscriptionsReference> 
             /gsclBase/applications/app/subscriptions
  </tns:subscriptionsReference>
</tns:application>
"""

