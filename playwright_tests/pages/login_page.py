"""
Playwright 版本登录页面操作封装
"""
from playwright.sync_api import Page
from playwright_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    url = "/login"

    username_input = "input[name='username']"
    password_input = "input[name='password']"
    login_btn = ".login-btn"
    error_msg = ".error-msg"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    def open(self):
        super().open(self.url)

    def input_username(self, username: str):
        self.input_text(self.username_input, username)

    def input_password(self, password: str):
        self.input_text(self.password_input, password)

    def click_login_button(self):
        self.click(self.login_btn)

    def login(self, username: str, password: str):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    def get_error_message(self) -> str:
        if self.is_element_exist(self.error_msg):
            return self.get_text(self.error_msg)
        return None

    def is_on_login_page(self) -> bool:
        return "/login" in self.get_current_url()

    def is_login_success(self) -> bool:
        return "/generator" in self.get_current_url()

    def get_page_title(self) -> str:
        return self.page.title()

    def is_submit_button_enabled(self) -> bool:
        return self.page.locator(self.login_btn).is_enabled()
