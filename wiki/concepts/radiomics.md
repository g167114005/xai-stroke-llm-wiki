---
type: concept
title: Radiomics（影像組學）
---
# Radiomics（影像組學）

## 白話解釋
人眼看影像看的是形狀與明暗；radiomics 是用程式把一塊影像區域算成幾百、上千個數字，例如亮度分布、紋理粗細、形狀規則程度。這些數字再丟給機器學習模型去找規律。
優點是能抓到人眼看不出的細節；缺點是數字太多、彼此高度相關，而且同一個病灶換一台機器掃，算出來的數字可能就不一樣。

## 在中風影像怎麼用
- 常與臨床變項、梗塞位置合併，用來預測功能預後或併發症，例如 [[li2026]]、Huang H. et al.（尚未 ingest）、Huang L. et al.（尚未 ingest）。
- 不同掃描儀造成的差異稱為 batch effect；Huang H. et al. 用 ComBat 做校正 [review, §4.3]。
- 特徵彼此相關會讓 SHAP 排名不穩，見 [[shap-feature-dependence]]。

## 相關頁面
[[shap]]、[[external-validation]]、[[validation-stage-discrimination]]、[[by-task]]
