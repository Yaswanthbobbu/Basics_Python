from selenium import webdriver
from selenium.webdriver.common import by
from time import sleep

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com//")
driver.maximize_window()

rows = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))

print(rows)
print(cols)

for h in range(1,5):
    header = driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th["+str(h)+"]").text
    print(header)

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end= "   ")
    print()


driver.close()