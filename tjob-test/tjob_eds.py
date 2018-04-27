from selenium import webdriver
import sys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import selenium
from time import sleep
#import unittest



#open nightly and go to test support services
url = sys.argv[1]


projectname = 'tjobs_eds_1'
tjobname = 'test_tjobs'
#env_docker_image = 'ubuntu:16.04'
env_docker_image = 'rowshan/eds_e2e'
commands = """
		git clone https://github.com/rowshan/eds_e2e.git
		cd eds_e2e
		docker build -t rowshan/eds_e2e .
		#Run the test_app image container
		docker run -p 5022:5022 rowshan/eds_e2e
		"""



#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
assert driver.title, 'Elastest Nightly Home'
sleep(1)

#driver.implicitly_wait(20)
#driver.maximize_window()



### navigate to the project in the side_nav
project = driver.find_element_by_id('nav_projects')

if not project.is_displayed():
	web_element = driver.find_element_by_id("main_menu").click()
	sleep(1)  # delay to allow menu animation to complete.
	project.click()
sleep(2)

# create new project and save it
driver.find_element_by_xpath("//button[contains(string(), 'New Project')]").click()
driver.find_element_by_name("project.name").send_keys(projectname)
driver.find_element_by_xpath("//button[contains(string(), 'SAVE')]").click()
sleep(1)


####Create a tjobs
driver.find_element_by_xpath("//button[contains(string(), 'New TJob')]").click()
driver.find_element_by_name("tJobName").send_keys(tjobname)
driver.find_element_by_class_name("mat-select-trigger").click()
driver.find_element_by_xpath("//md-option[contains(string(), 'None')]").click()
#self.driver.save_screenshot('ETM_tjobs_eds.png')

driver.find_element_by_name("tJobImageName").send_keys(env_docker_image)
#	self.driver.find_element_by_name("mat-input-infix")
driver.find_element_by_id("commands").send_keys(commands)
driver.find_element_by_xpath("//md-checkbox[@title='Select EDS']").click()
driver.find_element_by_xpath("//button[contains(string(), 'SAVE')]").click()
sleep(1)

# run tjob
driver.find_element_by_xpath("//button[@title='Run TJob']").click()
sleep(1)
driver.save_screenshot('ETM_run_eds_tjobs.png')
sleep(1)

# check job status.
while True:
	try:
		check_job_status = driver.find_element_by_xpath(
			"//etm-dashboard/div[1]/div/md-card/md-card-content/div/span[1]/span[1][ contains(string(), 'SUCCESS') or contains(string(), 'ERROR') or contains(string(), 'FAIL') ]")
		print(check_job_status.text)
		break
	except selenium.common.exceptions.NoSuchElementException:
		print("waiting to finish ...")
		sleep(20)

if 'SUCCESS' in check_job_status.text:
	print('successfull')
	print(check_job_status.text)
	exit(0)
else:
	print('Failed')
	print(check_job_status.text)
	exit(1)
driver.close()


