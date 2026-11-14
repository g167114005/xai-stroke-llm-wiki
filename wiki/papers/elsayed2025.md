---
type: paper
title: EBDS：ViT＋VGG16 混合模型做 CT 中風診斷
key: elsayed2025
year: 2025
source_file: 41598_2025_Article_14444.pdf
task: 偵測分類
modality: CT
xai: Grad-CAM＋LIME
validation: 內部（Kaggle 公開資料）
---
# Elsayed et al.（2025）EBDS：ViT＋VGG16 混合模型做 CT 中風診斷

## 一句話
把兩種影像模型的特徵合在一起看 CT，判斷有沒有中風。

## 研究設計
- 使用 Kaggle 上公開的資料集訓練與評估 [elsayed2025, p.1]。

## 模型與結果
- 模型：ViT＋VGG16 混合分類器
- 測試準確度 99.6%；stroke 類別 precision 0.98、normal 類別 recall 0.99、整體 F1-score 0.99 [elsayed2025, p.1]。

## XAI 怎麼做
- 用 Grad-CAM 與 LIME 提供視覺化解釋 [elsayed2025, p.1]，Grad-CAM 的說明在 [elsayed2025, p.13]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[grad-cam]]、[[stroke-terms]]、[[auc]]
- 議題：（無特別對應的議題頁）
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
