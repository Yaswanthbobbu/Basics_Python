#switch_to_Frame(id)(name)

from selenium import webdriver
from selenium.webdriver.common import by
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.devtools").click()
sleep(2)

driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("DevToolsException").click()
sleep(2)


driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
sleep(2)

driver.close()