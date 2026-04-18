"""
数据源切换功能测试（内联、文件、OpenAPI）
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.generator_page import GeneratorPage


def login(driver, base_url):
    """登录辅助函数"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login("admin", "123456")


class TestSourceSwitch:
    """测试数据源切换"""

    def test_switch_to_file_source(self, driver, base_url):
        login(driver, base_url)

        generator_page = GeneratorPage(driver, base_url)
        if not generator_page.is_on_generator_page():
            generator_page.open()

        generator_page.switch_to_file_source()
        assert generator_page.is_file_source_active()

    def test_switch_to_openapi_source(self, driver, base_url):
        login(driver, base_url)

        generator_page = GeneratorPage(driver, base_url)
        if not generator_page.is_on_generator_page():
            generator_page.open()

        generator_page.switch_to_openapi_source()
        assert generator_page.is_openapi_source_active()
