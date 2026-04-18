# 分支保护设置指南

本文档说明如何在 GitHub 上配置分支保护规则，强制执行 PR Review 流程。

## 📋 设置步骤

### 1. 进入分支保护设置

1. 打开仓库页面：https://github.com/XW123-ART/mockly-tests
2. 点击 **Settings** 选项卡
3. 在左侧菜单选择 **Branches**
4. 点击 **Add rule** 按钮

### 2. 配置 main/master 分支保护

**Branch name pattern:** `main` 或 `master`

#### ✅ 勾选以下选项：

**Protect matching branches**

- [x] **Require a pull request before merging**
  - [x] Require approvals: `1`
  - [x] Dismiss stale PR approvals when new commits are pushed
  - [x] Require review from Code Owners (如果添加了 CODEOWNERS 文件)

- [x] **Require status checks to pass before merging**
  - [x] Require branches to be up to date before merging
  - **Status checks that are required:**
    - `code-quality`
    - `test (3.11)`
    - `test (3.12)`
    - `generate-report`

- [x] **Require conversation resolution before merging**

- [x] **Require signed commits** (可选，推荐)

- [x] **Include administrators** (确保管理员也遵守规则)

**Restrict pushes that create files**

- [x] **Restrict pushes that create files** (可选)

**Do not allow bypassing the above settings**

- [x] **Do not allow bypassing the above settings**

### 3. 配置 develop 分支保护

点击 **Add rule** 添加另一条规则：

**Branch name pattern:** `develop`

#### ✅ 勾选以下选项：

- [x] **Require a pull request before merging**
  - [x] Require approvals: `1`

- [x] **Require status checks to pass before merging**
  - [x] Require branches to be up to date before merging
  - **Status checks that are required:**
    - `code-quality`
    - `test (3.11)`
    - `test (3.12)`

- [x] **Do not allow bypassing the above settings**

### 4. 保存设置

点击 **Create** 或 **Save changes** 保存分支保护规则。

## 🔒 保护效果

设置完成后，以下操作将被禁止：

| 操作 | 保护前 | 保护后 |
|------|--------|--------|
| 直接 push 到 main | ✅ 允许 | ❌ 禁止 |
| 直接 push 到 develop | ✅ 允许 | ❌ 禁止 |
| 无 Review 合并 | ✅ 允许 | ❌ 禁止 |
| CI 失败合并 | ✅ 允许 | ❌ 禁止 |
| 删除 main 分支 | ✅ 允许 | ❌ 禁止 |

## 📝 验证保护是否生效

### 测试 1：直接 Push 到 main

```bash
 git checkout main
 git pull origin main
 # 做一些修改
 echo "test" >> README.md
 git add .
 git commit -m "test: direct push to main"
 git push origin main
```

**预期结果：**
```
remote: error: GH006: Protected branch update failed...
remote: error: Changes must be made through a pull request.
```

### 测试 2：创建 PR 并验证检查

1. 创建一个新分支：`git checkout -b feature/test-protection`
2. 做一些修改并推送
3. 在 GitHub 创建 PR
4. 验证是否出现以下检查项：
   - `code-quality`
   - `test (3.11)`
   - `test (3.12)`
   - `generate-report`

5. 尝试在检查通过前合并，应该被阻止

## 🛠️ 使用 GitHub CLI 设置（可选）

如果你安装了 [GitHub CLI](https://cli.github.com/)，可以使用命令设置：

```bash
# 登录 GitHub CLI
gh auth login

# 设置 main 分支保护
gh api repos/XW123-ART/mockly-tests/branches/main/protection \
  --method PUT \
  --input - <<EOF
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["code-quality", "test (3.11)", "test (3.12)", "generate-report"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "dismiss_stale_reviews": true
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF

# 设置 develop 分支保护
gh api repos/XW123-ART/mockly-tests/branches/develop/protection \
  --method PUT \
  --input - <<EOF
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["code-quality", "test (3.11)", "test (3.12)"]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

## 📊 分支保护配置检查清单

- [ ] main/master 分支规则已创建
- [ ] develop 分支规则已创建
- [ ] 要求 1 个 PR Review
- [ ] 要求 CI 状态检查通过
- [ ] 禁止管理员绕过规则
- [ ] 禁止强制推送
- [ ] 禁止分支删除
- [ ] 已测试直接 push 被阻止
- [ ] 已测试 PR 合并需要 Review

---

如有问题，请参考 [GitHub 官方文档](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
