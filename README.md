# 🧰 HTML Lab · 在线工具集

> 轻量、纯粹、无服务端 —— 所有工具均在浏览器本地运行，绝不收集任何数据。

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-brightgreen)](https://ace-trump-tech.github.io/html-lab/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## 📌 项目简介

`html-lab` 是一个基于 **GitHub Pages** 的在线工具集合，目前已炼成 **30 件仙器**，涵盖编解码、格式化、生成器、图片处理、文本处理等分类。每个工具都是独立的 HTML 页面，无需后端，数据永不离开你的浏览器。

## 🚀 如何使用（直接访问）

### 主站首页
**[https://ace-trump-tech.github.io/html-lab/](https://ace-trump-tech.github.io/html-lab/)**  
首页以卡片形式展示所有可用工具，点击即可跳转。

## 🚀 当前已上线工具（30 件）

### 🪄 镇阁仙器

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **Base64 编码/解码** | [base64/](https://ace-trump-tech.github.io/html-lab/base64/) | 支持 UTF-8 文本（中文、emoji），在线编码解码，一键复制结果。 |
| **二维码生成器** | [qrcode/](https://ace-trump-tech.github.io/html-lab/qrcode/) | 输入文本或网址，实时生成 QR Code，可下载为 PNG 图片。 |
| **Markdown 在线预览** | [markdown-preview/](https://ace-trump-tech.github.io/html-lab/markdown-preview/) | 左栏编辑右栏实时预览，快捷插入工具栏，可复制渲染后的 HTML。 |
| **文本差异对比** | [diff-checker/](https://ace-trump-tech.github.io/html-lab/diff-checker/) | 两段文本逐行 Diff，新增绿色标记、删除红色标记，统计增删行数。 |
| **字数 & 字节统计器** | [word-counter/](https://ace-trump-tech.github.io/html-lab/word-counter/) | 实时统计字符数、字节数（UTF-8）、单词数、中文字符数、阅读时间。 |

### 🖼️ 图片处理

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **图片压缩** | [image-compressor/](https://ace-trump-tech.github.io/html-lab/image-compressor/) | 调整质量与缩放比例，实时预览压缩效果，纯前端 Canvas 处理。 |
| **图片格式转换** | [image-converter/](https://ace-trump-tech.github.io/html-lab/image-converter/) | PNG / JPEG / WebP 格式互转，上传即可下载转换后的图片。 |
| **图片 Base64 转换** | [image-base64/](https://ace-trump-tech.github.io/html-lab/image-base64/) | 图片 ⇄ Base64 字符串互转，支持 Data URI 格式。 |

### 🔤 编码/解码

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **URL 编码/解码** | [url-codec/](https://ace-trump-tech.github.io/html-lab/url-codec/) | encodeURIComponent / encodeURI 双模式，处理中文及特殊字符。 |
| **HTML 实体编解码** | [html-entity/](https://ace-trump-tech.github.io/html-lab/html-entity/) | &amp;lt; ⇄ &lt; 互转，安全处理 HTML 标签和特殊符号。 |
| **Unicode 编解码** | [unicode-codec/](https://ace-trump-tech.github.io/html-lab/unicode-codec/) | \\uXXXX / &#x / &# / U+ 多种格式互转。 |
| **摩斯电码** | [morse-code/](https://ace-trump-tech.github.io/html-lab/morse-code/) | 文本 ⇄ 摩斯电码互转，含字母和数字对照表。 |
| **JWT 解码器** | [jwt-decoder/](https://ace-trump-tech.github.io/html-lab/jwt-decoder/) | 解码 JWT Header 与 Payload，解析标准 Claims，检测过期状态。 |

### 🎲 生成器

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **随机密码生成器** | [password-generator/](https://ace-trump-tech.github.io/html-lab/password-generator/) | 基于 Web Crypto API，可配置长度与字符集，实时显示密码强度。 |
| **UUID 生成器** | [uuid-generator/](https://ace-trump-tech.github.io/html-lab/uuid-generator/) | 使用 crypto.randomUUID()，支持小写/大写/无连字符，可批量生成。 |
| **Lorem Ipsum 生成器** | [lorem-ipsum/](https://ace-trump-tech.github.io/html-lab/lorem-ipsum/) | 拉丁 Lorem Ipsum 或中文乱数假文，支持段落/句子/单词模式。 |
| **哈希生成器** | [hash-generator/](https://ace-trump-tech.github.io/html-lab/hash-generator/) | MD5 / SHA-1 / SHA-256 / SHA-512 摘要生成，基于 CryptoJS。 |

### 📐 格式化/校验

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **JSON 格式化 & 校验** | [json-formatter/](https://ace-trump-tech.github.io/html-lab/json-formatter/) | 格式化、压缩、校验 JSON，语法高亮，错误定位，支持转义/去转义。 |
| **HTML 格式化** | [html-formatter/](https://ace-trump-tech.github.io/html-lab/html-formatter/) | 美化/压缩 HTML 代码，自动缩进。 |
| **CSS 格式化** | [css-formatter/](https://ace-trump-tech.github.io/html-lab/css-formatter/) | 美化/压缩 CSS 样式，自动缩进与换行。 |
| **JavaScript 格式化** | [js-formatter/](https://ace-trump-tech.github.io/html-lab/js-formatter/) | 美化/压缩 JS 代码，去除注释。 |
| **SQL 格式化** | [sql-formatter/](https://ace-trump-tech.github.io/html-lab/sql-formatter/) | 关键字大写、子句换行缩进，支持 SELECT/INSERT/UPDATE/DELETE。 |

### 📝 文本处理

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **正则表达式测试器** | [regex-tester/](https://ace-trump-tech.github.io/html-lab/regex-tester/) | 输入正则与测试文本，实时高亮匹配，显示捕获分组与匹配位置。 |
| **大小写转换** | [case-converter/](https://ace-trump-tech.github.io/html-lab/case-converter/) | UPPER / lower / Title / 驼峰 / 蛇形 / 短横 等多种转换。 |
| **文本去重** | [text-dedup/](https://ace-trump-tech.github.io/html-lab/text-dedup/) | 逐行去重，支持大小写敏感、去除空格、保留空行等选项。 |
| **文本排序** | [text-sorter/](https://ace-trump-tech.github.io/html-lab/text-sorter/) | 字母升序/降序、数字排序、随机打乱、反转顺序。 |

### 🧰 其他工具

| 工具名称 | 直达链接 | 功能说明 |
|---------|----------|----------|
| **Unix 时间戳转换** | [unix-timestamp/](https://ace-trump-tech.github.io/html-lab/unix-timestamp/) | 实时时间戳显示，时间戳与日期双向互转，秒/毫秒自动识别。 |
| **颜色工具** | [color-tools/](https://ace-trump-tech.github.io/html-lab/color-tools/) | 颜色拾取器，HEX / RGB / HSL 三者实时互转，CSS 代码一键复制。 |
| **进制转换** | [base-converter/](https://ace-trump-tech.github.io/html-lab/base-converter/) | 二进制、八进制、十进制、十六进制实时联动互转。 |
| **单位换算** | [unit-converter/](https://ace-trump-tech.github.io/html-lab/unit-converter/) | 长度、重量、温度、数据存储等常用单位换算。 |

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
├── index.html              # 工具集首页（仙器阁 + 分类仙器）
├── base64/                 # Base64 编解码
├── qrcode/                 # 二维码生成器
├── markdown-preview/       # Markdown 在线预览
├── diff-checker/           # 文本差异对比
├── word-counter/           # 字数 & 字节统计器
├── image-compressor/       # 图片压缩
├── image-converter/        # 图片格式转换
├── image-base64/           # 图片 Base64 转换
├── url-codec/              # URL 编码/解码
├── html-entity/            # HTML 实体编解码
├── unicode-codec/          # Unicode 编解码
├── morse-code/             # 摩斯电码
├── jwt-decoder/            # JWT 解码器
├── password-generator/     # 随机密码生成器
├── uuid-generator/         # UUID 生成器
├── lorem-ipsum/            # Lorem Ipsum 生成器
├── hash-generator/         # 哈希生成器
├── json-formatter/         # JSON 格式化 & 校验
├── html-formatter/         # HTML 格式化
├── css-formatter/          # CSS 格式化
├── js-formatter/           # JavaScript 格式化
├── sql-formatter/          # SQL 格式化
├── regex-tester/           # 正则表达式测试器
├── case-converter/         # 大小写转换
├── text-dedup/             # 文本去重
├── text-sorter/            # 文本排序
├── unix-timestamp/         # Unix 时间戳转换
├── color-tools/            # 颜色工具
├── base-converter/         # 进制转换
├── unit-converter/         # 单位换算
└── README.md
```

## ✨ 如何添加一个新工具？

1. 在根目录下创建新文件夹，例如 `my-tool/`。
2. 在该文件夹内新建 `index.html`，编写工具代码（纯前端）。
3. 在根目录 `index.html` 的对应分类中添加工具卡片（仙器阁或分类仙器），并在 `.update-list` 中添加条目。
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
- 图片处理：HTML5 Canvas API
- 随机生成：Web Crypto API
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
