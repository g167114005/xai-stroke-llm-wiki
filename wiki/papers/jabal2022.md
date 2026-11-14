---
type: paper
title: 可解釋 ML 預測取栓後 3 個月功能預後
key: jabal2022
year: 2022
source_file: fneur-13-884693.pdf
task: 功能預後
modality: NCCT＋CTA（自動萃取）
xai: SHAP
validation: 內部（兩中心）
---
# Jabal et al.（2022）可解釋 ML 預測取栓後 3 個月功能預後

## 一句話
病人一到急診，就用當下拿得到的臨床與 CT 資訊，預測取栓三個月後的恢復。

## 研究設計
- 兩中心回溯性研究，293 位接受取栓的 AIS 病人 [jabal2022, p.1]。
- 影像生物標記用自動化軟體從 CT 與 CTA 量化 [jabal2022, p.1]。

## 模型與結果
- 模型：ML 模型（臨床、影像、合併）
- 以 90 天 mRS 二分作為預測目標，分別建立臨床、影像與合併模型 [jabal2022, p.1]。

## XAI 怎麼做
- 用 SHAP 做特徵重要性分析 [jabal2022, p.3]，並可逐一檢視每位病人的預測 [jabal2022, p.4]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
