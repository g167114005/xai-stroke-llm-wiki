---
type: paper
title: ViT-LSTM 混合模型做 CT 中風偵測與分類
key: hossain2025
year: 2025
source_file: 1-s2.0-S0010482525000617-main.pdf
task: 偵測分類
modality: CT
xai: Attention map＋SHAP＋LIME
validation: 內部＋Kaggle 公開資料
---
# Hossain et al.（2025）ViT-LSTM 混合模型做 CT 中風偵測與分類

## 一句話
把兩種深度學習架構接在一起看 CT 找中風，並用三種方法畫出模型看哪裡。

## 研究設計
- 自行收集的 CT 資料，並在 Kaggle brain stroke dataset 上再測一次 [hossain2025, p.1]。

## 模型與結果
- 模型：ViT-LSTM
- 在 Kaggle 資料上準確度 96.61% [hossain2025, p.1]。
- 平均測試準確度 97.61% [hossain2025, p.9]。

## XAI 怎麼做
- 同時使用 Attention map、SHAP、LIME 三種技術 [hossain2025, p.3]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- Review 把它歸為 transformer attention-map 流程，是 10 篇影像顯著圖研究裡唯一不屬 Grad-CAM 家族的 [review, §4.4]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[grad-cam]]、[[stroke-terms]]、[[auc]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
