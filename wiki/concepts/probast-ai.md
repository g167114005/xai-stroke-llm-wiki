---
type: concept
title: PROBAST+AI（預測模型偏誤風險評估工具）
---
# PROBAST+AI（預測模型偏誤風險評估工具）

## 白話解釋
這是一張給「預測模型研究」用的檢查表，用來判斷研究結果會不會因為做法有問題而過度樂觀。
它分四個領域逐項檢查：病人與資料怎麼來的、預測變項怎麼量的、結果怎麼定義的、統計分析怎麼做的。每個領域評為 Low、Unclear 或 High；只要有一個領域是 High，整體就是 High。
「Unclear」不是「沒問題」，而是「論文沒寫清楚，無法判斷」。

## 在中風影像怎麼用
- Review 用它評讀全部 30 篇，結果 28 篇為 High、兩篇為 Unclear、沒有 Low [review, §2]。
- 問題集中在分析領域（Domain 4：26/30）[review, §2]。
- Review 把「模型的偏誤風險」與「解釋的可信度」分開評，兩者不能互相代替 [review, §5.4]。
- 沒有外部驗證、radiomic 共線性、增益 AUC 不顯著，都不能單獨構成 High [review, §5.4]。

## 相關頁面
[[external-validation]]、[[calibration]]、[[explanation-validity-untested]]、[[review]]
