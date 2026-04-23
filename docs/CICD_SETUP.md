# CI/CD 配置说明

这个项目用了 GitHub Actions 做自动化测试和部署。

## CI 做了什么事？

每次 push 代码或创建 PR 时，自动执行：

```
代码检查 → 运行测试 → 生成报告
  ↓           ↓           ↓
 Black      pytest      Allure
 Flake8    (3.11/3.12)   报告
```

## 三个任务（Jobs）

### 1. Code Quality - 代码检查
- 用 Black 检查代码格式
- 用 Flake8 检查代码规范
- 失败会标红，但不会阻止后面的测试

### 2. Test - 运行测试
- 同时在 Python 3.11 和 3.12 下跑测试
- 生成 Allure 测试结果
- 上传测试结果供后面使用

### 3. Report - 生成报告
- 合并两个 Python 版本的测试结果
- 生成漂亮的 Allure HTML 报告
- **只有 master 分支**会部署到 GitHub Pages

## 触发条件

| 操作 | 目标分支 | 会发生什么 |
|------|---------|-----------|
| push | master/develop/feature/* | 跑完整 CI |
| pull_request | master/develop | 跑完整 CI |

## 查看结果

1. **CI 状态**：GitHub → Actions 标签页
2. **测试报告**：https://XW123-ART.github.io/mockly-tests/（master分支）
3. **PR 状态**：PR 页面下方会显示检查状态

## 如果 CI 挂了怎么办？

1. 点进 Actions 看哪个步骤报错了
2. 看错误日志，修复代码
3. 重新 push，CI 会自动重跑

常见原因：
- 代码格式不对（Black 检查失败）→ 运行 `black .` 格式化
- 测试失败 → 本地运行 `pytest` 调试
- 依赖问题 → 检查 requirements.txt

## 技术细节

用的 GitHub Actions 插件：
- `actions/checkout@v4` - 拉代码
- `actions/setup-python@v5` - 设置 Python
- `actions/cache@v4` - 缓存 pip 依赖
- `simple-elf/allure-report-action@master` - 生成 Allure 报告
- `peaceiris/actions-gh-pages@v3` - 部署到 GitHub Pages

---

CI/CD 就是自动化工具，让代码提交更规范，省去手动跑测试的麻烦。
