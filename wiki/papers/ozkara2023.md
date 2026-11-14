---
type: paper
title: ML 預測遠端中型血管阻塞 (DMVO) 病人的短期預後
key: ozkara2023
year: 2023
source_file: qims-13-09-5815.pdf
task: 功能預後
modality: CT perfusion＋臨床與檢驗
xai: SHAP
validation: 內部（訓練／測試切分）
---
# Ozkara et al. (2023)（2023）ML 預測遠端中型血管阻塞 (DMVO) 病人的短期預後

## 一句話
塞住的是比較小的血管時，預後研究很少；這篇用影像與抽血資料來預測短期恢復。

## 研究設計
- 回溯性世代研究，納入 69 位病人 [ozkara2023, p.5]。
- 資料以 70:30 分成訓練與測試，用 recursive feature elimination 選特徵 [ozkara2023, p.1]。

## 模型與結果
- 模型：XGBoost 等六種演算法
- XGBoost 用十個特徵表現最好：AUROC 0.894、AUPRC 0.756 [ozkara2023, p.1]。

## XAI 怎麼做
- SHAP 排出的重要特徵依序包含 mismatch volume、Tmax >6 s、DWI volume 等 [ozkara2023, p.9]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]
- 議題：[[shap-feature-dependence]]
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
