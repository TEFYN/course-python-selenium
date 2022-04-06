from selenium import webdriver
import time

#Option1
#ESTA ES OTRA FORMA, TE LO INSTALA SOLO
#from webdriver_manager.chrome import ChromeDriverManager #identifica la versión del driver y lo levanta
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#esto da el mensaje: 
# "DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())"
#La solucion es:


#Option2
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


#Option3
#ESTA ES OTRA FORMA: PERO ADEMAS HAY QUE DESCARGAR LA VERSION DE CHROMEDRIVER  GUARDARLA EN ALGUNA CARPETA Y AGREGAR LA RUTA EN LAS VARIABLES DE ENTORNO"
# from selenium import webdriver
# driver = webdriver.Chrome()



driver.get('http://demostore.supersqa.com')
time.sleep(2)
driver.quit()

#
# driver = webdriver.Firefox()
# driver.get('http://demostore.supersqa.com')