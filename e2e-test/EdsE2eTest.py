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
	tests = ["test_load_torm_home_preloader(tormurl)", "test_load_torm_api_info(tormurl+\"/api/context/services/info\")",
	 "test_service_launch(tormurl)", "test_create_new_project(tormurl+\"/api/project\")",
			 "test_create_new_tjob(tormurl+\"/api/tjob\")","test_run_tjob(tormurl)"]
	# tests=["test_load_torm_home_preloader(tormurl)","test_load_torm_api_info(tormurl+\"/api/context/services/info\")",
	# "test_service_launch(tormurl)"]
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


# Create a new tjob as part of a project
def test_create_new_tjob(tormapicreatetjoburl):
	s = requests.Session()
	# This is the standard payload used to create an a tjob using the image dockernash/ess-e2e
	payload = {
		"id": 0,
		"name": "E2E tjob",
		"imageName": "dockernash/ess-e2e",
		"project": {
			"id": projectId,
			"name": "E2E test EDS",
			"suts": [],
			"tjobs": []
		},
		"tjobExecs": [],
		"parameters": [],
		"commands": "python tjob-request.py " + edsip,
		"resultsPath": "",
		"execDashboardConfig": "{\"showComplexMetrics\":true,\"allMetricsFields\":{\"fieldsList\":[{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_cpu_totalUsage\",\"activated\":false,\"type\":\"cpu\",\"subtype\":\"totalUsage\",\"unit\":\"percent\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_memory_usage\",\"activated\":false,\"type\":\"memory\",\"subtype\":\"usage\",\"unit\":\"percent\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_memory_maxUsage\",\"activated\":false,\"type\":\"memory\",\"subtype\":\"maxUsage\",\"unit\":\"bytes\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_blkio_read_ps\",\"activated\":false,\"type\":\"blkio\",\"subtype\":\"read_ps\",\"unit\":\"bytes\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_blkio_write_ps\",\"activated\":false,\"type\":\"blkio\",\"subtype\":\"write_ps\",\"unit\":\"bytes\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_blkio_total_ps\",\"activated\":false,\"type\":\"blkio\",\"subtype\":\"total_ps\",\"unit\":\"bytes\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_net_rxBytes_ps\",\"activated\":false,\"type\":\"net\",\"subtype\":\"rxBytes_ps\",\"unit\":\"amount/sec\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_net_rxErrors_ps\",\"activated\":false,\"type\":\"net\",\"subtype\":\"rxErrors_ps\",\"unit\":\"amount/sec\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_net_rxPackets_ps\",\"activated\":false,\"type\":\"net\",\"subtype\":\"rxPackets_ps\",\"unit\":\"amount/sec\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_net_txBytes_ps\",\"activated\":false,\"type\":\"net\",\"subtype\":\"txBytes_ps\",\"unit\":\"amount/sec\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_net_txErrors_ps\",\"activated\":false,\"type\":\"net\",\"subtype\":\"txErrors_ps\",\"unit\":\"amount/sec\"},{\"component\":\"\",\"stream\":\"et_dockbeat\",\"streamType\":\"composed_metrics\",\"name\":\"et_dockbeat_net_txPackets_ps\",\"activated\":false,\"type\":\"net\",\"subtype\":\"txPackets_ps\",\"unit\":\"amount/sec\"}]},\"allLogsTypes\":{\"logsList\":[{\"component\":\"test\",\"stream\":\"default_log\",\"streamType\":\"log\",\"name\":\"test_default_log_log\",\"activated\":true},{\"component\":\"sut\",\"stream\":\"default_log\",\"streamType\":\"log\",\"name\":\"sut_default_log_log\",\"activated\":true}]}}",
		"execDashboardConfigModel": {
			"showComplexMetrics": True,
			"allMetricsFields": {
				"fieldsList": [
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_cpu_totalUsage",
						"activated": False,
						"type": "cpu",
						"subtype": "totalUsage",
						"unit": "percent"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_memory_usage",
						"activated": False,
						"type": "memory",
						"subtype": "usage",
						"unit": "percent"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_memory_maxUsage",
						"activated": False,
						"type": "memory",
						"subtype": "maxUsage",
						"unit": "bytes"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_blkio_read_ps",
						"activated": False,
						"type": "blkio",
						"subtype": "read_ps",
						"unit": "bytes"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_blkio_write_ps",
						"activated": False,
						"type": "blkio",
						"subtype": "write_ps",
						"unit": "bytes"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_blkio_total_ps",
						"activated": False,
						"type": "blkio",
						"subtype": "total_ps",
						"unit": "bytes"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_net_rxBytes_ps",
						"activated": False,
						"type": "net",
						"subtype": "rxBytes_ps",
						"unit": "amount/sec"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_net_rxErrors_ps",
						"activated": False,
						"type": "net",
						"subtype": "rxErrors_ps",
						"unit": "amount/sec"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_net_rxPackets_ps",
						"activated": False,
						"type": "net",
						"subtype": "rxPackets_ps",
						"unit": "amount/sec"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_net_txBytes_ps",
						"activated": False,
						"type": "net",
						"subtype": "txBytes_ps",
						"unit": "amount/sec"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_net_txErrors_ps",
						"activated": False,
						"type": "net",
						"subtype": "txErrors_ps",
						"unit": "amount/sec"
					},
					{
						"component": "",
						"stream": "et_dockbeat",
						"streamType": "composed_metrics",
						"name": "et_dockbeat_net_txPackets_ps",
						"activated": False,
						"type": "net",
						"subtype": "txPackets_ps",
						"unit": "amount/sec"
					}
				]
			},
			"allLogsTypes": {
				"logsList": [
					{
						"component": "test",
						"stream": "default_log",
						"streamType": "log",
						"name": "test_default_log_log",
						"activated": True
					},
					{
						"component": "sut",
						"stream": "default_log",
						"streamType": "log",
						"name": "sut_default_log_log",
						"activated": True
					}
				]
			}
		},
		"esmServicesString": "[{\"id\":\"a1920b13-7d11-4ebc-a732-f86a108ea49c\",\"name\":\"EBS\",\"selected\":false},{\"id\":\"fe5e0531-b470-441f-9c69-721c2b4875f2\",\"name\":\"EDS\",\"selected\":false},{\"id\":\"af7947d9-258b-4dd1-b1ca-17450db25ef7\",\"name\":\"ESS\",\"selected\":true},{\"id\":\"29216b91-497c-43b7-a5c4-6613f13fa0e9\",\"name\":\"EUS\",\"selected\":false},{\"id\":\"bab3ae67-8c1d-46ec-a940-94183a443825\",\"name\":\"EMS\",\"selected\":false}]",
		"esmServices": [
			{
				"id": "a1920b13-7d11-4ebc-a732-f86a108ea49c",
				"name": "EBS",
				"selected": False
			},
			{
				"id": "fe5e0531-b470-441f-9c69-721c2b4875f2",
				"name": "EDS",
				"selected": False
			},
			{
				"id": "af7947d9-258b-4dd1-b1ca-17450db25ef7",
				"name": "ESS",
				"selected": True
			},
			{
				"id": "29216b91-497c-43b7-a5c4-6613f13fa0e9",
				"name": "EUS",
				"selected": False
			},
			{
				"id": "bab3ae67-8c1d-46ec-a940-94183a443825",
				"name": "EMS",
				"selected": False
			}
		],
		"esmServicesChecked": 0
	}

	r = s.post(tormapicreatetjoburl, json=payload)
	# Storing the value of the tjobid in a gloabl variable so that the function to run the tjob can access it
	global tjobId
	tjobId = int(json.loads(r.text)["id"])
	# print tjobId
	try:
		assert "E2E tjob" in r.text
	except AssertionError:
		print("New TJob creation failed")
		return "failed"
	print("Successfully created a tjob with name " + payload["name"])
	return "success"


