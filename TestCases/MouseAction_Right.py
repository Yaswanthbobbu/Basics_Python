# Hover # single click
#double click # drag drop

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
element = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)
actions.context_click(element).perform()

sleep(4)
driver.close()