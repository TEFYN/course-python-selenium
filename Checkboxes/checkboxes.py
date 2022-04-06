from selenium import webdriver

from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://materializecss.com/checkboxes.html')

checkbox = driver.find_element(By.CSS_SELECTOR)
checkbox
