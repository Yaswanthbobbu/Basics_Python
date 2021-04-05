#locate all the elements of locators and action methods

class LoginPage1():
      textbox_username_id = "Email"
      textbox_password_id = "Password"
      button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
      link_login_Text = "welcome"
      link_logout_text =  "Logout"

#to initilize driver we need to create one constructor

      def __init__(self,driver):
          self.driver=driver

      def setUserName(self,username):
          self.driver.find_element_by_id(self.textbox_username_id).clear()
          self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

      def setPassword(self,password):
          self.driver.find_element_by_id(self.textbox_password_id).clear()
          self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

      def clicklogin(self):
          self.driver.find_element_by_xpath(self.button_login_xpath).click()

      def clicklogout(self):
          self.driver.find_element_by_xpath(self.link_logout_text).click()