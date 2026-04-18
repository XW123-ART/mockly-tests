"""
pytest的配置文件
这个文件会自动被pytest加载，用来做一些全局配置
"""

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService


# 这是一个pytest的fixture，用来创建浏览器驱动
# scope="session"表示整个测试会话只创建一次浏览器
@pytest.fixture(scope="session")
def driver():
    """
    创建浏览器驱动
    这个fixture会在所有测试开始前创建一个浏览器，
    所有测试结束后再关闭浏览器
    """
    print("\n=== 开始创建浏览器驱动 ===")

    # 使用 Selenium 4.6+ 内置的 Selenium Manager 自动管理驱动
    # 无需指定驱动路径，Selenium 会自动下载匹配浏览器版本的驱动
    browser = webdriver.Edge()

    # 最大化窗口
    browser.maximize_window()

    print("=== 浏览器创建成功 ===")

    # 添加Allure报告信息
    allure.attach("浏览器类型", "Microsoft Edge")

    # yield相当于return，但后面还有代码会执行
    # 这里把浏览器对象传给测试用例
    yield browser

    # 测试结束后执行的代码
    print("\n=== 测试结束，关闭浏览器 ===")
    browser.quit()
    print("=== 浏览器已关闭 ===")


# pytest钩子：测试失败时自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)#tryfirst=True表示优先执行这个钩子
def pytest_runtest_makereport(item, call):
    """
    测试失败时自动截图并添加到Allure报告
    """
    outcome = yield
    report = outcome.get_result()

    # 如果测试失败且有driver fixture
    if report.when == "call" and report.failed:
        # 获取driver
        driver = None
        for fixture_name in item.fixturenames:
            if fixture_name == "driver":
                driver = item.funcargs.get("driver")
                break

        if driver:
            # 截图
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="失败截图",
                    attachment_type=allure.attachment_type.PNG
                )
                allure.attach(
                    driver.current_url,
                    name="失败时的URL",
                    attachment_type=allure.attachment_type.TEXT
                )
            except Exception as e:
                print(f"截图失败: {e}")


# 另一个fixture，用来存储基础URL
@pytest.fixture(scope="session")
def base_url():
    """返回项目的基础URL"""
    return "http://127.0.0.1:5000"
