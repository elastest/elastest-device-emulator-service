from selenium import webdriver

#from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
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

	def Test_job(self):
		#show the location of web driver locally
		self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
		self.driver.implicitly_wait(10)
		self.driver.set_page_load_timeout(30)
		#self.driver.get("http://elastest.io:37000")
		self.driver.get("http://elastest.io")
		self.driver.maximize_window()
		assert self.driver.title, 'Elastest Home'
		#		print(driver.title)

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

