from selenium import webdriver

#from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

import time
import unittest


#
# # do stuff
# driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# driver.implicitly_wait(10)
# driver.set_page_load_timeout(30)
# #driver.get("http://elastest.io:37000")
# driver.get("http://elastest.io")
# driver.maximize_window()
# assert driver.title, 'Elastest Home'
# #print(driver.title)





#import nose



class Tjobs(unittest.TestCase):


	#open nightly and go to test support services
	def Test_job1(self):
		#show the location of web driver locally
		self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

		self.driver.implicitly_wait(20)
		self.driver.maximize_window()

		#self.driver.get("http://elastest.io:37000")
		self.driver.set_page_load_timeout(100000)
		self.driver.get("http://nightly.elastest.io:37000")
		assert self.driver.title, 'Elastest Home'
		#		print(driver.title)
		self.driver.find_element_by_id("nav_support_services").click()#send_keys("navigate to create eds instanced")
		self.driver.save_screenshot('ETM.png')
		#select EDS from dropdown list and create and instance

		#select_eds = self.driver.find_element_by_id("cdk-overlay-0")
		#select_test_service = self.driver.find_element_by_class_name("ng-trigger ng-trigger-transformPanel ng-tns-c12-1 mat-select-panel mat-primary mat-select-panel-done-animating")
		#select_eds = self.driver.find_element_by_class_name("mat-option mat-selected")



		#print [o.text for o in select_eds.options]
		select_eds= self.driver.find_element_by_id("md-option-5")

		# select by visible text
		select_eds.select_by_visible_text("EDS")
		
		select_eds.save_screenshot('ETM_select_eds.png')


# create a test support service via etm


	# def tearDown(self):
	# 		# Close the browser.
	# 		# Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
	#
	# 		if (self.driver != None):
	# 			print("--------------------------------")
	# 			self.driver.close()
	# 			self.driver.quit()

if __name__ == "__main__":
	unittest.main()#(verbosity=2)[/python]

