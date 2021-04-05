# Hover # single click
#double click # drag drop

from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
element1 = driver.find_element_by_xpath("//*[@id='box1']")
element2 = driver.find_element_by_xpath("//*[@id='box2']")
element3 = driver.find_element_by_xpath("//*[@id='box3']")
element4 = driver.find_element_by_xpath("//*[@id='box4']")
element5 = driver.find_element_by_xpath("//*[@id='box5']")
element6 = driver.find_element_by_xpath("//*[@id='box6']")
element7 = driver.find_element_by_xpath("//*[@id='box7']")

target1 = driver.find_element_by_xpath("//*[@id='box101']")
target2 = driver.find_element_by_xpath("//*[@id='box102']")
target3 = driver.find_element_by_xpath("//*[@id='box103']")
target4 = driver.find_element_by_xpath("//*[@id='box104']")
target5 = driver.find_element_by_xpath("//*[@id='box105']")
target6 = driver.find_element_by_xpath("//*[@id='box106']")
target7 = driver.find_element_by_xpath("//*[@id='box107']")


actions = ActionChains(driver)
actions.drag_and_drop(element1,target1).perform()
actions.drag_and_drop(element2,target2).perform()
actions.drag_and_drop(element3,target3).perform()
actions.drag_and_drop(element4,target4).perform()
actions.drag_and_drop(element5,target5).perform()
actions.drag_and_drop(element6,target6).perform()
actions.drag_and_drop(element7,target7).perform()


sleep(10)
driver.close()