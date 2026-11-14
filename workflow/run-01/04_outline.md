# ④ 大綱 → ⑤ 人工確認

主題：SHAP 與 Grad-CAM 的方法學限制　讀者：課堂同學與老師　頁數：13

| 頁 | 標題 | 用到的證據卡 |
|---|---|---|
| 1 | 標題頁 | （無，meta） |
| 2 | 為什麼中風影像 AI 需要「解釋」 | stroke-terms、auc、grad-cam、shap、review |
| 3 | 兩種解釋：Grad-CAM 與 SHAP | grad-cam、shap |
| 4 | 我們檢查了什麼 | review |
| 5 | 限制一：特徵彼此相關時，SHAP 排名會跟著算法變 | shap-feature-dependence |
| 6 | 限制二：排名高，不等於有額外價值 | shap-rank-vs-incremental-value、gerbasi2022 |
| 7 | 限制三：Grad-CAM 粗、怕假影、看不到表格資料 | gradcam-coarse-and-artifacts |
| 8 | 限制四：換一家醫院，AUC 會怎麼變？ | validation-stage-discrimination、explanation-validity-untested |
| 9 | 限制五：解釋本身幾乎沒被驗證 | explanation-validity-untested |
| 10 | 限制六：熱圖永遠很肯定 | automation-bias-and-uncertainty |
| 11 | 那該怎麼辦 | shap-feature-dependence、gradcam-coarse-and-artifacts、validation-stage-discrimination、automation-bias-and-uncertainty |
| 12 | 總結 | review |
| 13 | 這份簡報怎麼做的 | （無，meta：流程說明） |

沒用到的卡：li2026、kuzan2026、cao2026、huangl2025、inamdar2026、internal-vs-external、uncertainty-quantification（它們的重點已收在議題卡的「證據」裡；保留備查）。

## ⑤ 人工確認紀錄
- 2026-11-15　AI 提出 12 頁大綱（第 1–12 頁）。
- 使用者回覆：**「加一頁『這份簡報怎麼做的』」** → 退回 ④ 修大綱，新增第 13 頁。
- 修改後即依使用者指示進入 ⑥（使用者的回覆同時是對其餘 12 頁的同意）。
