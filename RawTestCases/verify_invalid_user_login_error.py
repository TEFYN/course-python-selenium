import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2



class InvalidUserLoginError:

    invalid_email = 'abd@supersqa.com'
    url = "http://demostore.supersqa.com/my-account/"
    expected_msg = 'Unknown email address. Check again or try your username.'

    def __init__(self): #constructor
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)


    def input_email(self):
        field = self.driver.find_element(By.ID, 'username')
        field.send_keys(self.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys('abcdefge')

    def click_login(self):
        self.driver.find_element(By.NAME, 'login').click()


    def verify_error_message(self):
        error_element = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
        displayed_err = error_element.text
        assert displayed_err == self.expected_msg , "The displayed error is not expected."
        print('PASS')

    def quit(self):
        self.driver.quit()

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_message()
        self.quit()

if __name__ == '__main__':

    obj = InvalidUserLoginError()
    obj.main()