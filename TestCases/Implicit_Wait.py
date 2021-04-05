#Synchronisation error : Balancing between code execution and response of the application
#we have to specify implicit only once in the program
#Explicit is based on condition
#Implicit is based on the time given

from selenium import webdriver
# from selenium.webdriver.common import keys
import time
driver = webdriver.Chrome(executable_path="c:\Drivers\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5) #applicable for all the elements of the page
assert "google" in driver.title
#time.sleep(5)
print(driver.title)
driver.close()