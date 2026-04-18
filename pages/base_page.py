"""
页面对象基类，封装 Selenium 常用操作
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    """所有页面对象的基类"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 10

    def open(self, url):
        full_url = self.base_url + url
        self.driver.get(full_url)
        time.sleep(1)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def wait_for_element(self, by, value):
        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    def wait_for_clickable(self, by, value):
        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(EC.element_to_be_clickable((by, value)))

    def click(self, by, value):
        element = self.wait_for_clickable(by, value)
        element.click()

    def input_text(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        element = self.wait_for_element(by, value)
        return element.text

    def get_current_url(self):
        return self.driver.current_url

    def is_element_exist(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except:
            return False
