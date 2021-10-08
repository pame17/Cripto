from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Chrome()
letras = string.ascii_lowercase

driver.get("https://elitecenter.cl/my-account/")
user = driver.find_element_by_id("username")
user.clear()
user.send_keys("Nombre")
password = driver.find_element_by_id("password")
password.clear()
password.send_keys("mtazpdhrrtbj")
click = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/article/div/div/div[2]/div/div[1]/form/p[3]/button").click()

driver.get("https://elitecenter.cl/my-account/edit-account/")
password_current = driver.find_element_by_id("password_current")
password_current.clear()
password_current.send_keys("mtazpdhrrtbj")
new_password1 = driver.find_element_by_id("password_1")
new_password1.clear()
new_password2 = driver.find_element_by_id("password_2")
new_password2.clear()
clave = ''.join(random.choice(letras) for i in range(12))
new_password1.send_keys(clave)
new_password2.send_keys(clave)
print("La contraseña es: ", clave)
click = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/article/div/div/div/div[2]/form/p[5]/button").click()