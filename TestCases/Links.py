#how many links in website
#capture all the links in webpage
#click option on link

from selenium import webdriver
from selenium.webdriver.common import by
import time

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

links = driver.find_elements_by_tag_name("a")
print("No. of links in the page:", len(links))

for option in links :
    print(option.text)

driver.find_element_by_link_text("REGISTER").click()

driver.close()
