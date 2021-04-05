from selenium import webdriver
from selenium.webdriver.chrome import options
from time import sleep

Chrome_Options= webdriver.ChromeOptions()
Chrome_Options.add_experimental_option("prefs",{"download.default_directory":'C:/Drivers'})

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe",chrome_options=Chrome_Options)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.find_element_by_xpath("//*[@id='textbox']").send_keys("Testing filedownload")
driver.find_element_by_xpath("//*[@id='createTxt']").click()
driver.find_element_by_id("link-to-download").click()


driver.find_element_by_id("pdfbox").send_keys("Testing file pdf download")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

#driver.close()