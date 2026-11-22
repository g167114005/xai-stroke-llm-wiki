---
type: paper
title: Spatial radiomics nomogram 預測 AIS 不良預後（多中心）
key: huangh2026
year: 2026
source_file: Development of a spatial radiomics nomogram for predicting unfavorable outcomes after acute ischemic stroke_A multicenter study.pdf
task: 功能預後
modality: DWI (MRI)
xai: SHAP
validation: 外部驗證（5 家中心）
---
# Huang H. et al.（2026）Spatial radiomics nomogram 預測 AIS 不良預後（多中心）

## 一句話
把「梗塞在大腦哪個位置」變成分數，加上影像紋理與臨床資料，預測三個月後的恢復情況。

## 研究設計
- 多中心回溯性研究：訓練 3,502 人、外部驗證 421 人 [huangh2026, p.1]。
- 中心 1、2 的病人做訓練，中心 3–7 做外部驗證 [huangh2026, p.2]。
- 不良預後定義為 mRS 3–6；位置特徵是把梗塞遮罩對到 425 區的腦圖譜 [huangh2026, p.1]。

## 模型與結果
- 模型：nomogram（Radscore＋Locscore＋臨床）
- 位置模型優於 radiomics 模型：AUC 0.793 vs 0.767（p < 0.01）[huangh2026, p.1]。
- 最終 nomogram 的 AUC：訓練 0.894、外部驗證 0.874 [huangh2026, p.1]。
- 校準用 calibration curve 與 Brier score 評估 [huangh2026, p.3]。

## XAI 怎麼做
- SHAP 用在最佳的位置模型，最有影響力的區域：superior corona radiata、superior longitudinal fasciculus、internal capsule、precentral gyrus [huangh2026, p.1]。

## Review 的評論
- Review 選為正文詳述的研究之一 [review, §3]。
- Review 記載：7 家中心、分析 3923 人（收案 4891、排除 968）[review, §3.2]。
- ⚠ 不一致：review 寫位置模型 AUC 為 0.791 [review, §3.2]；原文摘要寫 0.793 [huangh2026, p.1]（原文表格中 0.791 與 0.793 都出現，分屬不同演算法 [huangh2026, p.6]）。本 wiki 依規則採 review。正式刊登版維持 0.791，並在 Table 1 標明這是 XGB 模型的數字 [reviewpub, p.6]；所以兩邊引的是不同演算法的結果，不是抄錯。
- 用 empirical-Bayes ComBat 處理不同掃描儀造成的 batch effect；但外部 AUC 維持住，並不能證明是 harmonization 的功勞 [review, §4.3]。
- 沒有獨立的內部驗證階段，所以 review 不把它當成「內部→外部」的配對比較 [review, §4.3]。
- 偏誤風險：Unclear，理由同 Li et al.（未交代流程隔離）[review, §5.4]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]、[[radiomics]]、[[external-validation]]
- 議題：[[validation-stage-discrimination]]、[[review-vs-original]]
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
