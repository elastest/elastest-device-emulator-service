from selenium import webdriver

#from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By

import time
import unittest





class Tjobs(unittest.TestCase):


	#open nightly and go to test support services
	def Test_job1(self):
		#show the location of web driver locally
		self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

		self.driver.implicitly_wait(20)
		self.driver.maximize_window()

		#self.driver.get("http://elastest.io:37000")
		self.driver.set_page_load_timeout(100000)
		self.driver.get("http://elastest.io/")
		assert self.driver.title, 'Elastest Home'
		#sleep(2)
		self.driver.save_screenshot('./e2e/Elastest_io.png')



# Boilerplate code to start the unit tests
if __name__ == "__main__":
	unittest.main()