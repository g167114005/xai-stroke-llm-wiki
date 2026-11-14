---
type: concept
title: Grad-CAM（Gradient-weighted Class Activation Mapping）
---
# Grad-CAM（Gradient-weighted Class Activation Mapping）

## 白話解釋
Grad-CAM 會在影像上疊一張「熱圖」，顏色越紅代表模型做判斷時越依賴那一塊。
它的原理是往回追蹤模型最後一層影像特徵對答案的影響。問題是，影像經過很多層壓縮後，最後一層的格子很粗，所以熱圖其實是把一張很小的圖放大貼回原圖，邊緣是糊的。
它只能回答「模型看了哪裡」，不能回答「模型看對了沒」。

## 在中風影像怎麼用
- 多搭配 CNN 或 Vision Transformer，用在 CT 或 MRI 上偵測病灶、標出模型關注的位置 [review, §1]。
- Review 評讀的影像顯著圖研究共 10 篇，定位全都只用眼睛看，沒有量化 [review, §4.4]。
- 解析度粗、容易被假影誤導、看不到非影像變項，詳見 [[gradcam-coarse-and-artifacts]]。

## 相關頁面
[[shap]]、[[gradcam-coarse-and-artifacts]]、[[uncertainty-quantification]]、[[by-xai-paradigm]]、[[review]]
