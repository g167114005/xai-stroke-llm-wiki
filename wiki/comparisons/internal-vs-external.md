---
type: comparison
title: 內部驗證 vs 外部驗證的 AUC
---
# 內部驗證 vs 外部驗證的 AUC

## 對照表
| 論文 | 數字來源 | 前一階段 AUC | 外部（或後一階段）AUC | 出處 |
|---|---|---|---|---|
| [[cao2026]] | review 配對 | 0.918 | 0.755 | [review, §4.3] |
| [[li2026]] | review 配對 | 0.84 | 0.86 | [review, §4.3] |
| [[huangl2025]] | review 配對 | 0.78 | 0.88 | [review, §4.3] |
| [[huangh2026]] | review（development→外部，非配對） | 0.894 | 0.874 | [review, §4.3] |
| [[kuzan2026]] | 原文 | 1.000 | 0.987、0.986 | [kuzan2026, p.1] |
| [[tuxunjiang2025]] | 原文（測試集→外部） | 0.914 | 0.910、0.912 | [tuxunjiang2025, p.1] |
| [[zhao2026]] | 原文（內部測試→外部） | 0.847 | 0.856、0.876 | [zhao2026, p.2] |
| [[gu2026]] | 原文（訓練→驗證） | 0.872 | 0.842 | [gu2026, p.1] |

## 怎麼讀這張表
- 「review 配對」是 review 認定的內部驗證對獨立外部驗證配對；其他列的兩個階段不一定是這種配對，括號裡寫明比的是什麼 [review, §4.3]。
- Review 不計算平均下降幅度；這張表要看的是「各研究不一樣」，不是「平均掉多少」[review, §4.3]。
- 觀念見 [[external-validation]] 與 [[auc]]；討論見 [[validation-stage-discrimination]]。

## 相關頁面
[[validation-stage-discrimination]]、[[external-validation]]、[[auc]]、[[by-task]]
