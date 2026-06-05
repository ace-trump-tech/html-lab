# 🧰 HTML Lab · 在线工具集

> 轻量、纯粹、无服务端 —— 所有工具均在浏览器本地运行，绝不收集任何数据。

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen)](https://ace-trump-tech.github.io/html-lab/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## 📌 项目简介

`html-lab` 是一个基于 **GitHub Pages** 的在线工具集合，提供日常开发、调试及隐私保护所需的小工具。每个工具都是独立的 HTML 页面，无需后端，数据永不离开你的浏览器。

## 🚀 当前已上线工具（13 件）

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **Base64 编码/解码** | [base64/](https://ace-trump-tech.github.io/html-lab/base64/) | 支持 UTF-8 文本（中文、emoji），在线编码解码，一键复制结果。 |
| **二维码生成器** | [qrcode/](https://ace-trump-tech.github.io/html-lab/qrcode/) | 输入文本或网址，实时生成 QR Code，可下载为 PNG 图片。 |
| **JSON 格式化 & 校验** | [json-formatter/](https://ace-trump-tech.github.io/html-lab/json-formatter/) | 格式化、压缩、校验 JSON，语法高亮，错误定位，支持转义/去转义。 |
| **URL 编码/解码** | [url-codec/](https://ace-trump-tech.github.io/html-lab/url-codec/) | encodeURIComponent / encodeURI 双模式，处理中文及特殊字符。 |
| **Unix 时间戳转换** | [unix-timestamp/](https://ace-trump-tech.github.io/html-lab/unix-timestamp/) | 实时时间戳显示，时间戳与日期双向互转，秒/毫秒自动识别。 |
| **Markdown 在线预览** | [markdown-preview/](https://ace-trump-tech.github.io/html-lab/markdown-preview/) | 左栏编辑右栏实时预览，快捷插入工具栏，可复制渲染后的 HTML。 |
| **颜色工具** | [color-tools/](https://ace-trump-tech.github.io/html-lab/color-tools/) | 颜色拾取器，HEX / RGB / HSL 三者实时互转，CSS 代码一键复制。 |
| **随机密码生成器** | [password-generator/](https://ace-trump-tech.github.io/html-lab/password-generator/) | 基于 Web Crypto API，可配置长度与字符集，实时显示密码强度。 |
| **正则表达式测试器** | [regex-tester/](https://ace-trump-tech.github.io/html-lab/regex-tester/) | 输入正则与测试文本，实时高亮匹配，显示捕获分组与匹配位置。 |
| **JWT 解码器** | [jwt-decoder/](https://ace-trump-tech.github.io/html-lab/jwt-decoder/) | 解码 JWT Header 与 Payload，解析标准 Claims，检测过期状态。 |
| **哈希生成器** | [hash-generator/](https://ace-trump-tech.github.io/html-lab/hash-generator/) | MD5 / SHA-1 / SHA-256 / SHA-512 摘要生成，本地计算不泄露数据。 |
| **文本差异对比** | [diff-checker/](https://ace-trump-tech.github.io/html-lab/diff-checker/) | 两段文本逐行 Diff，新增绿色标记、删除红色标记，统计增删行数。 |
| **字数 & 字节统计器** | [word-counter/](https://ace-trump-tech.github.io/html-lab/word-counter/) | 实时统计字符数、字节数（UTF-8）、单词数、中文字符数、阅读时间。 |

> 💡 所有工具完全在浏览器本地运行，**不会上传任何数据**，可放心使用。

## 🧪 本地运行与开发

```bash
git clone https://github.com/ace-trump-tech/html-lab.git
cd html-lab
# 使用任意 HTTP 服务器，例如 Python 3
python -m http.server 8080
```
打开浏览器访问 `http://localhost:8080` 即可预览。

## 📁 项目结构

```
html-lab/
├── index.html              # 工具集首页（导航卡片 + 更新日志）
├── base64/                 # Base64 编解码工具
├── qrcode/                 # 二维码生成器
├── json-formatter/         # JSON 格式化与校验
├── url-codec/              # URL 编码/解码
├── unix-timestamp/         # Unix 时间戳转换
├── markdown-preview/       # Markdown 在线预览
├── color-tools/            # 颜色工具（HEX/RGB/HSL）
├── password-generator/     # 随机密码生成器
├── regex-tester/           # 正则表达式测试器
├── jwt-decoder/            # JWT 解码器
├── hash-generator/         # 哈希生成器
├── diff-checker/           # 文本差异对比
├── word-counter/           # 字数 & 字节统计器
└── README.md
```

## ✨ 如何添加一个新工具？

1. 在根目录下创建新文件夹，例如 `my-tool/`。
2. 在该文件夹内新建 `index.html`，编写工具代码（纯前端）。
3. 在根目录 `index.html` 的 `.tools-grid` 中添加指向新工具的卡片，并在 `.update-list` 中添加条目。
4. 提交并推送：
   ```bash
   git add .
   git commit -m "feat: add new tool"
   git push origin main
   ```
5. GitHub Pages 会自动部署，新工具即可通过 `https://ace-trump-tech.github.io/html-lab/新文件夹名/` 访问。

## 📜 技术栈

- 原生 HTML5 / CSS3 / JavaScript（ES6+）
- 二维码生成：`qrcode-generator`（MIT）
- Markdown 渲染：`marked`（MIT）
- 哈希计算：`crypto-js`（MIT）
- 其他工具尽量无第三方依赖
- 响应式设计，支持移动端

## 🤝 贡献指南

- **纯前端实现**，不依赖外部 API，不收集用户数据。
- 每个工具独立成文件夹，内含 `index.html`。
- 保持界面简洁、风格统一。
- 提交前请在主流浏览器（Chrome / Firefox / Edge）测试。

提交方式：Fork → 创建分支 → PR。

## 📄 许可证

[MIT](LICENSE) © ace-trump-tech

## 🙏 致谢

感谢开源社区，让在线工具回归干净、安全。

---

**⭐ 如果这个工具箱对你有帮助，请给仓库点个 Star！**
