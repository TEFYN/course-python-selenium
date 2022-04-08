import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()
driver.get('C:\\tefy\course-python-selenium\Alerts\\alerts_example.html')
time.sleep(2)


driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-info').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'button[class="btn-close"]').click()
time.sleep(3)



driver.find_element(By.CSS_SELECTOR, 'div#jsAlertExample button').click()
time.sleep(3)
myAlert = driver.switch_to.alert
print(myAlert.text)
assert myAlert.text == 'I am a JavaScript Alert', "Unexpected text on alert."
myAlert.accept()
time.sleep(3)


confirmAlert = driver.find_element(By.CSS_SELECTOR, 'div#jsConfirmExample button')
confirmAlert.click()
time.sleep(3)

driver.switch_to.alert.dismiss()
time.sleep(3)
confirmAlert.click()
time.sleep(3)


driver.switch_to.alert.accept()
time.sleep(3)
prompt = driver.find_element(By.CSS_SELECTOR, 'div#jsPromptExample button')
prompt.click()

driver.switch_to.alert.send_keys('Python-Selenium')
driver.switch_to.alert.accept()
time.sleep(3)


driver.quit()
