---
type: paper
title: 只用影像參數預測前循環 LVO 病人的功能預後
key: ozkara2024
year: 2024
source_file: Journal of Neuroimaging - 2024 - Ozkara - Utilizing imaging parameters for functional outcome prediction in acute ischemic.pdf
task: 功能預後
modality: CTA＋CT perfusion
xai: SHAP
validation: 內部（單一中心）
---
# Ozkara et al. (2024)（2024）只用影像參數預測前循環 LVO 病人的功能預後

## 一句話
完全不看病人的臨床資料，只用 CT 影像量出來的數值，預測三個月後的恢復。

## 研究設計
- 單一中心回溯性研究，180 位病人（102 位女性）；良好預後定義為 90 天 mRS 0-2 [ozkara2024, p.1]。
- 預測變項只包含影像參數 [ozkara2024, p.1]。

## 模型與結果
- 模型：XGBoost（另比較 CatBoost、Random Forest）
- XGBoost 最好：AUROC 0.91、precision 0.72、recall 0.81、AUPRC 0.83、accuracy 0.78、Brier score 0.17 [ozkara2024, p.1]。

## XAI 怎麼做
- 用 SHAP 判斷預測變項的相對重要性 [ozkara2024, p.3]；多期 CTA 側枝循環分數是最重要的特徵 [ozkara2024, p.1]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]
- 議題：[[shap-feature-dependence]]
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
