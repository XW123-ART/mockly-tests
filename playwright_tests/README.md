# Playwright 版本测试套件

使用 Playwright + pytest + POM 模式重新实现的测试框架

## 项目特点

### 1. 与 Selenium 版本的一致性
- **相同的 POM 架构**：保持 pages/base_page.py + pages/login_page.py 结构
- **相同的测试数据**：复用 data/login_data.json
- **相同的测试场景**：覆盖所有登录相关测试用例

### 2. Playwright 带来的改进

| 特性 | Selenium | Playwright |
|------|----------|------------|
| 自动等待 | 需要手动 sleep | ✅ 自动等待元素可交互 |
| 元素定位 | By.ID/CLASS_NAME/CSS | CSS/XPath，更简洁 |
| 浏览器管理 | 手动下载驱动 | ✅ 自动管理 |
| 执行速度 | 较慢 | ✅ 更快 |
| 多浏览器 | 配置复杂 | ✅ 原生支持 Chromium/Firefox/WebKit |

### 3. 代码对比示例

**Selenium 版本：**
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 需要显式等待
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-btn"))
)
element.click()
time.sleep(2)  # 等待页面跳转
```

**Playwright 版本：**
```python
# 自动等待，代码更简洁
page.locator(".login-btn").click()
# 不需要 sleep，自动处理
```

## 运行测试

```bash
# 运行所有 Playwright 测试
python -m pytest playwright_tests/ -v

# 运行特定测试
python -m pytest playwright_tests/test_login.py::test_login -v

# 带浏览器界面运行（调试用）
python -m pytest playwright_tests/ -v --headed

# 特定浏览器
python -m pytest playwright_tests/ -v --browser chromium
```

## 测试结果

```
playwright_tests/test_login.py::test_login[chromium-正确用户名密码] PASSED
playwright_tests/test_login.py::test_login[chromium-错误密码] PASSED
playwright_tests/test_login.py::test_login[chromium-不存在的用户] PASSED
playwright_tests/test_login.py::test_login[chromium-用户名为空] PASSED
playwright_tests/test_login.py::test_login[chromium-密码为空] PASSED
playwright_tests/test_login.py::test_login_required[chromium] PASSED
playwright_tests/test_login.py::test_login_button_state[chromium] PASSED
playwright_tests/test_login.py::test_playwright_auto_wait[chromium] PASSED

============================== 8 passed in 9.81s ==============================
```

## 技术亮点

1. **跨技术栈能力**：能将 Selenium 项目迁移到 Playwright
2. **POM 模式精通**：无论用什么工具，都保持架构一致性
3. **框架设计能力**：设计可复用的基础页面类
4. **新技术学习能力**：快速掌握 Playwright 的 API 和最佳实践

## 新增测试用例

除了复刻 Selenium 版本的测试，还增加了 Playwright 特有测试：

- `test_login_button_state`: 验证按钮状态（利用 Playwright 更强的元素状态检测）
- `test_playwright_auto_wait`: 演示自动等待机制
