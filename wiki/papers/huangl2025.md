---
type: paper
title: 以 ASPECTS 分區做 CT radiomics 預測惡性腦水腫
key: huangl2025
year: 2025
source_file: Development and validation of a radiomics model based on the ASPECTS framework using CT imaging for predicting malignant cerebral edema.pdf
task: 併發症與無效再通
modality: NCCT＋CTA
xai: SHAP
validation: 外部驗證（2 家中心）
---
# Huang L. et al.（2025）以 ASPECTS 分區做 CT radiomics 預測惡性腦水腫

## 一句話
不用醫師手動圈出梗塞範圍，直接從 CT 的固定分區抽特徵，預測病人會不會發生危險的腦水腫。

## 研究設計
- 多中心回溯性研究，5 家中風中心共 708 位病人 [huangl2025, p.1]。
- 3 家中心的資料以 7:3 分成訓練與內部驗證，其餘 2 家做外部驗證 [huangl2025, p.3]。
- development 506 人、外部驗證 202 人 [huangl2025, p.4]。

## 模型與結果
- 模型：臨床＋radiomics 融合模型
- 融合模型 AUC：訓練 0.91、內部驗證 0.78（95 %CI：0.70–0.87）、外部驗證 0.88（95 %CI：0.82–0.94）[huangl2025, p.1]。
- 外部驗證中，只用臨床變項的模型 AUC 為 0.71 [huangl2025, p.1]。
- 在外部資料上，各模型的校準 (calibration) 普遍變差 [huangl2025, p.5]。

## XAI 怎麼做
- 用 SHAP 解釋特徵貢獻；最重要的包括 ASPECTS 與 NIHSS [huangl2025, p.1]，review 另列出多期側枝循環分數 (CS) [review, §3.3]。

## Review 的評論
- Review 選為正文詳述的研究之一 [review, §3]。
- 直接從 ASPECTS 分區抽特徵，避開了「手動圈梗塞」這個臨床瓶頸 [review, §3.3]。
- 內部 0.78 → 外部 0.88（Δ = +0.100）[review, §4.3]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]、[[radiomics]]、[[external-validation]]
- 議題：[[shap-feature-dependence]]、[[validation-stage-discrimination]]
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
