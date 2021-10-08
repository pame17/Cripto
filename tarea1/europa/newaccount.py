from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Chrome()
letras = string.ascii_lowercase
driver.get("https://www.todobajos.com/es/iniciar-sesion?back=my-account")
click = driver.find_element_by_xpath("//*[@id='SubmitCreate']").click()
nombre = driver.find_element_by_css_selector("div.col-lg-12:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
nombre.clear()
nombre.send_keys("Nombres")
apellido = driver.find_element_by_css_selector("div.col-lg-12:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
apellido.clear()
apellido.send_keys("Apellidos")
email = driver.find_element_by_css_selector("div.col-lg-12:nth-child(4) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
email.send_keys("tacim73047@mxgsby.com")
password = driver.find_element_by_css_selector(".js-visible-password")
password.clear()
clave = ''.join(random.choice(letras) for i in range(12))
password.send_keys(clave)
print("La contraseña es: ", clave)
button = driver.find_element_by_xpath("//*[@id='customer-form']/footer/button")
driver.execute_script("arguments[0].click();", button)
