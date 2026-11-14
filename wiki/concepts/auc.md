---
type: concept
title: AUC（ROC 曲線下面積）
---
# AUC（ROC 曲線下面積）

## 白話解釋
AUC 是衡量「模型分不分得出兩群人」的分數，介於 0 與 1 之間。隨便抽一個有病的與一個沒病的，模型給有病的那位較高分數的機率，就是 AUC。亂猜大約是一半，越接近 1 越好。
要注意：AUC 高只代表「排序排得對」，不代表模型給的機率準不準（那是 [[calibration]]），也不代表模型的解釋可信。

## 在中風影像怎麼用
- Review 指出近年的中風影像模型 AUC 常常超過 0.85 到 0.90 [review, §1]。
- 同一個模型在自家資料與別家醫院資料上的 AUC 可能不同，見 [[internal-vs-external]]。
- Review 強調：外部資料上的 AUC 不能當成「解釋也能重現」的證據 [review, §4.4]。

## 相關頁面
[[calibration]]、[[external-validation]]、[[internal-vs-external]]、[[validation-stage-discrimination]]
