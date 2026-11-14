---
type: comparison
title: 依解釋方式對照（影像顯著圖 vs SHAP）
---
# 依解釋方式對照（影像顯著圖 vs SHAP）

## 對照表
| 論文 | 解釋方式 | 實際用的 XAI 方法 | review 正文對「解釋有沒有被驗證」的說明 |
|---|---|---|---|
| [[kuzan2026]] | 影像顯著圖 | Grad-CAM | 外部資料質性檢視 |
| [[tuxunjiang2025]] | 影像顯著圖 | Grad-CAM | 外部資料質性檢視 |
| [[inamdar2026]] | 影像顯著圖 | 量化 Grad-CAM＋不確定性量化 (UQ) | 量化 fidelity（MoRF／AUPC）；穩定性部分證據 |

## 怎麼讀這張表
- Review 依主要解釋方式把 30 篇分成影像顯著圖（n = 10）與 SHAP 特徵歸因（n = 20）[review, §4.4]。
- 逐篇的分組是本 wiki 依各論文實際使用的方法歸類；review 正文只給總數，逐篇編碼在補充資料 Table S6（不在 `raw/` 中）[review, §2]。
- 最後一欄只收 review 正文有點名的情形；「正文未個別說明」不代表沒問題，整體情形見 [[explanation-validity-untested]]。

## 相關頁面
[[shap]]、[[grad-cam]]、[[explanation-validity-untested]]、[[by-task]]、[[review]]
