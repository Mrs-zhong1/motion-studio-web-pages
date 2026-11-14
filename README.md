# Motion Studio · Web 体验版

此仓库用于**公开的 Web 预览与用户验收**。研发源码仍以另一个修复分支 PR 为准；本仓库中的 `review-preview.html` 是一次性复制的预览构建，并不会自动同步开发分支。

## 当前真实状态

- `index.html`：不再是空文件，默认跳转到 `review-preview.html`
- `review-preview.html`：包含模板库首页、模板交互预览、组件与编辑器的单页 Web 体验版
- `.github/workflows/pages-review.yml`：发布脚本已经提交，并包含部署后的 HTTP 200 + 实际模板库内容检查
- **公开 Pages 网站是否已启用并成功发布，尚未得到可复核的成功证据**。提交 HTML 和工作流不等于网页已上线

## GitHub Pages 配置（需要仓库管理员操作）

1. 打开 [仓库 Pages 设置](https://github.com/Mrs-zhong1/motion-studio-web-pages/settings/pages)
2. 在 **Build and deployment → Source** 选择 **GitHub Actions**，使用已经存在的 `Deploy Motion Studio Review Site` 工作流
3. 在 [Actions](https://github.com/Mrs-zhong1/motion-studio-web-pages/actions/workflows/pages-review.yml) 中选择 **Run workflow**，选择 `main`，执行
4. 只有当工作流中 `Confirm deployed URL returns real Motion Studio markup` 显示 PASS 时，才能认为预览站点真正可访问

参考：[GitHub 官方 Pages 发布来源设置](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

### 如果上传 Pages Artifact 失败

当前开发仓库过去出现过 Actions Artifact 配额限制；如果展示仓库发布时也遇到该问题，可以**改用 Pages Source → Deploy from a branch → main → /(root)** 后保存。这是 GitHub 支持的静态网站分支发布方式，直接读取仓库根目录中的 `index.html`，不需要我们自定义构建脚本。启用这种分支发布方式时，现有自定义部署工作流不是发布必需条件。

## 链接

- [公开展示仓库源文件](https://github.com/Mrs-zhong1/motion-studio-web-pages/blob/main/review-preview.html)
- [U1～U4 开发 PR](https://github.com/Mrs-zhong1/motion-studio-web/pull/1)
- [16 张真实浏览器视觉截图画廊（GitHub 仓库文件）](https://github.com/Mrs-zhong1/motion-studio-web/blob/fix/u1-u2-template-first-20261114/stage9/visual-evidence/README.md)

**发布门槛：** 网站上线只代表可以开始真实交互验收。素材许可、视觉品质、原生 Safari 和真实 Apple GPU 验收还未完成，不能称为正式生产版。
