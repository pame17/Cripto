from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Chrome()
letras = string.ascii_lowercase
driver.get("https://elitecenter.cl/my-account/?action=register")
user = driver.find_element_by_id("reg_username")
user.clear()
user.send_keys("Nombre Prueba")
email = driver.find_element_by_id("reg_email")
email.send_keys("prueba@correo.cl")
password = driver.find_element_by_id("reg_password")
password.clear()
clave = ''.join(random.choice(letras) for i in range(12))
password.send_keys(clave)

click = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/article/div/div/div[2]/div/div[2]/form/p[4]/button").click()