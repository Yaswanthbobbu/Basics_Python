#select dropdown option
#count options
#captureoptions

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

drp.select_by_index(2)
#drp.select_by_value("Radio-1")
#drp.select_by_visible_text("Afternoon")

print(len(drp.options))

all_options = drp.options

for option in all_options :
    print(option.text)


driver.close()