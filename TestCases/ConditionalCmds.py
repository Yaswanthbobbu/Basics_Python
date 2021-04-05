#is_displayed
#is_selected
#is_enabled


from selenium import webdriver
# from selenium.webdriver.common import keys
import time
driver = webdriver.Chrome(executable_path="c:\Drivers\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
searchbar = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
time.sleep(5)
print(searchbar.is_enabled())
print(searchbar.is_displayed())
driver.close()


