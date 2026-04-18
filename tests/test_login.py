"""
用户登录功能测试
"""
import pytest
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.generator_page import GeneratorPage


def load_login_data():
    """加载登录测试数据"""
    data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'login_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['test_cases']


@pytest.mark.parametrize("test_data", load_login_data(), ids=lambda x: x['name'])
def test_login(driver, base_url, test_data):
    """测试登录功能（参数化）"""
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_data['username'], test_data['password'])

    if test_data['expected'] == 'success':
        assert login_page.is_login_success(), "登录失败"
        generator_page = GeneratorPage(driver, base_url)
        assert test_data['username'] in generator_page.get_user_info()
    else:
        assert login_page.is_on_login_page(), "应该留在登录页"


def test_login_required(driver, base_url):
    """测试未登录时访问生成页需要登录"""
    driver.delete_all_cookies()
    generator_page = GeneratorPage(driver, base_url)
    generator_page.open()
    assert LoginPage(driver, base_url).is_on_login_page()
