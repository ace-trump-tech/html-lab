# 🧰 HTML Lab · 在线工具集

> 轻量、纯粹、无服务端 —— 所有工具均在浏览器本地运行，绝不收集任何数据。

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen)](https://ace-trump-tech.github.io/html-lab/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## 📌 项目简介

`html-lab` 是一个基于 **GitHub Pages** 的在线工具集合，旨在提供日常开发、调试及隐私保护所需的简洁小工具。每个工具都是独立的 HTML 页面，无需后端，不依赖第三方库，开箱即用。

## 🛠️ 当前工具

| 工具 | 访问路径 | 功能描述 |
|------|----------|----------|
| **Base64 编码/解码** | `/base64-tool/` | 支持 UTF-8 文本（含中文、emoji），本地编码解码，一键复制结果。 |

更多工具正在开发中……（JSON 格式化、时间戳转换、二维码生成等）

## 🚀 在线访问

🔗 **主站**：[https://ace-trump-tech.github.io/html-lab/](https://ace-trump-tech.github.io/html-lab/)

每个子工具均可通过 `https://ace-trump-tech.github.io/html-lab/工具名/` 直接访问。

## 🧪 本地运行

如果你想在本地预览或修改这些工具：

```bash
git clone https://github.com/ace-trump-tech/html-lab.git
cd html-lab
# 使用任意 HTTP 服务器，例如 Python 3
python -m http.server 8080
```
打开浏览器访问 `http://localhost:8080` 即可。

## 📁 项目结构

```
html-lab/
├── index.html              # 工具集首页（导航卡片）
├── base64-tool/
│   └── index.html          # Base64 编解码工具
├── README.md               # 项目说明
└── (未来新增工具的文件夹)
```

## ✨ 如何添加一个新工具？

1. 在根目录下创建新文件夹，例如 `json-formatter/`。
2. 在该文件夹内新建 `index.html`，编写你的工具代码（完全前端实现）。
3. 在根目录的 `index.html` 的 `.tools-grid` 中添加一个指向新工具的卡片链接。
4. 提交并推送：
   ```bash
   git add .
   git commit -m "feat: add json formatter tool"
   git push origin main
   ```
5. GitHub Pages 会自动部署，访问 `https://ace-trump-tech.github.io/html-lab/新文件夹名/` 即可。

## 📜 技术栈

- 原生 HTML5 / CSS3 / JavaScript（ES6+）
- 无任何第三方框架或库（保持轻量）
- 使用 `TextEncoder` / `TextDecoder` 处理 UTF-8 Base64
- 响应式设计，支持移动端

## 🤝 贡献指南

欢迎提交新工具或改进现有工具！请遵守以下原则：

- **纯前端实现**，不依赖外部 API，不收集用户数据。
- 每个工具独立成一个文件夹，内含 `index.html`。
- 保持界面简洁、易用，风格与现有工具大致统一。
- 提交前请测试工具在主流浏览器（Chrome / Firefox / Edge）上的兼容性。

提交方式：Fork 仓库 → 创建新分支 → 提交 Pull Request。

## 📄 许可证

[MIT](LICENSE) © ace-trump-tech

## 🙏 致谢

项目受开源社区启发，旨在打造一个干净、可信赖的在线工具站点。

---

**⭐ 如果你觉得有用，请给仓库点个 Star！**
```
