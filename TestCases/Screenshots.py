#save_screenshot
#get_Screenshot_as_file

from selenium import webdriver

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.save_screenshot("C:/Users/bobbu.yaswanth/Desktop/page1.png")
driver.get_screenshot_as_file("C:/Users/bobbu.yaswanth/Desktop/page2.png")


driver.close()