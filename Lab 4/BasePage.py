from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage:
    ERROR_MESSAGE = (By.ID, "error_message")

    def __init__(self):
        self.base_url = "http://localhost:5173/"
        self.web_driver = webdriver.Chrome(options=Options())

    def get_driver(self):
        return self.web_driver

    def close(self):
        return self.web_driver.close()

    def open(self, url):
        self.web_driver.get(self.base_url + url)

    def find(self, by, locator):
        return self.web_driver.find_element(by, locator)

    def click(self, by, locator):
        self.find(by, locator).click()

    def type(self, by, locator, text):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)

    def find_with_wait(self, by, locator):
        element = WebDriverWait(self.web_driver, 10).until(
            EC.visibility_of_element_located((by, locator)))

        return element

    def get_error_message(self):
        toast = self.find_with_wait(*self.ERROR_MESSAGE)

        return toast.text