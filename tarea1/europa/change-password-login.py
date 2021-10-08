from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Chrome()
letras = string.ascii_lowercase

driver.get("https://www.todobajos.com/es/iniciar-sesion")
user = driver.find_element_by_css_selector("div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)")
user.clear()
user.send_keys("reseso6861@soulsuns.com")
password = driver.find_element_by_css_selector(".js-visible-password")
password.clear()
password.send_keys("didqc")
button = driver.find_element_by_xpath("//*[@id='SubmitLogin']")
driver.execute_script("arguments[0].click();", button)

driver.get("https://www.todobajos.com/es/datos-personales")
password_current = driver.find_element_by_css_selector("div.col-lg-6:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
password_current.clear()
password_current.send_keys("didqc")
new_password = driver.find_element_by_css_selector("div.col-lg-6:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
new_password.clear()
clave = ''.join(random.choice(letras) for i in range(5))
new_password.send_keys(clave)
print("La contraseña es: ",clave)
button = driver.find_element_by_xpath("//*[@id='customer-form']/footer/button")
driver.execute_script("arguments[0].click();", button)