---
type: paper
title: 急診中風影像 AI 的系統性回顧
key: ahmedae2025
year: 2025
source_file: cureus-0017-00000093941.pdf
task: 其他（回顧文章）
modality: NCCT、MRI、CTA 等
xai: 文中提及 Grad-CAM 與 SHAP
validation: 不適用
---
# Ahmed A.E. et al.（2025）急診中風影像 AI 的系統性回顧

## 一句話
這不是原創研究，而是整理別人研究的回顧文章。

## 研究設計
- 依 PRISMA 搜尋 PubMed、Scopus、Web of Science、Cochrane CENTRAL，納入九篇研究，以 CLAIM 評估品質 [ahmedae2025, p.1]。

## 模型與結果
- 模型：（回顧，無自建模型）
- NCCT 偵測顱內出血的 AUC 最高到 0.98；自動 ASPECTS 評分與專家共識的一致性 κ 最高到 0.90 [ahmedae2025, p.1]。

## XAI 怎麼做
- 文中把 Grad-CAM 與 SHAP 描述為能增進信任的工具，同時指出外部驗證與實際整合仍有限 [ahmedae2025, p.2]。

## Review 的評論
- Review 在初篩就把它排除：它是次級的系統性回顧，沒有原始的預測模型 [review, §2]。
- 所以它不在 30 篇被評讀的研究之內 [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[grad-cam]]、[[stroke-terms]]、[[auc]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
