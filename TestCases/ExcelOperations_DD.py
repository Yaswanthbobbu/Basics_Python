import XLUtility
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/index.php")

file = "/TestCases/OpenPyXl.xlsx"
rows = XLUtility.getrowcount(file, "sheet1")

for r in range(2,rows+1):
       username = XLUtility.readdata(file, "sheet1", r, 1)
       password = XLUtility.readdata(file, "sheet1", r, 2)

       driver.find_element_by_name("userName").send_keys(username)
       driver.find_element_by_name("password").send_keys(password)
       driver.find_element_by_name("submit").click()

       if driver.title== "Login: Mercury Tours":
           print("Testcase Passed")
           XLUtility.writedata(file, "sheet1", r, 3, "Test Passed")
       else:
           print("Testcase Failed")
           XLUtility.writedata(file, "sheet1", r, 3, "Test Failed")

       driver.find_element_by_link_text("Home").click()

driver.close()
