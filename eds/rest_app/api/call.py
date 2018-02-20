# Python 2.7.6
# RestfulClient.py
import re
import requests
from requests.auth import HTTPDigestAuth
import json
from base64 import b64decode

# Replace with the correct URL
url1 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/x/latest/"
url2 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/y/latest/"
url3 = "http://172.18.0.2:8000/onem2m/MemsIPE/sensor_data/z/latest/"

url={url1, url2, url3}

print len(url)

# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
#myResponse = requests.get(url, auth=HTTPDigestAuth(raw_input("username: "), raw_input("Password: ")), verify=True)
for i in url:
	#print i
	myResponse = requests.get(i)
	print "code:"+ str(myResponse.status_code)
#print myResponse.text


# For successful API call, response code will be 200 (OK)
	if (myResponse.ok):

	# Loading the response data into a dict variable
	# json.loads takes in only binary or string variables so using content to fetch binary content
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
	#jData = json.loads(myResponse.content)
		jData = myResponse.content
		#print "this is ", jData

		#print len(jData)

		array = json.loads(jData)
		#print array["m2m:cin"]["con"]
		convert = b64decode(array["m2m:cin"]["con"])
	print convert

else:
	# If response code is not ok (200), print the resulting http error code with description
	myResponse.raise_for_status()