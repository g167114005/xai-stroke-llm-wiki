---
type: paper
title: NCCT radiomics 預測接受傳統治療的 AIS 病人預後
key: zhangl2023
year: 2023
source_file: PIIS0720048X23002735.pdf
task: 功能預後
modality: NCCT
xai: SHAP
validation: 內部測試集（兩中心）
---
# Zhang L. et al.（2023）NCCT radiomics 預測接受傳統治療的 AIS 病人預後

## 一句話
只用最基本、不打顯影劑的 CT，預測病人出院半年後的狀況。

## 研究設計
- 兩中心回溯性研究，240 位接受傳統治療的 AIS 病人 [zhangl2023, p.1]。
- 從 NCCT 抽出 1454 個 texture 特徵 [zhangl2023, p.1]。

## 模型與結果
- 模型：SVM（fusion model）
- 測試集 AUC：radiomics 模型 0.705、fusion 模型 0.857、臨床模型 0.643 [zhangl2023, p.1]。
- fusion 模型準確度 84.8%、敏感度 93.8% [zhangl2023, p.1]。

## XAI 怎麼做
- 用 SHAP 分析各特徵的貢獻 [zhangl2023, p.4]，summary 圖在 [zhangl2023, p.5]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]、[[radiomics]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
