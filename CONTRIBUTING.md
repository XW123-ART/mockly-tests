# 项目贡献说明

这个项目是我的自动化测试学习项目，欢迎一起交流！

## 🌿 分支管理（Git Flow）

我用的分支策略很简单：

| 分支 | 用途 | 说明 |
|------|------|------|
| `master` | 正式版本 | 稳定的代码，通过PR才能合并进来 |
| `develop` | 开发分支 | 日常开发都在这，新功能先合并到这 |
| `feature/*` | 功能分支 | 开发新功能，比如 `feature/login-test` |

### 开发流程

1. **从 develop 创建新分支**
```bash
git checkout develop
git pull origin develop
git checkout -b feature/你的功能名称
```

2. **写代码 + 提交**
```bash
git add .
git commit -m "feat: 添加了xxx功能"
```

3. **推送到 GitHub 并创建 PR**
```bash
git push origin feature/你的功能名称
```
然后去 GitHub 创建 Pull Request，选择合并到 develop 分支。

### 提交信息格式（建议）

- `feat:` 新功能
- `fix:` 修复bug
- `docs:` 修改文档
- `test:` 添加测试

## 🛡️ 分支保护说明

我配置了 GitHub 的分支保护，主要是为了防止自己手滑：

- **master 分支**：不能直接 push，必须通过 PR 合并，且需要 CI 检查通过
- **develop 分支**：同样需要 PR 合并

这样即使我自己写代码，也要走 PR 流程，保证代码质量。

## 🚀 CI/CD 自动化的东西

提交代码后 GitHub Actions 会自动跑：

1. **代码检查**：用 Black 检查代码格式，Flake8 检查代码规范
2. **运行测试**：同时在 Python 3.11 和 3.12 下跑测试
3. **生成报告**：自动生成 Allure 测试报告
4. **部署报告**：如果是 master 分支，自动部署到 GitHub Pages

你可以在 Actions 页面看到运行结果，报告地址：
https://XW123-ART.github.io/mockly-tests/

## 📝 代码规范

我用的 Python 代码规范：

```bash
# 格式化代码
black .

# 检查代码
flake8 .
```

## ❓ 有问题？

有问题可以提 Issue，或者直接联系我。

---

一起写代码，一起进步！
