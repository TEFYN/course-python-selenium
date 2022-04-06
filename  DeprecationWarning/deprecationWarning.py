#from webdriver_manager.chrome import ChromeDriverManager #identifica la versión del driver y lo levanta
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#esto da el mensaje:
# "DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())"
#La solucion es:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://demostore.supersqa.com')


cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()
driver.back()
cart.click()
driver.back()
driver.quit()


