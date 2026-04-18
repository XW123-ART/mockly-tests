"""
OpenAPI 文件上传功能测试
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


class TestOpenapiUpload:
    """测试 OpenAPI 文件上传"""

    def test_upload_openapi_file(self, driver, base_url):
        login(driver, base_url)

        generator_page = GeneratorPage(driver, base_url)
        if not generator_page.is_on_generator_page():
            generator_page.open()

        generator_page.switch_to_openapi_source()

        test_file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'data',
            'test_openapi.json'
        )
        generator_page.upload_openapi_file(test_file_path)
        generator_page.set_count(2)
        generator_page.click_submit()

        result = generator_page.get_result_text()
        assert result is not None, "没有生成结果"
