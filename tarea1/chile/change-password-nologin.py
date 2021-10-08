from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Chrome()
letras = string.ascii_lowercase
driver.get("https://elitecenter.cl/my-account/lost-password/")
user = driver.find_element_by_id("user_login")
user.clear()
user.send_keys("Nombre")
click = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/article/div/div/form/p[3]/button").click()

#Proceso intermedio donde se consigue el URL desde el correo...

driver.get("https://elitecenter.cl/my-account/lost-password/?show-reset-form=true&action")
new_password1 = driver.find_element_by_id("password_1")
new_password1.clear()
new_password2 = driver.find_element_by_id("password_2")
new_password2.clear()
clave = ''.join(random.choice(letras) for i in range(12))
print("La contraseña es: ", clave)
new_password1.send_keys(clave)
new_password2.send_keys(clave)
click = driver.find_element_by_xpath("//*[@id='post-10']/div/div/form/p[4]/button").click()