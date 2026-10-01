# 《未来之链》GitHub Pages 阅读版

## 网站内容

- 三部书架与完整章节目录。
- 已收录90章正文、一篇序言、92张章节配图和3张正式封面。
- 第53章《七分钟》正文与配图已补齐。
- 正文、图片均随仓库保存；网页不依赖 JavaScript 即可阅读、翻页。
- 章末留言、评分与读者登录链接到现有互动站，继续使用其云端数据。

## 发布设置

GitHub 仓库 Settings → Pages → Deploy from a branch → main → /docs → Save。

## 文件说明

- `content/chapters/`：章节正文、标题、时间和配图列表。
- `docs/assets/`：封面、配图、样式及网站图标。
- `docs/index.html`：首页。
- `docs/read/章节编号/index.html`：独立章节页。
- `scripts/build.py`：使用 Python 3 生成全部静态页面，不需要额外安装依赖。

## 更新章节

修改 `content/chapters/`，然后在仓库目录运行：

```sh
python3 scripts/build.py
```

将更新后的内容和 `docs` 目录一并提交到 main。GitHub Pages 会按发布设置更新。

通过原网站作者后台上传的修订不会自动同步到此仓库，需要重新导入并生成页面。GitHub 仓库不包含云端留言数据库、登录凭据或本地测试账号。
