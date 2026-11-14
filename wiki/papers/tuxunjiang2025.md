---
type: paper
title: Cross-attention ViT 用多序列 MRI 判斷中風嚴重度
key: tuxunjiang2025
year: 2025
source_file: Prediction of NIHSS Scores and Acute Ischemic Stroke Severity Using a Cross-attention Vision Transformer Model with Multimodal MRI.pdf
task: 偵測分類
modality: 多序列 MRI（DWI、T1WI、T2WI、FLAIR）
xai: Grad-CAM
validation: 外部驗證（2 家中心）
---
# Tuxunjiang et al.（2025）Cross-attention ViT 用多序列 MRI 判斷中風嚴重度

## 一句話
讓 AI 看好幾種 MRI 影像，判斷病人的神經缺損是「輕微」還是「中重度」。

## 研究設計
- 回溯收集 1227 位 AIS 病人，依 NIHSS 分成輕度（< 5）與中重度（≥5）[tuxunjiang2025, p.1]。
- 比較八個模型：臨床模型、radiomics 模型，以及不同融合方式的深度學習模型，深度學習都以 ViT 為基礎 [tuxunjiang2025, p.1]。

## 模型與結果
- 模型：Vision Transformer（cross-attention）
- 最佳的 Model 8（以 DWI 為主、交叉融合其他序列）在測試集 AUC 0.914、ACC 0.830、特異度 0.818、敏感度 0.853 [tuxunjiang2025, p.1]。
- 外部驗證：中心 2 與中心 3 的 AUC 為 0.910 與 0.912 [tuxunjiang2025, p.1]。
- 次族群分析大多穩定，但 BMI 分組有顯著差異（p < 0.001）[tuxunjiang2025, p.1]。

## XAI 怎麼做
- 用 Grad-CAM 產生熱圖，顯示梗塞核心 (infarct core) 是對預測最關鍵的區域 [tuxunjiang2025, p.1]。
- 方法說明在 [tuxunjiang2025, p.8]，熱圖在 [tuxunjiang2025, p.11]。

## Review 的評論
- Review 選為正文詳述的研究之一 [review, §3]。
- Review 記載實際納入分析的是 1162 人（原文寫收集 1227 人，兩者是「收案」與「分析」的差別）[review, §3.1] [tuxunjiang2025, p.1]。
- 熱圖在梗塞核心的權重明顯高於周邊組織 [review, §3.1]。
- 外部資料上的解釋只做了質性檢視 [review, §4.4]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[grad-cam]]、[[stroke-terms]]、[[auc]]、[[radiomics]]、[[external-validation]]
- 議題：[[gradcam-coarse-and-artifacts]]、[[explanation-validity-untested]]
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
