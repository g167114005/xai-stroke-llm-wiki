# ① 檢索 wiki

主題：**SHAP 與 Grad-CAM 的方法學限制**（讀者：課堂同學與老師）
做法：從 `wiki/index.md` 出發，先取全部議題頁，再取它們「證據」小節連到的論文頁，以及解釋名詞需要的觀念頁。

| 類型 | 頁面 | 為什麼需要 |
|---|---|---|
| 裁判來源 | review | 整體數字（30 篇、偏誤風險、XAI 評讀） |
| 觀念 | shap、grad-cam、uncertainty-quantification | 向非醫療背景的讀者解釋方法 |
| 議題 | shap-feature-dependence | 限制一 |
| 議題 | shap-rank-vs-incremental-value | 限制二 |
| 議題 | gradcam-coarse-and-artifacts | 限制三 |
| 議題 | validation-stage-discrimination | 限制四 |
| 議題 | explanation-validity-untested | 限制五 |
| 議題 | automation-bias-and-uncertainty | 限制六 |
| 比較 | internal-vs-external | 限制四的數字 |
| 論文 | li2026、gerbasi2022、kuzan2026、cao2026、huangl2025、inamdar2026 | 各限制的實例 |

未取用：review-vs-original（與簡報主題無關，是校對用）、by-task、by-xai-paradigm（總覽，簡報不需要逐篇列）。

## 退回紀錄
- **④ → ①（缺題）**：排大綱時發現第 2 頁「為什麼需要解釋」沒有材料（原本只檢索了限制相關的頁面）。依 Graph 規定，④ 不能自己回頭讀 `raw/`，所以退回 ① 補檢索兩個觀念頁：`auc`（AUC 常見的數值範圍）、`stroke-terms`（三個臨床決策點），再重跑 ③ 產生這兩張卡。
