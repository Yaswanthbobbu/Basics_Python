#from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.support.ui import WebDriverWait
#import config


from selenium import webdriver
from selenium.webdriver.common import By
from selenium.webdriver.common import keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome(executable_path="c:\Drivers\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath() # flight button
time.sleep(5)
driver.find_element_by_id().clear()
driver.find_element_by_id().send_keys("SFO")# source
driver.find_element_by_id().clear()
driver.find_element_by_id().send_keys("NYK")  # destination
driver.find_element_by_id().clear()
driver.find_element_by_id().clear() #to date
driver.find_element_by_id().clear()
driver.find_element_by_id().clear() # from date

time.sleep(2)

driver.find_element_by_xpath().click() #click search button

#Explicit conditions
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable(By.Xpath))

element.click()
driver.close()






driver.close()