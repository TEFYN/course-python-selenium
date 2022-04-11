# import pdb
import time

from selenium import webdriver


from selenium.webdriver.chrome.service import Service  #para levantar el browser 1
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #para levantar el browser 2
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()
driver.get('C:\\tefy\course-python-selenium\Multiple_Windows_and_tabs\windows-and_tabs_example.html')

driver.find_element(By.XPATH, '//*[@id="windows"]/a[1]').click()

original_window_handle = driver.current_window_handle
print(original_window_handle)

all_windows_handles = driver.window_handles
print(all_windows_handles)
new_window = all_windows_handles[1]
print(new_window)

print(f"Before switching focus: " + driver.title)
time.sleep(2)
driver.switch_to.window(new_window)
time.sleep(2)

print(f"After switching focus: " + driver.title)
my_headding = driver.find_element(By.XPATH, '/html/body/h1').text
print(my_headding)

time.sleep(2)
# pdb.set_trace()
driver.quit()