---
type: concept
title: 外部驗證（external validation）
---
# 外部驗證（external validation）

## 白話解釋
模型在 A 醫院的資料上訓練，再拿去 A 醫院沒用過的資料上測，叫內部驗證；拿去 B 醫院的資料上測，叫外部驗證。
就像學生在自己學校的模擬考考得好，不代表去別的學校考也一樣好。不同醫院的機器、掃描方式、病人組成都不同，所以外部驗證才能看出模型能不能「搬家」。

## 在中風影像怎麼用
- Review 以各研究所報告的最高驗證階段來評讀：獨立外部驗證 9 篇、只有內部測試或 cross-validation 21 篇 [review, §2]。
- 外部表現變差是「可攜性」的觀察，不能直接當成開發過程有錯的證明 [review, §5.4]。
- 各研究內部與外部的數字對照見 [[internal-vs-external]]。

## 相關頁面
[[auc]]、[[calibration]]、[[validation-stage-discrimination]]、[[internal-vs-external]]、[[probast-ai]]
