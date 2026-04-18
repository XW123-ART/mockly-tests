"""
登录页面操作封装
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    """登录页面对象"""
    url = "/login"

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_btn = (By.CSS_SELECTOR, ".login-btn")
    error_msg = (By.CLASS_NAME, "error-msg")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def open(self):
        super().open(self.url)
        time.sleep(1)

    def input_username(self, username):
        self.input_text(*self.username_input, username)

    def input_password(self, password):
        self.input_text(*self.password_input, password)

    def click_login_button(self):
        self.click(*self.login_btn)
        time.sleep(2)

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    def get_error_message(self):
        if self.is_element_exist(*self.error_msg):
            return self.get_text(*self.error_msg)
        return None

    def is_on_login_page(self):
        return "/login" in self.get_current_url()

    def is_login_success(self):
        return "/generator" in self.get_current_url()
