import pprint
import requests
import os
import sys
import json
import time

# function that calls all other tests
projectId = 0
tjobId = 0
edsip = ""


def e2etests():
	tormurl = sys.argv[1]
	# To check whether the TORM URL has been read correctly
	if tormurl[-1] != '/':
		tormurl = tormurl + '/'

	print("TORM URL is: " + tormurl)
	# List of all the tests to be run. Append to this list the new tests
	tests = ["test_load_torm_home_preloader(tormurl)",
			 "test_load_torm_api_info(tormurl+\"/api/context/services/info\")", "test_service_launch(tormurl)",
			 "test_create_new_project(tormurl+\"/api/project\")"]
	# tests=["test_load_torm_home_preloader(tormurl)","test_load_torm_api_info(tormurl+\"/api/context/services/info\")","test_service_launch(tormurl)"]
	numtests = len(tests)
	testssuccess = 0
	testsfailed = 0
	testsrun = 0
	testsleft = numtests
	# Check if the number of tests is empty
	if numtests != 0:
		# Iterate through each test in the list of tests
		for i in range(len(tests)):
			testsrun += 1
			print("~~~~~~~~~~~~~~~")
			print("Running test " + str(testsrun) + " out of " + str(testsleft))
			status = eval(tests[i])
			# Check if the last test executed successfully.
			if status == "success":
				testssuccess += 1
				print("Status: Success")
			if status == "failed":
				testsfailed += 1
				print("Status: Failed")
				# A failed test will prevent the execution of future tests. This behavior is debatable.
				break

	print("##############")
	print("_TESTS SUMMARY_")
	print("TOTAL TESTS RAN: " + str(testsrun))
	print("TOTAL TESTS SUCCEEDED: " + str(testssuccess))
	print("TOTAL TESTS FAILED: " + str(testsfailed))


# Launch EDS service via ess
def test_service_launch(tormurl):
	getinstancesurl = tormurl + "api/esm/services/instances"
	s = requests.Session()
	r = s.get(getinstancesurl)
	# There should not be any ESS services already launched
	if r.text == '[]':
		launchurl = tormurl + "api/esm/services/af7947d9-258b-4dd1-b1ca-17450db25ef7/prov"
		# Lauch an instance of the EdS service using the id of the EDS service provide by the ESM
		r1 = s.post(launchurl)
		# An empty response body indicates failed launch
		if len(r1.text) != 0:
			getedsipurl = tormurl + "/api/esm/services/instances/" + r1.text
			# Check to see if the request to launch ESS was accepted
			r2 = s.get(getinstancesurl)
			# JSON List of all instance of the services
			instances = json.loads(r2.text)
			# This loop is to add waiting time for the ESS service to be launched
			while 0 == len(instances):
				print("Waiting for the launched EDS instance to appear in instances set (load completely)")
				time.sleep(5)
				r2 = s.get(getinstancesurl)
				instances = json.loads(r2.text)
			# This loop is to check if the launched service is ready
			while False == instances[0]["serviceReady"]:
				r2 = s.get(getinstancesurl)
				instances = json.loads(r2.text)
				print("Waiting for service to be ready")
				time.sleep(5)

			if True == instances[0]["serviceReady"]:
				r3 = s.get(getedsipurl)

				global edsip
				edsip = json.loads(r3.text)["serviceIp"]
				print("The IP address of EDS is: " + str(edsip))
				return "success"

		else:
			print("Length of instances array returned is 0")
			return "failed"
	else:
		print("Pre-launch issue: Some services are running before launching")
		return "failed"


# Function to check whether the TORM preloader page can successfully retrieved
def test_load_torm_home_preloader(tormurl):
	s = requests.Session()
	r = s.get(tormurl)
	# print(r.text)
	try:
		assert "Loading ElasTest..." in r.text
	except AssertionError:
		print("Test to load TORM home page prealoader failed")
		return "failed"
	print("TORM home page loaded successfully")
	return "success"


# Function to check whether the TORM API is running correctly
def test_load_torm_api_info(tormapiinfourl):
	s = requests.Session()
	r = s.get(tormapiinfourl)
	# print(r.text)
	try:
		assert "elasticSearchUrl" in r.text
	except AssertionError:
		print("Call to load elasticSearchUrl failed")
		return "failed"
	print("TORM API is correctly accessible")
	return "success"


# Function to make REST API calls to create a project in TORM
def test_create_new_project(tormapicreateprojecturl):
	s = requests.Session()
	payload = {"id": 0, "name": "E2E test EDS"}
	r = s.post(tormapicreateprojecturl, json=payload)
	# Storing value in a global variable so that other functions can read it
	global projectId
	projectId = int(json.loads(r.text)["id"])
	try:
		assert "E2E test EDS" in r.text
	except AssertionError:
		print("New Project creation failed")
		return "failed"
	print("Successfully created a test project named " + payload["name"])
	return "success"

if __name__ == "__main__":
	e2etests()