# Function to test the running of the tjob
def test_run_tjob(tormurl):
	time.sleep(5)
	s = requests.Session()
	# Strangely enough, this was the body of the request for running a tjob
	payload = {"tJobParams": []}
	r = s.post(tormurl + "api/tjob/" + str(tjobId) + "/exec", json=payload)
	# print(r.text)

	try:
		# Check wither the tjob execution is in progress
		assert "IN PROGRESS" in str(json.loads(r.text)["result"])
		exec_resp = s.get(tormurl + "api/tjob/" + str(tjobId) + "/exec/" + str(json.loads(r.text)["id"]))
		# Loop of waits until the tjob has been executed completely. Note to make use the of the maxexectime of tjobs to avoid this wait to be indefinite of the tjob is stuck in a loop
		while ("FAIL" != str(json.loads(exec_resp.text)["result"]).strip()) and (
			"SUCCESS" != str(json.loads(exec_resp.text)["result"]).strip()):
			print("TJob execution status is: " + str(json.loads(exec_resp.text)["result"]))
			exec_resp = s.get(tormurl + "api/tjob/" + str(tjobId) + "/exec/" + str(json.loads(r.text)["id"]))
			time.sleep(5)

		# The statements to execute if the tjob execution is successful
		if "SUCCESS" in str(json.loads(exec_resp.text)["result"]):
			# print exec_resp.text
			print("TJob execution successful")
			return "success"
		# The statements to execute if the tjob execution fails
		elif "FAIL" in str(json.loads(exec_resp.text)["result"]):
			# print exec_resp.text
			print("TJob execution failed")
			return "failed"
		# The statements to execute if there are some unforseen errors
		else:
			print("TJob execution status is neither success nor fail")
			return "failed"

	except AssertionError:
		print("TJob execution failed")
		return "failed"

if __name__ == "__main__":
	e2etests()