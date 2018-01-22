from selenium import webdriver

#from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait




# do stuff
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)
#driver.get("http://elastest.io:37000")
driver.get("http://elastest.io")
driver.maximize_window()
assert driver.title, 'Elastest Home'
#print(driver.title)


