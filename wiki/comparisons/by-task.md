---
type: comparison
title: 依臨床任務對照
---
# 依臨床任務對照

## 對照表
| 論文 | 任務 | 影像 | 模型 | XAI | 驗證方式 | review 的偏誤風險 |
|---|---|---|---|---|---|---|
| [[kuzan2026]] | 偵測分類 | DWI (MRI) | deep CNN | Grad-CAM | 外部驗證（2 家中心） | High |
| [[tuxunjiang2025]] | 偵測分類 | 多序列 MRI（DWI、T1WI、T2WI、FLAIR） | Vision Transformer（cross-attention） | Grad-CAM | 外部驗證（2 家中心） | High |
| [[inamdar2026]] | 偵測分類 | CT | 輕量 CNN（TrustNet）＋Monte Carlo dropout | 量化 Grad-CAM＋不確定性量化 (UQ) | 內部切片＋外部公開切片 | High |
| [[li2026]] | 功能預後 | 多參數 MRI（DWI、FLAIR 等） | 融合模型（LASSO 選特徵） | SHAP | 外部驗證（第 5 家中心） | Unclear |
| [[huangh2026]] | 功能預後 | DWI (MRI) | nomogram（Radscore＋Locscore＋臨床） | SHAP | 外部驗證（5 家中心） | Unclear |

## 怎麼讀這張表
- 任務分類參考 review 的三個決策點：再灌流分流（偵測分類）、急性併發症、功能預後 [review, §3]；「風險與病因」「其他」是本 wiki 為了放進全部來源而加的分類。
- 「review 的偏誤風險」是預測模型的評等，不是解釋可信度的評等；兩者 review 分開評 [review, §5.4]。
- 名詞看不懂請先讀 [[stroke-terms]]；偏誤風險怎麼評見 [[probast-ai]]。

## 相關頁面
[[by-xai-paradigm]]、[[internal-vs-external]]、[[stroke-terms]]、[[probast-ai]]、[[review]]
