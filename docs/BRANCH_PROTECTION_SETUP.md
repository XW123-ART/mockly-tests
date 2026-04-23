# 分支保护设置教程

手把手教你设置 GitHub 分支保护，防止直接 push 到重要分支。

## 为什么要设置？

- 防止手滑直接 push 代码到 master
- 强制通过 Pull Request 合并代码
- 强制 CI 检查通过才能合并

## 设置步骤

### 1. 打开设置页面

1. 进入仓库：https://github.com/XW123-ART/mockly-tests
2. 点击 **Settings** 标签
3. 左侧菜单选择 **Branches**
4. 点击 **Add rule** 按钮

### 2. 保护 master 分支

填写以下信息：

**Branch name pattern**: `master`

勾选这些选项：

- ✅ **Require a pull request before merging**（必须通过PR合并）
  - Require approvals: `1`（需要1个人审批）

- ✅ **Require status checks to pass before merging**（CI必须通过）
  - Require branches to be up to date（要求分支最新）
  - 勾选这些检查：
    - `Code Quality`
    - `Test (3.11)`
    - `Test (3.12)`

- ✅ **Do not allow bypassing the above settings**（不允许绕过）

### 3. 保护 develop 分支

再点 **Add rule** 添加一个规则：

**Branch name pattern**: `develop`

勾选：
- ✅ Require a pull request before merging
- ✅ Require status checks to pass before merging
- ✅ Do not allow bypassing settings

### 4. 保存

点击 **Create** 保存。

## 测试是否生效

```bash
# 切换到 master
git checkout master

# 尝试直接 push（应该失败）
echo "test" >> README.md
git add .
git commit -m "test"
git push origin master
```

应该看到错误：
```
remote: error: GH006: Protected branch update failed...
remote: error: Changes must be made through a pull request.
```

说明设置成功！

## 正常 workflow

```
feature/xxx ──PR──▶ develop ──PR──▶ master
         (review)         (review+CI)
```

---

有问题就 Google 一下，或者问 ChatGPT 😄
