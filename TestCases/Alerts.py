from selenium import webdriver
from selenium.webdriver.common import by
import time

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com//")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)

#driver. switch_to_alert().accept()
driver.switch_to_alert().dismiss()
time.sleep(2)

driver.close()