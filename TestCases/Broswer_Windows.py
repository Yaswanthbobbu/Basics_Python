from selenium import webdriver
from selenium.webdriver.common import by
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)
handles =  driver.window_handles

for handle in handles:
     driver.switch_to.window(handle)
     print(driver.title)
if driver.title== "Frames & windows":
   driver.close()

