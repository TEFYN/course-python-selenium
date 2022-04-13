import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service  # para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager  # para levantar el browser 2


# import pdb

class InvalidUserLoginError(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://demostore.supersqa.com/my-account/")
        cls.driver.maximize_window()
        # pdb.set_trace()

    def test_input_email(self):
        field = self.driver.find_element(By.ID, 'username')
        invalid_email = 'abd@supersqa.com'
        field.send_keys(invalid_email)

    def test_input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys('abcdefge')

    def test_click_login(self):
        self.driver.find_element(By.NAME, 'login').click()
        time.sleep(20)

    def test_verify_error_message(self):
        field = self.driver.find_element(By.ID, 'username')
        invalid_email = 'abd@supersqa.com'
        field.send_keys(invalid_email)

        field = self.driver.find_element(By.ID, 'password')
        field.send_keys('abcdefge')

        self.driver.find_element(By.NAME, 'login').click()
        error_element = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
        displayed_err = error_element.text
        expected_msg = 'Unknown email address. Check again or try your username.'
        assert displayed_err == expected_msg, "The displayed error is not expected."
        print('PASS')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
