---
type: concept
title: 校準（calibration）
---
# 校準（calibration）

## 白話解釋
模型說「這位病人有七成機率預後不好」，那麼在所有被說七成的病人裡，真的應該大約七成預後不好。說的機率與實際發生的比例對得上，就叫校準良好。
一個模型可以很會排序（[[auc]] 高）卻校準很差，例如把所有人的風險都報得太高。臨床上要拿機率來做決定時，校準比排序更要緊。

## 在中風影像怎麼用
- Review 指出，反覆出現的分析缺失之一就是沒有評估機率校準；8 篇正文詳述的研究中只有四篇報告了 calibration [review, §5.4]。
- Huang L. et al. 在外部資料上各模型的校準普遍變差 [huangl2025, p.5]。
- Cao et al. 除了 AUC 下降，也出現校準漂移 [review, §3.3]。

## 相關頁面
[[auc]]、[[external-validation]]、[[probast-ai]]、[[uncertainty-quantification]]
