from selenium import webdriver
import time
import selenium
import sys

url = sys.argv[1]
projectname = 'EDSE2E_UI'
tjobname = 'eds-base-tjob'
tjobimage = 'elastest/eds-base'

COMMANDS = """
git clone https://github.com/elastest/elastest-device-emulator-service.git /tmp/eds
./create-app-structure -d TestApplication
cp /tmp/eds/demo/eds_sut/TestApplication/__init__.py apps/TestApplication/src/testapplication/
cp /tmp/eds/demo/eds_sut/TestApplication/__main__.py apps/TestApplication/src/testapplication/
cp /tmp/eds/demo/eds_sut/TestApplication/test_application.py apps/TestApplication/src/testapplication/

./apps/test-application -v
"""

driver = webdriver.Chrome()
driver.get(url)

time.sleep(10)
# Click the main menu
driver.find_element_by_id("main_menu").click()
time.sleep(3)
# Click on Projects
driver.find_element_by_id("nav_projects").click()
time.sleep(2)

# Create new project
driver.find_element_by_xpath("//button[contains(string(), 'New Project')]").click()
driver.find_element_by_name("project.name").send_keys(projectname)
driver.find_element_by_xpath("//button[contains(string(), 'SAVE')]").click()
time.sleep(2)

# Create a new TJob
driver.find_element_by_xpath("//button[contains(string(), 'New TJob')]").click()
driver.find_element_by_name("tJobName").send_keys(tjobname)
driver.find_element_by_class_name("mat-select-arrow").click()
driver.find_element_by_xpath("//md-option[contains(string(), 'None')]").click()
driver.find_element_by_name("tJobImageName").send_keys(tjobimage)
driver.find_element_by_name("commands").send_keys(COMMANDS)
driver.find_element_by_xpath("//md-checkbox[@title='Select EDS']").click()
driver.find_element_by_xpath("//button[contains(string(), 'SAVE')]").click()
time.sleep(4)

driver.find_element_by_xpath("//button[@title='Run TJob']").click()
time.sleep(5)

res = None
while True:
    try:
        res = driver.find_element_by_xpath("//etm-dashboard/div")
        if "Executing" in res.text:
            print('Executing test')
        elif "Finished" in res.text:
            break
    except selenium.common.exceptions.NoSuchElementException:
        print("waiting for tjob to finish")
        timesleep(20)
    time.sleep(5)

if "SUCCESS" in res.text:
    print('TJob succeeded')
    print(res.text)
    exit(0)

else:
    print('TJob failed')
    print(res.text)
    exit(1)

driver.close()
