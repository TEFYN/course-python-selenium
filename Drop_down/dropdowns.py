import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()
driver.get('https://ventadecasasydepartamentos.netlify.app/')
time.sleep(3)
contacto = driver.find_element(By.CSS_SELECTOR, 'body > header > div > div > nav > a:nth-child(4)')
contacto.click()
time.sleep(3)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")



#scroll hasta un elemento en particular, agregar import ActionChains
element = driver.find_element(By.CSS_SELECTOR, "body > main > form > fieldset:nth-child(3) > label:nth-child(5)")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

my_dropdown = driver.find_element(By.ID, 'opciones')
dropdown_object = Select(my_dropdown)

import pdb; pdb.set_trace()
time.sleep(3)

time.sleep(3)
driver.quit()