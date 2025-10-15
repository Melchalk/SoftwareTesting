from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

def get_driver(path: str):
    driver.get(path)
    return driver

def close():
    driver.close()