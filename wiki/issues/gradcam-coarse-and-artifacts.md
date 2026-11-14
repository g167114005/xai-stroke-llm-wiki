---
type: issue
title: Grad-CAM 的三個弱點：解析度粗、怕假影、看不到非影像資料
---
# Grad-CAM 的三個弱點：解析度粗、怕假影、看不到非影像資料

## 問題是什麼
1. **解析度粗**：最後一層特徵圖經過多次降採樣，熱圖本質上是一張粗格子圖被內插放大到 512 × 512 的影像上 [review, §4.2]。所以它畫不出缺血半影的細緻邊界、皮質小梗塞或側枝血管床 [review, §4.2]。
2. **怕假影**：NCCT 上靠近顱骨與顱底的 beam-hardening 假影，常造成假陽性的亮區；DWI 上空氣與組織交界的磁化率失真也會 [review, §4.2]。
3. **看不到非影像變項**：Grad-CAM 只能作用在像素上，無法呈現發病到院時間、血糖、入院 NIHSS 這些表格資料與影像之間的交互作用 [review, §4.2]。

## 證據
- （目前已 ingest 的論文中還沒有對應的證據）

## Review 的立場
- 未來應改用較高解析度的變體（例如 Guided Grad-CAM、Grad-CAM++），並採用能同時解釋影像熱圖與臨床表格變項的多模態架構 [review, §4.2]。
- 給第一線急診用的視覺解釋，應該與預測準確度接受同等級的客觀驗證，不能停在「看起來合理」[review, §6.2]。

## 相關頁面
[[grad-cam]]、[[explanation-validity-untested]]、[[uncertainty-quantification]]、Kuzan et al.（尚未 ingest）
