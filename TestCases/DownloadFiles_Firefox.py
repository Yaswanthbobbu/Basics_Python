from selenium import webdriver
from time import sleep
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf") #mime type
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","C:/Users/bobbu.yaswanth/")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)

driver = webdriver.Firefox(executable_path ="C:\Drivers\geckodriver.exe",firefox_profile=fp)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.find_element_by_xpath("//*[@id='textbox']").send_keys("Testing filedownload")
driver.find_element_by_xpath("//*[@id='createTxt']").click()
driver.find_element_by_xpath("//*[@id='link-to-download']").click()


driver.find_element_by_id("pdfbox").send_keys("Testing file pdf download")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_xpath("//*[@id='pdf-link-to-download']").click()

#driver.close()