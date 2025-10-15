from appium import webdriver
from time import sleep
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.calculator2",
    "appActivity": ".Calculator",
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

def mobile_calculator_test():
    driver.find_element("id", "com.android.calculator2:id/digit_2").click()
    driver.find_element("id", "com.android.calculator2:id/op_add").click()
    driver.find_element("id", "com.android.calculator2:id/digit_3").click()
    driver.find_element("id", "com.android.calculator2:id/eq").click()

    sleep(1)
    result = driver.find_element("id", "com.android.calculator2:id/result").text

    assert result == "5"

    driver.quit()
