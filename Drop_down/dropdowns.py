import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()


driver.get('C:\\tefy\course-python-selenium\Drop_down\dropdown.html')

dropdown = driver.find_element(By.ID, 'estudios')
dropdown_obj = Select(dropdown)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)
import pdb
dropdown_obj.select_by_index(0)
time.sleep(1)
dropdown_obj.select_by_index(1)
time.sleep(1)
dropdown_obj.select_by_index(2)
time.sleep(1)
dropdown_obj.select_by_index(3)
time.sleep(1)
dropdown_obj.select_by_value('primaria')
time.sleep(1)


all_options = dropdown_obj.options
for opc in all_options:
    print('text: ' + opc.text)
    print('value: ' + opc.get_attribute('value'))


time.sleep(3)

#python_id = driver.find_element(By.CSS_SELECTOR, 'body > form > p:nth-child(46) > input[type=checkbox]:nth-child(8)')
#<input type="checkbox" name="conocimientos" value="Python"> " Python "
# <input type="checkbox" name="conocimientos" value="Javascript"> " Javascript "
driver.find_element(By.CSS_SELECTOR, 'input[name="conocimientos"][value="Python"]').click()

time.sleep(1)
pyId = driver.find_element(By.CSS_SELECTOR, 'input[value="Javascript"]')
print(f"{pyId.get_attribute('value')}: is selected: {pyId.is_selected()}, is enabled: {pyId.is_enabled()}" )
pyId.click()
print(f"{pyId.get_attribute('value')}: is selected: {pyId.is_selected()}, is enabled: {pyId.is_enabled()}" )
time.sleep(3)

myChoice = driver.find_elements(By.CSS_SELECTOR, 'input[name="conocimientos"]') #todos los elementos imput

print("\n\n")
for choice in myChoice:
    if choice.is_selected():
        print(f"*******is selectable: {choice.get_attribute('value')}")
    else:
        print(f"***is not selectable: {choice.get_attribute('value')}")






driver.get('https://ventadecasasydepartamentos.netlify.app/')

time.sleep(3)
#contacto = driver.find_element(By.CSS_SELECTOR, 'body > header > div > div > nav > a:nth-child(4)')
contacto = driver.find_element(By.CSS_SELECTOR, 'a[href="Contactos.html"]')

contacto.click()
time.sleep(3)



#scroll hasta un elemento en particular, agregar import ActionChains
element = driver.find_element(By.ID, "fecha")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

my_dropdown = driver.find_element(By.ID, 'opciones')
my_dropdown.click()
# import pdb; pdb.set_trace()
dropdown_object = Select(my_dropdown)
dropdown_object.select_by_index(1)
# pdb.set_trace()
time.sleep(2)


all_options = dropdown_object.options
print('\n\n')
for opc in all_options:
    print(f"{opc.text}: is selected: {opc.is_selected()}, is enabled: {opc.is_enabled()}")

# pdb.set_trace()
time.sleep(3)

driver.quit()