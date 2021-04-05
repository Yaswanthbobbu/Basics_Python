from selenium import webdriver
from selenium.webdriver.common import by
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")
driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users/bobbu.yaswanth/Desktop/BAU/Screenshot.png")

#driver.close()