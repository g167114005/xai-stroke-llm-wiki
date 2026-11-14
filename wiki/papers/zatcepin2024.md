---
type: paper
title: 用機器學習找出簡化 TSPO PET 定量所需的資訊
key: zatcepin2024
year: 2024
source_file: Machinelearning-basedapproachrevealsessential features.pdf
task: 其他（影像定量）
modality: TSPO PET＋MRI
xai: SHAP
validation: leave-one-out
---
# Zatcepin et al.（2024）用機器學習找出簡化 TSPO PET 定量所需的資訊

## 一句話
中風後的腦部發炎要用很麻煩的 PET 檢查來量，這篇想找出哪些資訊就夠用，好把檢查簡化。

## 研究設計
- 18 位缺血性中風病人，接受 [18F]GE-180 PET 與 T1w、FLAIR、ASL MRI [zatcepin2024, p.1]。
- 以 leave-one-out 方式驗證 [zatcepin2024, p.1]。

## 模型與結果
- 模型：random forest regressor
- 最重要的特徵是三個晚期 PET frame 與血漿活性濃度，作者據此測試「晚期 frame 除以血漿濃度」的簡化定量法 [zatcepin2024, p.1]。

## XAI 怎麼做
- 用 SHAP 評估每個特徵對演算法表現的影響 [zatcepin2024, p.5]。

## Review 的評論
- Review 把它放在未於正文詳述的 22 篇之中，但全文仍做了 PROBAST+AI 與 XAI 評讀 [review, §2]。
- fidelity 只有間接證據（用較少特徵的模型來佐證）[review, §4.4] [review, §2]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[stroke-terms]]、[[auc]]
- 議題：[[explanation-validity-untested]]
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
