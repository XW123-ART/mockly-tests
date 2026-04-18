# 贡献指南 (Contributing Guide)

感谢您对 Mockly Tests 项目的关注！本文档将帮助您了解我们的开发流程和分支策略。

## 🌿 分支策略 (Git Branching Strategy)

本项目采用 **Git Flow** 分支模型：

### 主要分支

| 分支 | 说明 | 保护级别 |
|------|------|----------|
| `main` / `master` | 生产环境代码，永远保持稳定 | 🔴 严格保护 |
| `develop` | 开发集成分支，新功能在此合并 | 🟡 保护 |

### 辅助分支

| 分支前缀 | 用途 | 示例 |
|----------|------|------|
| `feature/*` | 新功能开发 | `feature/user-login` |
| `bugfix/*` | Bug修复 | `bugfix/fix-login-error` |
| `hotfix/*` | 紧急生产问题修复 | `hotfix/fix-crash` |
| `release/*` | 版本发布准备 | `release/v1.0.0` |

## 🔄 工作流程

### 1. 创建功能分支

```bash
# 从 develop 分支创建
 git checkout develop
 git pull origin develop
 git checkout -b feature/your-feature-name

# 或者使用 git flow
 git flow feature start your-feature-name
```

### 2. 开发与提交

```bash
# 进行代码修改
 git add .
 git commit -m "feat: add user authentication feature"

# 保持与 develop 同步
 git pull origin develop
```

**提交信息规范：**

- `feat:` 新功能
- `fix:` Bug修复
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

### 3. 推送并创建 PR

```bash
 git push origin feature/your-feature-name
```

然后到 GitHub 创建 Pull Request，目标分支选择 `develop`。

### 4. PR Review 流程

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  创建 PR    │ ──▶ │  CI 检查    │ ──▶ │  Code Review│
└─────────────┘     └─────────────┘     └──────┬──────┘
                                                │
                       ┌─────────────┐          │
                       │  合并到     │ ◀────────┘
                       │  develop    │    通过
                       └─────────────┘
```

**PR 必须满足以下条件才能合并：**

1. ✅ 至少 1 个 Reviewer 的 Approve
2. ✅ CI/CD 流水线全部通过（测试、代码质量检查）
3. ✅ 无冲突，可自动合并
4. ✅ Allure 测试报告生成成功

## 🛡️ 分支保护规则

### main/master 分支保护

- [ ] 禁止直接推送 (Disable force pushes)
- [ ] 禁止删除 (Disable deletions)
- [ ] 要求 PR 才能合并 (Require pull request reviews)
- [ ] 要求 1 个 approving review
- [ ] 要求状态检查通过 (Require status checks)
  - `code-quality`
  - `test` (Python 3.11, 3.12)
  - `generate-report`
- [ ] 要求分支保持最新 (Require branches to be up to date)

### develop 分支保护

- [ ] 禁止直接推送
- [ ] 要求 PR 才能合并
- [ ] 要求 1 个 approving review
- [ ] 要求状态检查通过

## 🚀 CI/CD 流程

```
Push/PR ──▶ Code Quality ──▶ Test ──▶ Generate Report ──▶ Deploy to Pages
              (black/flake8)  (pytest)   (Allure)           (gh-pages)
```

### 流水线任务说明

| 任务 | 说明 | 失败影响 |
|------|------|----------|
| `code-quality` | 代码格式和质量检查 | 阻止合并 |
| `test` | 运行 pytest 测试 (多 Python 版本) | 阻止合并 |
| `generate-report` | 生成 Allure 测试报告 | 不阻止合并 |
| `notify` | 发送通知 | 无影响 |

### Allure 报告

- 每次 CI 运行都会生成 Allure 测试报告
- 报告自动部署到 GitHub Pages
- 访问地址：`https://XW123-ART.github.io/mockly-tests/`
- PR 会自动添加报告链接评论

## 📝 代码规范

### Python 代码风格

- 使用 **Black** 进行代码格式化
- 使用 **isort** 管理导入
- 使用 **flake8** 进行代码检查
- 最大行长度：88 字符 (Black 默认)

```bash
# 格式化代码
 black .
 isort .

# 检查代码
 flake8 .
```

### 测试规范

- 所有新功能必须包含测试
- 测试文件命名：`test_*.py`
- 测试函数命名：`test_*`
- 使用 pytest 参数化实现数据驱动测试
- 使用 Allure 注解丰富测试报告

```python
import allure

@allure.feature("用户模块")
@allure.story("登录功能")
def test_login_success(driver, base_url):
    """测试用户成功登录"""
    with allure.step("打开登录页面"):
        login_page.open()
    with allure.step("输入用户名密码"):
        login_page.login("admin", "123456")
    with allure.step("验证登录成功"):
        assert login_page.is_login_success()
```

## 🆘 常见问题

### Q: CI 失败了怎么办？

1. 点击 PR 中的 "Details" 查看失败原因
2. 修复代码后推送到同一分支
3. CI 会自动重新运行

### Q: 如何查看 Allure 报告？

- **方式一**：访问 GitHub Pages 部署的报告
- **方式二**：下载 CI Artifact 中的 `test-results`
- **方式三**：本地运行 `allure serve allure-results`

### Q: 分支冲突如何解决？

```bash
 git checkout feature/your-branch
 git fetch origin
 git rebase origin/develop
 # 解决冲突
 git push -f origin feature/your-branch
```

## 📞 联系方式

如有问题，请通过以下方式联系：

- 创建 GitHub Issue
- 发送邮件至项目维护者

---

**Happy Coding! 🎉**
