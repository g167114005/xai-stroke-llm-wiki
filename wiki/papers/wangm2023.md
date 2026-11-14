---
type: paper
title: 用 MRI 與可解釋 ML 判斷中風病人的認知與運動障礙程度
key: wangm2023
year: 2023
source_file: Medical Physics - 2023 - Wang - Diagnosis of cognitive and motor disorders levels in stroke patients through explainable.pdf
task: 其他（障礙程度分級）
modality: MRI（T2 Propeller）
xai: SHAP
validation: 內部
---
# Wang M. et al.（2023）用 MRI 與可解釋 ML 判斷中風病人的認知與運動障礙程度

## 一句話
看 MRI 就估出病人的認知與動作障礙有多嚴重，省下耗時的量表評估。

## 研究設計
- 符合運動障礙分類條件者九十一位、符合認知障礙分類條件者 83 位（原文寫作 Ninety-one 與 83）[wangm2023, p.3]。
- 用 14 種 ML 模型與一種 ensemble 方法預測 Fugl-Meyer 與 MMSE 等級 [wangm2023, p.1]。

## 模型與結果
- 模型：Random Forest、LDA 等多種模型
- 最高準確度：認知障礙 92.0%、運動障礙 82.5% [wangm2023, p.1]。

## XAI 怎麼做
- 用 SHAP 做事後解釋 [wangm2023, p.6]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
