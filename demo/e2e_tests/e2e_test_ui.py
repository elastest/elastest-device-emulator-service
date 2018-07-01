from selenium import webdriver
import time
import selenium
import sys

url = sys.argv[1]
projectname = 'EDSE2E_UI'
tjobname = 'sampletjob'
tjobimage = 'elastest/eds-base'

COMMANDS = """
git clone https://github.com/elastest/elastest-device-emulator-service.git /tmp/eds
./create-app-structure -d TestApplication
cp /tmp/eds/demo/e2e_tests/TestApplication/__init__.py apps/TestApplication/src/testapplication/
cp /tmp/eds/demo/e2e_tests/TestApplication/__main__.py apps/TestApplication/src/testapplication/
cp /tmp/eds/demo/e2e_tests/TestApplication/test_application.py apps/TestApplication/src/testapplication/

./apps/test-application -v
"""

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)

time.sleep(5)
# Click the main menu
elemProjects = driver.find_element_by_id('nav_projects')
if not elemProjects.is_displayed():
    elemMenu = driver.find_element_by_id("main_menu").click()
    time.sleep(1) # delay to allow menu animation to complete.
elemProjects.click()

time.sleep(5)
# Create new project
driver.find_element_by_xpath("//button[contains(string(), 'New Project')]").click()
time.sleep(2)
driver.find_element_by_name("project.name").send_keys(projectname)
time.sleep(2)
driver.find_element_by_xpath("//button[contains(string(), 'SAVE')]").click()
time.sleep(5)

# Create a new TJob
driver.find_element_by_xpath("//button[contains(string(), 'New TJob')]").click()
time.sleep(2)
driver.find_element_by_name("tJobName").send_keys(tjobname)
time.sleep(2)
driver.find_element_by_name("tJobSut").click()
time.sleep(2)
# driver.find_element_by_class_name("mat-select-trigger").click()
driver.find_element_by_xpath("//md-option[contains(string(), 'None')]").click()
time.sleep(2)
driver.find_element_by_name("tJobImageName").send_keys(tjobimage)
time.sleep(2)
driver.find_element_by_name("commands").send_keys(COMMANDS)
time.sleep(5)
driver.find_element_by_xpath("//md-checkbox[@title='Select EDS']").click()
driver.find_element_by_xpath("//button[contains(string(), 'SAVE')]").click()
time.sleep(4)

driver.find_element_by_xpath("//button[@title='Run TJob']").click()
time.sleep(5)

res = None
MAX_WAIT = 120
i = 0
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
    i += 1
    if i > MAX_WAIT:
        break

if "SUCCESS" in res.text:
    print('TJob succeeded')
    print(res.text)
    exit(0)

else:
    print('TJob failed')
    print(res.text)
    exit(1)

driver.close()
