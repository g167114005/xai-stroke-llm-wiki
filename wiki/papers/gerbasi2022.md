---
type: paper
title: 追蹤 DWI 與 T2-FLAIR 的 radiomics 對 AIS 預後的價值
key: gerbasi2022
year: 2022
source_file: jcdd-09-00468.pdf
task: 功能預後
modality: 追蹤 DWI＋T2-FLAIR (MRI)
xai: TreeSHAP
validation: nested cross-validation（無外部驗證）
---
# Gerbasi et al.（2022）追蹤 DWI 與 T2-FLAIR 的 radiomics 對 AIS 預後的價值

## 一句話
治療後再拍一次 MRI，看影像紋理能不能幫忙預測病人長期恢復得好不好。

## 研究設計
- 病人來自 MR CLEAN-NO IV 臨床試驗 [gerbasi2022, p.1]。
- 用 nested cross-validation 加 grid search，並以 SHAP 值做特徵篩選 [gerbasi2022, p.1]。

## 模型與結果
- 模型：tree ensemble
- 影像加臨床特徵的模型最好：AUC = 0.85，95%CI [0.81, 0.89] [gerbasi2022, p.1]。
- 但與「只用臨床特徵」相比是 0.85 對 0.83，DeLong 檢定 p = 0.33，差異不顯著 [gerbasi2022, p.8]。

## XAI 怎麼做
- 使用 TreeSHAP；每個特徵在內層驗證集上算平均絕對 SHAP 值來排名 [gerbasi2022, p.6]。
- SHAP 顯示兩種序列的影像特徵都有影響，其中 texture heterogeneity 最具預測力 [gerbasi2022, p.1]。

## Review 的評論
- Review 選為正文詳述的研究之一 [review, §3]。
- Review 記載分析人數為 164 人，流失率 69.6% [review, §3.2]。
- Review 用這篇說明：SHAP 排名高，不等於有額外的預測價值 [review, §3.2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]、[[radiomics]]、[[external-validation]]
- 議題：[[shap-rank-vs-incremental-value]]
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
