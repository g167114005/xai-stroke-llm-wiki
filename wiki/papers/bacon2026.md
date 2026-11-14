---
type: paper
title: 可解釋的雙流 EEG-MRI 融合找出中風運動恢復的結構—功能特徵
key: bacon2026
year: 2026
source_file: Interpretable_Dual-Stream_EEG-MRI_Fusion_Uncovers_Structure-Function_Signatures_of_Stroke_Motor_Recovery.pdf
task: 功能預後
modality: EEG＋結構 MRI
xai: SHAP（Kernel Explainer）
validation: 內部 cross-validation
---
# Bacon et al.（2026）可解釋的雙流 EEG-MRI 融合找出中風運動恢復的結構—功能特徵

## 一句話
同時看腦波與 MRI，預測中風病人的手部動作能不能恢復。

## 研究設計
- 26 位亞急性缺血性中風病人，做四種動作想像作業時記錄高密度 EEG，並搭配結構 MRI [bacon2026, p.1]。

## 模型與結果
- 模型：DS-CMF（雙流跨模態融合）
- 內部 cross-validation 中，PGMI 作業準確度 77.3%、WEMI 作業 73.3% [bacon2026, p.1]。

## XAI 怎麼做
- 對融合後的 embedding 用 model-agnostic 的 Kernel Explainer 計算 SHAP [bacon2026, p.7]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
