# run python TestCases/LoginTest.py

import unittest
import HtmlTestRunner
from selenium import webdriver
from time import sleep
import sys
sys.path.append("C://Users/bobbu.yaswanth/PycharmProjects/Basics")
from PageObjects.LoginPage import LoginPage1

class LoginTest1(unittest.TestCase):
    BaseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="C://Users/bobbu.yaswanth/PycharmProjects/Basics/drivers/chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.BaseURL)
        cls.driver.maximize_window()

    def test_login1(self):
        lp = LoginPage1(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clicklogin()
        sleep(4)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"Webpage title is not matched")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users/bobbu.yaswanth/PycharmProjects/Basics/Reports"))
