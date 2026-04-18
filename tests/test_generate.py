"""
数据生成功能测试
"""
import pytest
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.generator_page import GeneratorPage


def load_generate_data():
    """加载测试数据"""
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'generate_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['test_cases']


def login(driver, base_url):
    """登录辅助函数"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login("admin", "123456")


class TestDataGenerate:
    """测试数据生成功能"""

    @pytest.mark.parametrize("test_data", load_generate_data(), ids=lambda x: x['name'])
    def test_generate_data(self, driver, base_url, test_data):
        login(driver, base_url)

        generator_page = GeneratorPage(driver, base_url)
        if not generator_page.is_on_generator_page():
            generator_page.open()

        schema_json = json.dumps(test_data['schema'], ensure_ascii=False, indent=2)
        generator_page.generate_data(schema_json, test_data['count'])

        result = generator_page.get_result_text()
        assert result is not None, "没有生成结果"
