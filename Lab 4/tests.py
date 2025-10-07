from random import randint
from RegistrationPage import *

def test_positive_register_form():
    page = RegistrationPage()
    page.open("register")

    page.fill_form('Name', randint(1, 1000), randint(1, 1000))
    page.submit()

    assert page.find_with_wait(By.ID, 'personal_page')

    page.close()

def test_negative_register_form():
    page = RegistrationPage()
    page.open("register")

    page.fill_form('', '', '')
    page.submit()

    assert "Field must be not empty" in page.get_error_message()

    page.close()
