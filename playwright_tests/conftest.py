"""
Playwright 版本的 pytest 配置
与 Selenium 版本保持一致的结构
"""

import pytest


@pytest.fixture(scope="session")
def base_url():
    """返回项目的基础URL"""
    return "http://127.0.0.1:5000"


# 注意：pytest-playwright 会自动提供 page fixture
# 不需要在这里重新定义
# page fixture 会自动创建浏览器上下文和页面
