# 第 10 週作業：把你的工作拆成 AI 能做的流程

北醫 G167114005 醫學院人工智慧醫療碩士在職專班 碩二 鄭為遠
主題：XAI（SHAP／Grad-CAM）於急性缺血性中風神經影像

## 作業三部分在哪裡

| 作業要求 | 成品 | 佐證 |
|---|---|---|
| **建 Wiki**：先討論、後生成；至少 ingest 5 篇 | `wiki/`（53 頁；ingest 32 份來源） | 訪談 `docs/01_訪談紀錄.md` → 需求摘要 `docs/02_需求摘要.md` → 規則 `AGENTS.md`；紀錄 `wiki/log.md`；`git log` |
| **產生 HTML**：設計 Graph 或 Loop 的 workflow，生成簡報 | `slides/index.html`（13 頁，← → 換頁） | Graph 規格 `workflow/GRAPH.md`；執行紀錄 `workflow/run-01/` |
| **反思** | `docs/反思.md`（草稿，請改成自己的話） | — |

## 線上版本
- 首頁：https://g167114005.github.io/xai-stroke-llm-wiki/
- Wiki：https://g167114005.github.io/xai-stroke-llm-wiki/wiki-site/index.html
- 簡報：https://g167114005.github.io/xai-stroke-llm-wiki/slides/index.html
- 繳交內文：`docs/繳交內容.md`；截圖：`screenshots/`

`wiki-site/` 與 `index.html` 由 `python tools/build_site.py` 從 `wiki/` 產生，請勿手改。

## 建議的截圖
1. `docs/01_訪談紀錄.md`（先討論）
2. `AGENTS.md` 第 4、5 節（出處規則、以 review 為準）
3. `git log --oneline`（逐篇 ingest）
4. `python tools/lint.py` 的輸出（全過）
5. `wiki/papers/huangh2026.md`（⚠ 不一致的實例）
6. `workflow/GRAPH.md` 的流程圖
7. `workflow/run-01/06_faithfulness.md`、`08_render_check.md`（退回紀錄）
8. `slides/index.html` 第 8、9 頁

## 怎麼檢查
```
python tools/lint.py                          # wiki：出處、數字、連結、格式
python tools/slides_check.py workflow/run-01  # 簡報：每個要點對得到證據卡
node tools/render_check.js workflow/run-01    # 簡報：版面不溢出
```
需要 Python（`python-docx`，以及 `pdftotext` 或 `pypdf`）；渲染檢查另需 Node、Playwright 與 Chrome。

## 注意
- `raw/` 含尚未刊出的校樣與有版權的 PDF，不進版控，請勿上傳到公開位置。
- 已知限制寫在 `wiki/log.md` 最後一段。
