# Mockly Tests - Web 自动化测试项目

<p align="center">
  <a href="https://github.com/XW123-ART/mockly-tests/actions">
    <img src="https://github.com/XW123-ART/mockly-tests/workflows/CI/CD%20Pipeline/badge.svg" alt="CI/CD Status">
  </a>
  <a href="https://XW123-ART.github.io/mockly-tests/">
    <img src="https://img.shields.io/badge/Allure%20Report-View-9cf.svg" alt="Allure Report">
  </a>
  <img src="https://img.shields.io/badge/python-3.11%20%7C%203.12-blue.svg" alt="Python Version">
  <a href="https://github.com/XW123-ART/mockly-tests/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  </a>
</p>

<p align="center">
  基于 Selenium 和 Playwright 的 Web 自动化测试框架，集成 Allure 测试报告
</p>

***

## 📋 项目结构

```
mockly-tests/
├── .github/
│   ├── workflows/
│   │   └── test.yml          # CI/CD 流水线配置
│   └── pull_request_template.md  # PR 模板
├── docs/
│   ├── BRANCH_PROTECTION_SETUP.md  # 分支保护设置指南
│   └── CICD_SETUP.md         # CI/CD 配置说明
├── pages/                    # 页面对象 (Selenium)
│   ├── base_page.py
│   ├── login_page.py
│   └── generator_page.py
├── playwright_tests/         # Playwright 版本测试
│   ├── pages/
│   └── test_login.py
├── tests/                    # Selenium 测试用例
│   ├── test_login.py
│   ├── test_generate.py
│   ├── test_file_upload.py
│   ├── test_openapi_upload.py
│   ├── test_output_format.py
│   ├── test_generate_options.py
│   └── test_source_switch.py
├── data/                     # 测试数据
├── conftest.py              # Pytest 配置
├── requirements.txt         # 依赖列表
├── CONTRIBUTING.md          # 贡献指南
└── README.md
```

## 🚀 快速开始

### 环境要求

- Python 3.11 或 3.12
- Chrome / Edge / Firefox 浏览器
- Git

### 安装步骤

1. 克隆仓库

```bash
git clone https://github.com/XW123-ART/mockly-tests.git
cd mockly-tests
```

1. 创建虚拟环境

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

1. 安装依赖

```bash
pip install -r requirements.txt

# 安装 Playwright 浏览器
playwright install
```

1. 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定测试
pytest tests/test_login.py -v

# 生成 Allure 报告
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## 🌿 分支策略

本项目采用 **Git Flow** 分支模型：

| 分支          | 用途     | 保护级别    |
| ----------- | ------ | ------- |
| `master`    | 生产环境代码 | 🔴 严格保护 |
| `develop`   | 开发集成分支 | 🟡 保护   |
| `feature/*` | 新功能开发  | 🟢 无保护  |
| `bugfix/*`  | Bug 修复 | 🟢 无保护  |
| `hotfix/*`  | 紧急修复   | 🟢 无保护  |

### 工作流程

```bash
# 1. 从 develop 创建功能分支
git checkout develop
git pull origin develop
git checkout -b feature/your-feature

# 2. 开发并提交
git add .
git commit -m "feat: add new feature"
git push origin feature/your-feature

# 3. 创建 Pull Request 到 develop
# 4. Code Review 后合并
```

详细说明请查看 [CONTRIBUTING.md](./CONTRIBUTING.md)

## 🔄 CI/CD 流水线

### 流水线流程

```
Push/PR ──▶ Code Quality ──▶ Test ──▶ Generate Report ──▶ Deploy
            (Black/Flake8)   (Pytest)  (Allure)           (GitHub Pages)
```

### 状态检查

- ✅ **Code Quality** - 代码格式和质量检查
- ✅ **Test (3.11)** - Python 3.11 测试
- ✅ **Test (3.12)** - Python 3.12 测试
- ✅ **Generate Report** - Allure 报告生成

### 测试报告

- 📊 [Allure 测试报告](https://XW123-ART.github.io/mockly-tests/)
- 每次 CI 运行自动生成
- PR 自动添加报告链接

## 🧪 测试框架

### Selenium 版本

```python
# tests/test_login.py
def test_login(driver, base_url, test_data):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(test_data['username'], test_data['password'])
    assert login_page.is_login_success()
```

### Playwright 版本

```python
# playwright_tests/test_login.py
def test_login(page: Page, test_data):
    base_url = "http://127.0.0.1:5000"
    login_page = LoginPage(page, base_url)
    login_page.open()
    login_page.login(test_data['username'], test_data['password'])
    assert login_page.is_login_success()
```

## 📊 Allure 报告

### 本地查看

```bash
# 生成测试结果
pytest tests/ --alluredir=allure-results

# 启动报告服务
allure serve allure-results
```

### 在线报告

访问：<https://XW123-ART.github.io/mockly-tests/>

### 报告特性

- 📈 测试趋势分析
- 📋 详细的步骤记录
- 🖼️ 失败自动截图
- 🔍 测试用例分类

## 🤝 贡献指南

我们欢迎所有形式的贡献！请查看：

- [CONTRIBUTING.md](./CONTRIBUTING.md) - 详细的贡献指南
- [docs/BRANCH\_PROTECTION\_SETUP.md](./docs/BRANCH_PROTECTION_SETUP.md) - 分支保护设置
- [docs/CICD\_SETUP.md](./docs/CICD_SETUP.md) - CI/CD 配置说明

### 提交 PR 前检查清单

- [ ] 代码已通过 Black 格式化
- [ ] 所有测试通过
- [ ] 创建了功能分支 (`feature/xxx`)
- [ ] 提交了清晰的 PR 描述
- [ ] 添加了必要的测试

## 📝 技术栈

| 技术         | 版本        | 用途      |
| ---------- | --------- | ------- |
| Python     | 3.11/3.12 | 编程语言    |
| pytest     | 9.0+      | 测试框架    |
| Selenium   | 4.41+     | Web 自动化 |
| Playwright | 1.51+     | Web 自动化 |
| Allure     | 2.15+     | 测试报告    |
| Black      | 24.3+     | 代码格式化   |
| flake8     | 7.0+      | 代码检查    |

## 📄 许可证

本项目采用 [MIT](LICENSE) 许可证。

## 👥 作者

- **XW123-ART** - 项目维护者

***

<p align="center">
  如果这个项目对你有帮助，请给我们一颗 ⭐️
</p>

cicici

<br />

# CI trigger test
