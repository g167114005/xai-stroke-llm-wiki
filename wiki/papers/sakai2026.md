---
type: paper
title: 可解釋 ML 判斷 ESUS 病人的鈣化頸動脈斑塊是不是元兇
key: sakai2026
year: 2026
source_file: Journal of Neuroimaging - 2026 - Sakai - Explainable Machine#U2010Learning Model to Classify Culprit Calcified Carotid Plaque in.pdf
task: 風險與病因
modality: 頸部 CTA
xai: SHAP
validation: 內部
---
# Sakai et al.（2026）可解釋 ML 判斷 ESUS 病人的鈣化頸動脈斑塊是不是元兇

## 一句話
有些中風找不到原因，這篇用 AI 判斷脖子血管上的斑塊是不是兇手。

## 研究設計
- 回溯性橫斷研究：70 位病人、116 個鈣化斑塊（270 處鈣化）[sakai2026, p.4]。
- 比較八種分類器後，進一步調校 CatBoost [sakai2026, p.1]。

## 模型與結果
- 模型：CatBoost
- 用五個特徵的模型 ROC-AUC 0.79、precision-recall-AUC 0.86；優於只看斑塊厚度 ≥3 mm（ROC-AUC 0.59）或有無 IPH（ROC-AUC 0.51）[sakai2026, p.1]。

## XAI 怎麼做
- SHAP 指出斑塊厚度與 PVAT 體積最有影響力，可能的閾值分別是 >2.6 mm 與 ≥112 mm3 [sakai2026, p.1]。
- 用 SHAP waterfall plot 分析分錯的個案 [sakai2026, p.4]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
