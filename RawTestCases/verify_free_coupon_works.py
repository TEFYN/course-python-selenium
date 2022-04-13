

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def add_1_item_to_cart():
    driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click() #solo vamos a hacer click en el PRIMER ELEMENT
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[2]'), '1 item') #cuando ya se agregó el producto
    )

def click_cart_in_top_menu(): #demora unos segundos en actualizar el carrito por eso usamos un wait antes
    driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a').click()

def input_coupon_and_hit_enter(coupon_code):
    coupon_field = wait.until(EC.visibility_of_element_located((By.ID, 'coupon_code')))
    #coupon_field = driver.find_element(By.ID, 'coupon_code')
    #coupon_field.send_keys('SSQA100')
    coupon_field.send_keys(coupon_code)
    coupon_field.send_keys(Keys.ENTER)

def verify_total_is_0():
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[3]/td/strong/span/bdi'), '$0.00'))


if __name__ == '__main__':
    coupon_code = 'SSQA100'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10) #explicit wait
    driver.get('http://demostore.supersqa.com/')

    add_1_item_to_cart()
    click_cart_in_top_menu()
    input_coupon_and_hit_enter(coupon_code)
    verify_total_is_0()
    print('PASS')
    driver.quit()

