from random import randint
from time import sleep
from selenium.common import NoSuchElementException
from webdriver import *
from selenium.webdriver.common.by import By

driver = get_driver("http://localhost:5173/")

register = driver.find_element(By.ID, "register_navigation")
register.click()

name_form = driver.find_element(By.ID, 'register_name_form')
name_form.send_keys('Name')

phone_form = driver.find_element(By.ID, 'register_phone_form')
phone_form.send_keys(randint(1, 1000))

password_form = driver.find_element(By.ID, 'register_password_form')
password_form.send_keys(randint(1, 1000))

login = driver.find_element(By.ID, 'login_ok')
login.click()

is_correct = True
sleep(1)
try:
    driver.find_element(By.ID, 'personal_page')
except NoSuchElementException:
    is_correct = False

assert is_correct == True

close()

