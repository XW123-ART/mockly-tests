"""
Playwright 版本的用户登录功能测试
"""
import pytest
import json
import os
from playwright.sync_api import Page

from playwright_tests.pages.login_page import LoginPage


def load_login_data():
    """加载登录测试数据"""
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'login_data.json')
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['test_cases']


@pytest.mark.parametrize("test_data", load_login_data(), ids=lambda x: x['name'])
def test_login(page: Page, test_data):
    """测试登录功能（参数化）"""
    base_url = "http://127.0.0.1:5000"
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login(test_data['username'], test_data['password'])

    if test_data['expected'] == 'success':
        assert login_page.is_login_success()
    else:
        assert login_page.is_on_login_page()


def test_login_required(page: Page):
    """测试未登录时访问生成页需要登录"""
    base_url = "http://127.0.0.1:5000"
    page.context.clear_cookies()
    page.goto(f"{base_url}/generator")

    login_page = LoginPage(page, base_url)
    assert login_page.is_on_login_page()


def test_login_button_state(page: Page):
    """测试登录按钮状态"""
    base_url = "http://127.0.0.1:5000"
    login_page = LoginPage(page, base_url)
    login_page.open()

    assert login_page.is_submit_button_enabled()
    login_page.input_username("admin")
    assert login_page.is_submit_button_enabled()


def test_playwright_auto_wait(page: Page):
    """测试 Playwright 自动等待功能"""
    base_url = "http://127.0.0.1:5000"
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login("admin", "123456")
    assert login_page.is_login_success()
