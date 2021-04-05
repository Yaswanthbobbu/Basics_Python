# Hover # single click
#double click # drag drop

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")
element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")


actions = ActionChains(driver)
actions.double_click(element).perform()
sleep(4)

driver.close()