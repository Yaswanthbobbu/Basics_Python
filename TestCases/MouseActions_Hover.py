# Hover # single click
#double click # drag drop

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

Admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
UserMang = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
actions.move_to_element(Admin).move_to_element(UserMang).move_to_element(user).click().perform()


driver.close()