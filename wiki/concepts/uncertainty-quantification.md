---
type: concept
title: 不確定性量化（uncertainty quantification, UQ）
---
# 不確定性量化（uncertainty quantification, UQ）

## 白話解釋
一般模型只會給答案，不會說「我其實沒把握」。不確定性量化是讓模型同時回報信心。
常見做法之一是 Monte Carlo dropout：同一張影像讓模型帶著隨機性多算幾次，如果每次答案差很多，就代表它沒把握。
不確定性分兩種：影像本身就模糊（再多資料也沒用），以及模型沒看過這類病人（多給資料可以改善）。

## 在中風影像怎麼用
- Review 主張 XAI 必須搭配不確定性量化，否則遇到沒看過的情況，模型照樣會畫出很肯定的熱圖 [review, §5.1]。
- 實例是 [[inamdar2026]] 的 TrustNet，把 Monte Carlo dropout 與 Grad-CAM 結合 [review, §5.2]。
- 相關風險見 [[automation-bias-and-uncertainty]]。

## 相關頁面
[[grad-cam]]、[[calibration]]、[[automation-bias-and-uncertainty]]、[[inamdar2026]]
