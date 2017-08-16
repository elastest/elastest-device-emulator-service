
method = "POST"

path = "/m2m/applications"

request_orig = """
<?xml version="1.0"?>
<tns:application xmlns:tns="http://uri.etsi.org/m2m" tns:id="app"/>
"""

request_old = """
<?xml version="1.0"?>
<tns:application xmlns:tns="http://uri.etsi.org/m2m" appId="app"/>
"""

request = """
<?xml version="1.0"?>
<tns:application xmlns:tns="http://uri.etsi.org/m2m" appId="app">
    <tns:searchStrings><tns:searchString>SmartMeter</tns:searchString><tns:searchString>GA</tns:searchString><tns:searchString>Home</tns:searchString><tns:searchString>plugin-smartMeterApp-default</tns:searchString></tns:searchStrings>
</tns:application>
"""

request_plain = """
<?xml version="1.0"?>
<tns:application xmlns:tns="http://uri.etsi.org/m2m" appId="app">
</tns:application>
"""

response_orig = """
<?xml version="1.0"?>
<tns:application xmlns:tns="http://uri.etsi.org/m2m" tns:id="app">
    <tns:expirationTime>2012-10-25T13:13:04</tns:expirationTime>
</tns:application>
"""

response = """
<?xml version="1.0"?>
<tns:application xmlns:tns="http://uri.etsi.org/m2m" appId="app">
    <tns:expirationTime>2012-10-25T13:13:04</tns:expirationTime>
</tns:application>
"""
