---
type: paper
title: 多 PLD ASL 全腦與梗塞區 radiomics 預測 AIS 預後
key: wangz2025
year: 2025
source_file: 12880_2025_Article_1807.pdf
task: 功能預後
modality: multi-PLD ASL (MRI)
xai: SHAP
validation: 內部（permutation test）
---
# Wang Z. et al.（2025）多 PLD ASL 全腦與梗塞區 radiomics 預測 AIS 預後

## 一句話
用一種不打顯影劑就能看腦血流的 MRI，預測中風病人的恢復。

## 研究設計
- 110 位 AIS 病人，從全腦與梗塞區的 CBF 影像抽 radiomics 特徵，用五種 ML 演算法建模 [wangz2025, p.1]。
- 以 5000 次 permutation test 評估模型穩定度 [wangz2025, p.1]。

## 模型與結果
- 模型：SVM（comprehensive model）
- 結合 radiomics 與臨床資料的 SVM 模型最好（AUC = 0.904）[wangz2025, p.1]。
- 只用 radiomics 的組合模型與臨床模型之間沒有顯著差異 [wangz2025, p.1]。

## XAI 怎麼做
- 用 SHAP 判斷各特徵對模型表現的貢獻 [wangz2025, p.4]，結果在 [wangz2025, p.5]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]、[[radiomics]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
