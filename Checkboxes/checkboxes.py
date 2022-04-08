import time
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()
driver.get('C:\\tefy\course-python-selenium\Drop_down\dropdown.html')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)


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

print("\n\n")
for choice in myChoice:
    if choice.is_selected():
        choice.click()
    else:
        pass

time.sleep(2)

print("\n\n")
for choice in myChoice:
    choice.click()
time.sleep(2)

print("\n\n")
for choice in myChoice:
    choice.click()


#import pdb; pdb.set_trace()

time.sleep(3)

driver.quit()