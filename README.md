# 🧰 HTML Lab · 在线工具集

> 轻量、纯粹、无服务端 —— 所有工具均在浏览器本地运行，绝不收集任何数据。

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen)](https://ace-trump-tech.github.io/html-lab/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## 📌 项目简介

`html-lab` 是一个基于 **GitHub Pages** 的在线工具集合，提供日常开发、调试及隐私保护所需的小工具。每个工具都是独立的 HTML 页面，无需后端，数据永不离开你的浏览器。

## 🚀 如何使用（直接访问）

### 主站首页
**[https://ace-trump-tech.github.io/html-lab/](https://ace-trump-tech.github.io/html-lab/)**  
首页以卡片形式展示所有可用工具，点击卡片上的按钮即可跳转到对应工具。

### 当前已上线工具

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **Base64 编码/解码** | [base64-tool/](https://ace-trump-tech.github.io/html-lab/base64-tool/) | 支持 UTF-8 文本（中文、emoji），在线编码解码，一键复制结果。 |
| **二维码生成器** | [qrcode-tool/](https://ace-trump-tech.github.io/html-lab/qrcode-tool/) | 输入文本或网址，实时生成 QR Code，可下载为 PNG 图片。 |

> 💡 所有工具完全在浏览器本地运行，**不会上传任何数据**，可放心使用。

## 📅 计划中的工具

- JSON 格式化与校验
- Unix 时间戳转换
- 颜色拾取器（HEX/RGB/HSL 互转）
- Markdown 在线预览
- 随机密码生成器
- …（更多根据社区反馈添加）

## 🧪 本地运行与开发（适合想要自己部署或贡献代码的开发者）

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
├── index.html              # 工具集首页（导航卡片）
├── base64-tool/
│   └── index.html          # Base64 编解码工具
├── qrcode-tool/
│   └── index.html          # 二维码生成器
├── README.md
└── (未来新增工具的文件夹)
```

## ✨ 如何添加一个新工具？

1. 在根目录下创建新文件夹，例如 `json-formatter/`。
2. 在该文件夹内新建 `index.html`，编写工具代码（纯前端）。
3. 在根目录 `index.html` 的 `.tools-grid` 中添加指向新工具的卡片。
4. 提交并推送：
   ```bash
   git add .
   git commit -m "feat: add new tool"
   git push origin main
   ```
5. GitHub Pages 会自动部署，新工具即可通过 `https://ace-trump-tech.github.io/html-lab/新文件夹名/` 访问。

## 📜 技术栈

- 原生 HTML5 / CSS3 / JavaScript（ES6+）
- 二维码生成使用轻量库 `qrcode-generator`（MIT）
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
```

- **保留了开发相关内容**：本地运行、项目结构、贡献指南依然存在，方便想二次开发的人。

你可以直接用这个内容替换仓库中的 `README.md`。推送后，访客就能一目了然地知道怎么用这个项目了。
