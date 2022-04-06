import pdb
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2

from selenium.webdriver.common.by import By #find_element
import time #sleep
from selenium.webdriver.support.ui import WebDriverWait #Explicit waits (implicit waits no need to import anything
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()
driver.get('http://demostore.supersqa.com')
driver.save_screenshot('C:\\Users\\QA-User64\\Desktop\\screeshots\\Home.png')


#DISTINTAS FORMAS DE ENCONTRAR UN ELEMENTO
#cart = driver.find_element_by_id("site-header-cart")
#cart = driver.find_element("id", 'site-header-cart')


#solo cuando utilizo este metodo NECESITO importar from selenium.webdriver.common.by import By
driver.find_element(By.ID, 'site-header-cart').click()
#time.sleep(2)
driver.back()
#time.sleep(3)
driver.find_element(By.ID, 'site-header-cart').click()
driver.back()
#time.sleep(3)



WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'site-header-cart')))
driver.find_element(By.ID, 'site-header-cart').click()
driver.back()
(WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'site-header-cart')))).click()

driver.back()




driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a').click()#clic en MyAccount
#time.sleep(5)
driver.find_element(By.ID, 'username').send_keys('kbasdld')#escribe un usuario
time.sleep(1)
driver.find_element(By.ID, 'username').clear() #limpiar un campo
time.sleep(3)

# --------INICIA SESION

driver.find_element(By.ID, 'username').send_keys('backup.alaniz@gmail.com')#escribe otro usuario
driver.find_element(By.ID, 'password').send_keys('Tefy123!!')
driver.save_screenshot('C:\\Users\\QA-User64\\Desktop\\screeshots\\login.png')
login = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
login.click()
driver.save_screenshot('C:\\Users\\QA-User64\\Desktop\\screeshots\\MyAccount.png')
time.sleep(4)



# --------CIERRA SESION

logout = driver.find_element(By.CSS_SELECTOR, '#post-9 > div > div > div > p:nth-child(2) > a')
logout.click()



driver.back()
driver.back()
driver.find_element(By.CSS_SELECTOR, '#site-header-cart').click() #clic carrito
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a').click() #clilc MyAccount
time.sleep(4)

#demoget atributte

search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
#pdb.set_trace()

place_holder = search_field.get_attribute('placeholder')
if place_holder != "Search products…":
    raise Exception(f"Place holder for search field is not as expected. Actual: {place_holder}")
else:
    print("PASS")

nav_items = driver.find_elements(By.CSS_SELECTOR, 'ul.nav-menu li')
for item in nav_items:
    item_class = item.get_attribute('class')
    print(item_class)
    if 'current_page_item' in item_class:
        print(f"The selected tab is: {item.text}")

#site-navigation > div:nth-child(2) > ul
# driver.find_element(By.CSS_SELECTOR, '#main > ul > li.product.type-product.post-24.status-publish.first.instock.product_cat-music.has-post-thumbnail.downloadable.virtual.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
# time.sleep(5)

driver.get('http://demostore.supersqa.com')
image = driver.find_element(By.CSS_SELECTOR, 'li.product a')
print(f"the product's url is: {image.get_attribute('href')}")
image.click()
time.sleep(3)
driver.get('http://demostore.supersqa.com')


#XPATH no es recomendable porque puede cambiar, es mejor utilizar CSS_SELECTOR
driver.quit()
