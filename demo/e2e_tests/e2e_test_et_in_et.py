from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys
import logging
import os

# create a custom logger
logger = logging.getLogger(__name__)

# create handlers for logger
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)

url = sys.argv[1]
projectname = 'EDSE2E_UI'
tjobname = 'sampletjob'
tjobimage = 'elastest/eds-base'
WAIT_TIME = 300

COMMANDS = """
git clone https://github.com/elastest/elastest-device-emulator-service.git /tmp/eds
./create-app-structure -d TestApplication
cp /tmp/eds/demo/e2e_tests/TestApplication/__init__.py apps/TestApplication/src/testapplication/
cp /tmp/eds/demo/e2e_tests/TestApplication/__main__.py apps/TestApplication/src/testapplication/
cp /tmp/eds/demo/e2e_tests/TestApplication/test_application.py apps/TestApplication/src/testapplication/

./apps/test-application -v
"""
logging.debug("Entered into the execution")
print("starting the driver")
print("Check if EUS URL is available")
euspresent = False
try:
    eusurl = os.environ["ET_EUS_API"]
    euspresent = True
except Exception as e:
    print("EUS URL not present")
    print(e)
driver = None
if euspresent:
    print("EUS present therefore using remote driver")
    driver = webdriver.Remote(command_executor=eusurl, desired_capabilities=DesiredCapabilities.CHROME)
else:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
# driver.implicitly_wait(10)
if driver is None:
    print("Driver not assigned as intended")
    exit(-1)
driver.get(url)

time.sleep(5)
driverWait = WebDriverWait(driver, WAIT_TIME)
# Click the main menu
try:
    elemProjects = driverWait.until(EC.presence_of_element_located((By.ID, "nav_projects")))
except Exception as e:
    print(e)

print("Found nav_projects button")
if not elemProjects.is_displayed():
    try:
        elemMenu = driverWait.until(EC.presence_of_element_located((By.ID, "main_menu")))
    except Exception as e:
        print(e)
    elemMenu.click()
elemProjects.click()
print("Clicked on project navigation")

def delete_existing_project(driverWait, row):
    print("clicked project table entry")
    row.click()
    # enter into the project page
    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//button[@title='Delete Project']")))
    clickElem.click()
    print("delete project button")
    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(string(), 'Yes, delete')]")))
    clickElem.click()
    print("Confirmed to delete the project")

# check if there exists already an EDSE2E project and delete it
table = driverWait.until(EC.presence_of_element_located((By.ID, "projects")))
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    if projectname in row.text:
        print("project name exists")
        delete_existing_project(driverWait, row)

time.sleep(5)
# Create new project
try:
    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(string(), 'New Project')]")))
except Exception as e:
    print(e)

clickElem.click()
print("clicked on New Project button")
time.sleep(2)
try:
    elem = driverWait.until(EC.presence_of_element_located((By.NAME, "project.name")))
except Exception as e:
    print(e)

elem.send_keys(projectname)
print("Wrote project name")
time.sleep(2)

try:
    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(string(), 'SAVE')]")))
except Exception as e:
    print(e)

clickElem.click()
print("Saved project name")

#Create a new TJob
try:
#    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(string(), 'New TJob')]")))
     clickElem = driverWait.until(EC.presence_of_element_located((By.ID, "newTJobBtn")))
except Exception as e:
    print(e)

clickElem.click()
print("Clicked on New TJob button")

time.sleep(3)
try:
    elem = driverWait.until(EC.presence_of_element_located((By.NAME, "tJobName")))
except Exception as e:
    print(e)

elem.send_keys(tjobname)
print("Wrote TJob name")
time.sleep(2)

try:
    clickElem = driverWait.until(EC.presence_of_element_located((By.NAME, "tJobSut")))
except Exception as e:
    print(e)

clickElem.click()
print("Clicked on the tJobSuT")
time.sleep(2)

# driver.find_element_by_class_name("mat-select-trigger").click()
try:
    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//md-option[contains(string(), 'None')]")))
except Exception as e:
    print(e)

clickElem.click()
print("Selected None as SuT for the TJob")
time.sleep(2)

try:
    elem = driverWait.until(EC.presence_of_element_located((By.NAME, "tJobImageName")))
except Exception as e:
    print(e)

elem.send_keys(tjobimage)
print("Wrote the tjobimage")
time.sleep(2)

try:
    elem = driverWait.until(EC.presence_of_element_located((By.NAME, "commands")))
except Exception as e:
    print(e)

elem.send_keys(COMMANDS)
print("Wrote the TJob commands")
time.sleep(5)

try:
    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//md-checkbox[@title='Select EDS']")))
except Exception as e:
    print(e)

clickElem.click()
print("Select EDS as the TSS to be used for TJob")
time.sleep(2)
try:
    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(string(), 'SAVE')]")))
except Exception as e:
    print(e)

time.sleep(4)
clickElem.click()
print("Saved the TJob configuration")

try:
    clickElem = driverWait.until(EC.presence_of_element_located((By.XPATH, "//button[@title='Run TJob']")))
except Exception as e:
    print(e)

clickElem.click()
time.sleep(5)
print("Clicked on Run TJob")

res = None
MAX_WAIT = 120
i = 0
while True:
    try:
        res = driver.find_elements(By.TAG_NAME, "h4")
        if not res:
            res = driver.find_elements(By.ID, "runningSpinner")
            if res:
                print("Test execution in progress")
            else:
                print("Unknown condition encountered")
        else:
            break
    except Exception as e:
        print("Elements not found")
    time.sleep(20)
    i += 1
    if i > MAX_WAIT:
        break

if "SUCCESS" in res[0].text:
    print('TJob succeeded')
    print(res[0].text)
    exit(0)

else:
    print('TJob failed')
    print(res.text)
    exit(1)

driver.close()
