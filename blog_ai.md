# 陞和姍科技商號 AI 員工部落格管理指南 (SOP)

哈囉！未來的 AI 同事，我是負責建立這個部落格自動化系統的 AI 助理。
當你被指派要「新增」或「修改」部落格文章時，請嚴格遵循以下標準作業程序（SOP），以確保整個網站的穩定性與 SEO 品質。

## 1. 了解系統架構

本網站的部落格**不是**手動去改 HTML 檔案！而是使用「Markdown 撰寫 + 腳本自動生成 HTML」的架構。

核心目錄在 `blog_src/` 底下：
* `blog_src/posts/`：存放所有文章的 Markdown (`.md`) 原始檔。**你只需要在這裡新增或修改檔案。**
* `blog_src/templates/`：存放用來產生 HTML 的 Jinja2 樣板 (請不要隨意更動，除非接到修改版面的任務)。
* `blog_src/build.sh`：編譯腳本，執行它就會把 Markdown 轉成 `blog/*.html`。

## 2. 新增文章流程

### 步驟 2-1: 建立 Markdown 檔案
請在 `blog_src/posts/` 下建立一個新的 `.md` 檔案。檔名請使用英文與連字號，例如 `future-of-ai.md`（這會成為未來的網址：`/blog/future-of-ai.html`）。

### 步驟 2-2: 填寫 YAML Metadata (檔案最開頭)
每個 Markdown 檔案的最上方**必須**包含以下格式的 YAML 區塊。這是 SEO 和版面渲染的關鍵：

```markdown
---
title: 文章的完整標題
author: AI員工 你的名字 (例如: AI員工 Lora)
date: YYYY-MM-DD (例如: 2026-06-15)
description: 這裡填寫大約 50~100 字的文章摘要，這會顯示在部落格列表和 Google 搜尋結果中。
keywords: 關鍵字1, 關鍵字2, 陞和姍, AI員工
image: ../assets/你的圖片檔名.webp
---

這裡開始寫文章的正文...
```

**⚠️ 圖片處理注意事項**：
* 所有的文章圖片請統一放在根目錄的 `assets/` 資料夾下。
* 請一律將圖片轉換成 **.webp** 格式以優化載入速度。
* `image` 欄位的值必須是 `../assets/圖片名稱.webp`。

### 步驟 2-3: 撰寫文章內容
* 使用標準 Markdown 語法（`#`, `##`, `*`, `**` 等）撰寫內容。
* 如果要在文章內放入超連結，請加上 `target="_blank" rel="noopener noreferrer"` 以符合我們的安全與體驗規範。
  例如：`<a href="https://example.com" target="_blank" rel="noopener noreferrer">外部連結文字</a>`

### 步驟 2-4: 執行編譯腳本
文章寫好並存檔後，請在專案根目錄執行以下指令：

```bash
./blog_src/build.sh
```

這個腳本會自動：
1. 讀取你寫的 Markdown 檔。
2. 在 `blog/` 目錄下產生對應的 `你的檔名.html`。
3. 自動更新 `blog/index.html` (部落格文章列表)，並將新文章依日期排序在最前面。

### 步驟 2-5: Git 提交流程
確認編譯成功且無錯誤後，請將變更推送到遠端：

```bash
git checkout main
git pull origin main
git add blog_src/posts/你的檔名.md assets/你的圖片.webp blog/
git commit -m "docs(blog): add new post about [文章主題]"
git push origin main
```

## 3. 修改現有文章流程
1. 找到 `blog_src/posts/` 下對應的 `.md` 檔案進行修改。
2. 修改完成後，一樣執行 `./blog_src/build.sh`。
3. 執行 Git commit 與 push。
**絕對不要直接去改 `blog/` 底下的 HTML 檔案，因為下次編譯時你的修改就會被覆蓋掉！**

---
祝福你工作順利！
- 前輩 AI 留
