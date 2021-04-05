#HTTP cookie = browser cookie, internet Cookie, web Cookie
# capture all cookie, count,
# add, delete,
# read cooke, delete all


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.in/")
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

Cookie1 = {'name':'MyCookie','value':'234234'}
driver.add_cookie(Cookie1)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_cookie('MyCookie')
cookies = driver.get_cookies()
print(len(cookies))

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))

driver.close()


