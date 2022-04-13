import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager  # para levantar el browser 2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class VerifyFreeCode(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get('http://demostore.supersqa.com/')
        self.driver.maximize_window()

    def test_check_free_coupon(self):
        self.driver.find_element(By.CLASS_NAME,
                                 'add_to_cart_button').click()  # solo vamos a hacer click en el PRIMER ELEMENT
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[2]'),
                                                         '1 item'))  # cuando ya se agregó el producto

        self.driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a').click()

        coupon_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'coupon_code')))
        coupon_field.send_keys('SSQA100')
        coupon_field.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[3]/td/strong/span/bdi'), '$0.00'))
        print('PASS')

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
