import logging.config
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.ui import WebDriverWait #Explicit waits (implicit waits dont need to import anything
from selenium.webdriver.support import expected_conditions as EC

#
from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()
driver.get('http://demostore.supersqa.com/my-account/')



# --------INICIA SESION


driver.find_element(By.ID, 'username').send_keys('username')#escribe otro usuario
driver.find_element(By.ID, 'password').send_keys('password')
login = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
login.click()
time.sleep(3)

driver.find_element(By.ID, 'username').clear()
driver.find_element(By.ID, 'username').send_keys('backup.alaniz@gmail.com')#escribe otro usuario
driver.find_element(By.ID, 'password').send_keys('Tefy123!!')
driver.save_screenshot('C:\\Users\\QA-User64\\Desktop\\screeshots\\login.png')
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button').click()
#WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button'))).click()
#login.click()
# driver.save_screenshot('C:\\Users\\QA-User64\\Desktop\\screeshots\\MyAccount.png')
time.sleep(2)

# --------CIERRA SESION
logout = driver.find_element(By.CSS_SELECTOR, '#post-9 > div > div > div > p:nth-child(2) > a')
logout.click()
time.sleep(4)
driver.back()

search_field = driver.find_element(By.ID,"woocommerce-product-search-field-0")
search_field.send_keys("hoodie")
search_field.send_keys(Keys.ENTER)
time.sleep(3)


driver.get('http://demostore.supersqa.com/my-account/')

field = driver.find_element(By.ID, 'username')
field.send_keys('backup.alaniz@gmail.com')
time.sleep(2)
field.send_keys(Keys.TAB)
time.sleep(2)
field = driver.find_element(By.ID, 'password')
field.send_keys('Tefy123!!')
time.sleep(1)
field.send_keys(Keys.TAB)  #es un chjeckbox
field = driver.find_element(By.ID, 'rememberme')
field.click()
time.sleep(2)
field.send_keys(Keys.TAB)
time.sleep(1)
login = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
login.click()
time.sleep(2)


time.sleep(3)


driver.quit()


