import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()
driver.get('C:\\tefy\course-python-selenium\iFrames\iFrames_example.html')
time.sleep(2)

driver.find_element(By.ID, 'btnOutFrame').click()
time.sleep(2)
my_alert = driver.switch_to.alert

my_alert_text = my_alert.text
assert my_alert_text == 'Just Clicked Outside iFrame', "Should've gotten outside message"
print(my_alert_text)
my_alert.accept()
time.sleep(2)

#driver.switch_to.frame(driver.find_element(By.ID, 'myFrame1')) #foco en iframe
driver.switch_to.frame('myFrame1') #foco en iframe
driver.find_element(By.ID, 'btnInFrame').click()#click en un alert
time.sleep(2)
my_alert_text2 = driver.switch_to.alert.text
assert my_alert_text2 == 'Just Clicked Inside iFrame', "Should've gotten inside message"
print(driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.switch_to.default_content()


driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

#driver.switch_to.frame(driver.find_element(By.ID, 'myFrame2'))
driver.switch_to.frame('myFrame2')

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="product-33"]/div[1]/a').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button[class="pswp__button pswp__button--close"]').send_keys(Keys.ESCAPE)
time.sleep(2)
#scroll hasta un elemento en particular, agregar import ActionChains
element = driver.find_element(By.CSS_SELECTOR, 'span[class="posted_in"]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()


time.sleep(2)
#import pdb; pdb.set_trace()
driver.quit()






