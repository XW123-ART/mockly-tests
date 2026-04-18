# CI/CD 流水线配置说明

本文档详细说明 GitHub Actions CI/CD 流水线的配置和使用。

## 📋 流水线概览

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Trigger   │──▶│ Code Quality│──▶│    Test     │──▶│    Report   │
│ Push/PR     │   │ Black/Flake8│   │ Pytest      │   │ Allure      │
└─────────────┘   └─────────────┘   └─────────────┘   └──────┬──────┘
                                                              │
                                    ┌─────────────┐          │
                                    │   Deploy    │◀─────────┘
                                    │ GitHub Pages│
                                    └─────────────┘
```

## 🔄 触发条件

| 事件 | 目标分支 | 行为 |
|------|----------|------|
| `push` | `main`, `master`, `develop`, `feature/*`, `bugfix/*` | 运行完整流水线 |
| `pull_request` | `main`, `master`, `develop` | 运行完整流水线 |

## 🛠️ 作业 (Jobs) 说明

### 1. Code Quality

**目的：** 确保代码符合规范

**检查项：**
- ✅ Black 代码格式化
- ✅ isort 导入排序
- ✅ flake8 代码质量检查

**失败处理：** 会标记失败但不会阻塞后续步骤（用于渐进式采用）

### 2. Test

**目的：** 运行自动化测试

**矩阵策略：**
- Python 3.11
- Python 3.12

**步骤：**
1. 检出代码
2. 设置 Python 环境
3. 安装依赖
4. 运行 pytest 生成 Allure 结果
5. 上传测试结果 Artifact

### 3. Generate Report

**目的：** 生成并部署 Allure 测试报告

**功能：**
- 合并多 Python 版本的测试结果
- 生成历史报告
- 部署到 GitHub Pages
- PR 自动添加报告链接

### 4. Notify

**目的：** 发送通知

**功能：**
- 输出各步骤状态
- 失败时发送通知

## 📦 Artifacts

| Artifact 名称 | 内容 | 保留时间 |
|---------------|------|----------|
| `test-results-3.11` | Allure 结果 (Python 3.11) | 30天 |
| `test-results-3.12` | Allure 结果 (Python 3.12) | 30天 |

## 🚀 GitHub Pages 部署

### 配置步骤

1. 进入仓库 **Settings** → **Pages**
2. **Source** 选择 **Deploy from a branch**
3. **Branch** 选择 `gh-pages` / `root`
4. 点击 **Save**

### 访问地址

- 报告首页：`https://XW123-ART.github.io/mockly-tests/`
- 特定运行：`https://XW123-ART.github.io/mockly-tests/{run_number}/`

## 🔧 本地测试 CI 配置

使用 [act](https://github.com/nektos/act) 工具本地测试：

```bash
# 安装 act
brew install act

# 运行完整流水线
act

# 只运行特定 job
act -j test

# 使用特定事件
act pull_request
```

## 📝 环境变量和 Secrets

### Repository Secrets

| Secret | 说明 | 必需 |
|--------|------|------|
| `GITHUB_TOKEN` | 自动提供，用于部署 Pages | ✅ |

### 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `PYTHON_VERSION` | 3.12 | 主 Python 版本 |

## 🐛 故障排查

### 问题：CI 运行超时

**解决：**
```yaml
# 在 job 中添加超时设置
timeout-minutes: 30
```

### 问题：依赖安装慢

**解决：** 已配置 pip cache，如仍慢可更换源：
```yaml
- name: Install dependencies
  run: |
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    pip install -r requirements.txt
```

### 问题：Allure 报告未生成

**检查：**
1. 测试是否生成了 `allure-results` 目录
2. 检查 pytest 命令是否包含 `--alluredir=allure-results`

### 问题：Pages 部署失败

**检查：**
1. 确认 `gh-pages` 分支存在
2. 确认仓库 Settings → Pages 配置正确
3. 检查 `GITHUB_TOKEN` 权限

## 📊 CI/CD 指标

可在 GitHub 查看以下指标：

- **Actions** 标签页：查看运行历史和成功率
- **Insights** → **Actions**：查看使用统计

## 🔒 安全最佳实践

1. **不要**在代码中硬编码敏感信息
2. **不要**将 `.env` 文件提交到仓库
3. 使用 GitHub Secrets 存储敏感数据
4. 定期轮换访问密钥

---

如有问题，请参考 [GitHub Actions 文档](https://docs.github.com/en/actions)
