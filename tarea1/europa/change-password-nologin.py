from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string

driver = webdriver.Chrome()
letras = string.ascii_lowercase
driver.get("https://www.todobajos.com/es/recuperar-contraseña")
email = driver.find_element_by_id("email")
email.clear()
email.send_keys("reseso6861@soulsuns.com")
click = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/main/section/div/div/div/section/section/div/section/div/div/form/footer/button").click()

#Proceso intermedio donde se consigue el URL desde el correo...
token = ""
id_customer = ""
reset_token = ""
driver.get("https://www.todobajos.com/es/recuperar-contraseña?token="+token+"&id_customer="+id_customer+"reset_token="+reset_token)
new_password1 = driver.find_element_by_xpath("//[@id='content']/form/section/div[2]/div[1]/div/input")
new_password1.clear()
new_password2 = driver.find_element_by_xpath("//[@id='content']/form/section/div[2]/div[2]/div/input")
new_password2.clear()
clave = ''.join(random.choice(letras) for i in range(5))
print("La contraseña es: ", clave)
new_password1.send_keys(clave)
new_password2.send_keys(clave)
click = driver.find_element_by_xpath("//[@id='content']/form/section/div[2]/div[3]/div/button").click()