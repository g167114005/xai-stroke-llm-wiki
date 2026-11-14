---
type: paper
title: Swin Transformer–BiLSTM 與 ensemble 做多模態中風偵測與風險預測
key: ahmedmm2026
year: 2026
source_file: 1-s2.0-S001048252600079X-main.pdf
task: 偵測分類
modality: CT＋臨床資料
xai: LIME＋SHAP＋Attention map＋enhanced Grad-CAM
validation: cross-validation
---
# Ahmed M.M. et al.（2026）Swin Transformer–BiLSTM 與 ensemble 做多模態中風偵測與風險預測

## 一句話
一個模型看 CT 找中風，另一個模型用臨床資料估風險，兩邊都附上解釋。

## 研究設計
- CT 與臨床資料收集自孟加拉多家醫院 [ahmedmm2026, p.1]。
- 以 10-fold cross-validation 評估 [ahmedmm2026, p.8]。

## 模型與結果
- 模型：SwinT–BiLSTM＋ensemble classifier
- 作者報告在自有資料上最高 98% 準確度、AUC 1.00 [ahmedmm2026, p.1]。
- 平均測試準確度 97.80%，precision 97.68%、recall 97.27%、F1-score 97.42% [ahmedmm2026, p.8]。

## XAI 怎麼做
- 影像用 LIME 與 Grad-CAM 標出關鍵區域，表格資料用 LIME 與 SHAP [ahmedmm2026, p.2]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- Review 指出這篇把 SHAP 用在影像／表格分支，但主要歸類為影像顯著圖研究 [review, §4.4]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[grad-cam]]、[[stroke-terms]]、[[auc]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
