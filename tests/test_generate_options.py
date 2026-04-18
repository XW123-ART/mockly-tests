"""
数据生成选项功能测试（smart、mutate、report）
"""
import pytest
import json
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.generator_page import GeneratorPage


def load_option_data():
    """加载测试数据"""
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'option_test_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['test_cases']


def login(driver, base_url):
    """登录辅助函数"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login("admin", "123456")


class TestGenerateOptions:
    """测试数据生成选项"""

    @pytest.mark.parametrize("test_data", load_option_data(), ids=lambda x: x['name'])
    def test_generate_with_options(self, driver, base_url, test_data):
        login(driver, base_url)

        generator_page = GeneratorPage(driver, base_url)
        if not generator_page.is_on_generator_page():
            generator_page.open()

        schema_json = json.dumps(test_data['schema'], ensure_ascii=False, indent=2)
        generator_page.input_schema(schema_json)
        generator_page.set_count(test_data['count'])

        options = test_data['options']
        if options.get('smart'):
            generator_page.set_smart_option(True)
        if options.get('mutate'):
            generator_page.set_mutate_option(True)
        if options.get('report'):
            generator_page.set_report_option(True)

        generator_page.click_submit()
        time.sleep(6)

        result = generator_page.get_result_text()
        assert result and len(result) > 0, "生成失败"
