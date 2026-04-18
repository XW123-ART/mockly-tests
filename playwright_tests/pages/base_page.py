"""
Playwright 页面对象基类，封装常用操作
"""
from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.timeout = 10000

    def open(self, url: str):
        full_url = self.base_url + url
        self.page.goto(full_url)
        self.page.wait_for_load_state("networkidle")

    def find_element(self, selector: str):
        return self.page.locator(selector)

    def find_elements(self, selector: str):
        return self.page.locator(selector).all()

    def wait_for_element(self, selector: str):
        element = self.page.locator(selector)
        element.wait_for(timeout=self.timeout)
        return element

    def click(self, selector: str):
        self.page.locator(selector).click()

    def input_text(self, selector: str, text: str):
        element = self.page.locator(selector)
        element.clear()
        element.fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def get_current_url(self) -> str:
        return self.page.url

    def is_element_exist(self, selector: str) -> bool:
        try:
            count = self.page.locator(selector).count()
            return count > 0
        except:
            return False

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"screenshots/{name}.png")
