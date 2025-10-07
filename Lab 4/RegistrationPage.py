from BasePage import *

class RegistrationPage(BasePage):
    NAME_FIELD = (By.ID, "register_name_form")
    PHONE_FIELD = (By.ID, "register_phone_form")
    PASSWORD_FIELD = (By.ID, "register_password_form")
    OK_BUTTON = (By.ID, "login_ok")

    def fill_form(self, name, phone, password):
        self.type(*self.NAME_FIELD, name)
        self.type(*self.PHONE_FIELD, phone)
        self.type(*self.PASSWORD_FIELD, password)

    def submit(self):
        self.click(*self.OK_BUTTON)
