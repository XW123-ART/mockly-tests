"""
数据输出格式测试（JSON、CSV、SQL）
"""
import pytest
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.generator_page import GeneratorPage


def load_format_data():
    """加载测试数据"""
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'format_test_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['test_cases']


def login(driver, base_url):
    """登录辅助函数"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login("admin", "123456")


class TestOutputFormat:
    """测试输出格式"""

    @pytest.mark.parametrize("test_data", load_format_data(), ids=lambda x: x['name'])
    def test_output_format(self, driver, base_url, test_data):
        login(driver, base_url)

        generator_page = GeneratorPage(driver, base_url)
        if not generator_page.is_on_generator_page():
            generator_page.open()

        schema_json = json.dumps(test_data['schema'], ensure_ascii=False, indent=2)
        generator_page.input_schema(schema_json)
        generator_page.set_count(test_data['count'])
        generator_page.select_output_format(test_data['format'])

        if test_data['format'] == "sql":
            table_name = test_data.get('table', 'test_table')
            generator_page.set_table_name(table_name)

        generator_page.click_submit()

        result = generator_page.get_result_text()
        assert result, "没有生成结果"

        if test_data['format'] == "json":
            parsed = json.loads(result)
            assert isinstance(parsed, list)
            assert len(parsed) == test_data['count']

        elif test_data['format'] == "csv":
            lines = result.strip().split('\n')
            data_rows = [line for line in lines[1:] if line.strip()]
            assert len(data_rows) == test_data['count']
            assert ',' in result

        elif test_data['format'] == "sql":
            assert "INSERT INTO" in result.upper()
            insert_count = result.upper().count("INSERT INTO")
            assert insert_count == test_data['count']
