---
type: concept
title: SHAP（Shapley Additive exPlanations）
---
# SHAP（Shapley Additive exPlanations）

## 白話解釋
想像一個小組一起完成報告，最後要分功勞。SHAP 的做法是：把每個組員輪流「加入」或「拿掉」，看成績變多少，再平均起來，算出每個人的貢獻。
放到模型上，「組員」就是輸入的特徵（年齡、梗塞體積、某個影像紋理…），「成績」就是模型的預測。SHAP 給每個特徵一個數字，代表它把這次預測往上推或往下拉多少。
它回答的是「**這個模型**怎麼用這些特徵」，不是「這個特徵在人體裡真的造成什麼」。

## 在中風影像怎麼用
- 多用在把臨床分數、灌流指標、radiomics 紋理混在一起的表格式模型，用來排出「哪些特徵最重要」[review, §1]。
- Review 評讀的 SHAP 研究共 20 篇，沒有一篇交代計算時用的 background/reference distribution [review, §4.4]。
- 特徵之間高度相關時，SHAP 的個別排名會隨算法設定而變，詳見 [[shap-feature-dependence]]。
- 排名高不代表有額外預測價值，詳見 [[shap-rank-vs-incremental-value]]。

## 相關頁面
[[grad-cam]]、[[radiomics]]、[[shap-feature-dependence]]、[[shap-rank-vs-incremental-value]]、[[by-xai-paradigm]]、[[review]]
