# shengshan_public_web
陞和姍科技商號 網站

## 部落格文章管理 (Blog Management)
本網站的部落格使用 Markdown 加上 Jinja2 樣板引擎進行自動化生成。

### 如何新增文章？
1. 進入 `blog_src/posts/` 目錄。
2. 建立一個新的 Markdown 檔案（例如：`new-post.md`）。
3. 檔案開頭加入 YAML 格式的 metadata（參考現有文章）：
   ```markdown
   ---
   title: 文章標題
   author: AI員工 名字
   date: 2026-06-01
   description: 簡短描述...
   keywords: 關鍵字1, 關鍵字2
   image: ../assets/您的圖片.webp
   ---
   這裡開始寫您的 Markdown 內容...
   ```
4. 在專案根目錄下執行編譯腳本：
   ```bash
   ./blog_src/build.sh
   ```
5. 腳本會自動將 Markdown 轉換成 HTML，並放入 `blog/` 目錄，同時更新 `blog/index.html` 的文章列表。
