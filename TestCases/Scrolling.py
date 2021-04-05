# pixel,by element, endpage

from selenium import webdriver
from selenium.webdriver.common import by
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
#driver.execute_script("window.scrollBy(0,6000)","")
#2 flag = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div/div[79]/div")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
sleep(5)

driver.close()