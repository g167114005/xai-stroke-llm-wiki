---
type: paper
title: Explainable AI for Acute Ischemic Stroke Neuroimaging — SHAP 與 Grad-CAM 的 critical review
key: review
year: 2026
source_file: diagnostics-4566489-proof.docx
task: 回顧與方法學評讀
modality: NCCT、CTA、DWI 等
xai: SHAP、Grad-CAM
validation: 不適用（回顧文章）
---
# Review（Cheng et al., MDPI Diagnostics，已接受，校樣）

> 這是本 wiki 的「裁判」來源：其他論文頁與它不一致時，依 AGENTS.md §5 採它的說法。也因此要特別小心，見 [[review-vs-original]]。

## 一句話
把「用 AI 看中風影像、又附上解釋圖」的研究一篇一篇拿出來檢查：模型本身可不可靠？解釋圖可不可信？結論是兩邊都還有很大的問題。

## 研究設計
- 資料庫只查 PubMed/MEDLINE，範圍 1 January 2021 到 15 August 2026；作者明說這不是 PRISMA 系統性回顧，也沒有事先註冊 [review, §2]。
- 找到 34 筆；初篩排除 2 筆、2 筆拿不到全文，最後評讀 30 篇原始研究（24 篇急性 AIS 核心研究＋六篇鄰近的神經血管模型）[review, §2]。
- 其中 8 篇在正文詳述，其餘 22 篇放在補充資料，但全部都做了評讀 [review, §2]。
- 兩套評讀分開做：預測模型的偏誤風險用 [[probast-ai]]；解釋本身用八個面向的 XAI 評讀 [review, §2]。
- 三位醫師各自獨立評分，通訊作者只負責仲裁 [review, §2]。

## 模型與結果
- 整體偏誤風險：High 28 篇（93.3%）、Unclear 兩篇（6.7%，Li et al. 與 Huang H. et al.），沒有一篇是 Low [review, §2]。
- High 主要來自分析領域（Domain 4：26/30，86.7%）[review, §2]。
- 適用性 (applicability) 有高度疑慮的有 19 篇（63.3%）[review, §2]。
- 仲裁前三位評分者的一致性偏低（整體 RoB κ = 0.084），但三人完全一致的研究占 76.7%（23/30）；作者用 kappa paradox 解釋這個落差 [review, §2]。
- 8 篇正文詳述的研究裡，只有四篇報告了 calibration [review, §5.4]。

## XAI 怎麼做
- 依主要的解釋方式分兩群：影像顯著圖（Grad-CAM 類，n = 10）與特徵歸因（SHAP，n = 20）[review, §4.4]。
- 20 篇 SHAP 研究沒有任何一篇交代 background/reference distribution [review, §4.4]。
- 10 篇影像顯著圖研究的定位全都只做質性評估（用眼睛看代表性熱圖）[review, §4.4]。
- 只有一篇（Inamdar et al.）做了量化的解釋 fidelity 檢驗 [review, §4.4]。
- 有把解釋拿到外部資料檢視的只有兩篇，而且都是質性的 [review, §4.4]。
- 30 篇中有 10 篇（33.3%）的解釋性主張被評為 overstated [review, §4.4]。

## Review 的評論
- 結論：Grad-CAM 熱圖與 SHAP 排名可以輔助解讀，但「看起來合理」加上「AUC 很高」，不能證明解釋是忠實的，更不能證明因果 [review, §7]。
- 作者自己列的限制：只查一個資料庫、只收英文文獻 [review, §2]；評分者間一致性偏低，不能排除評分者或仲裁者門檻的共同影響 [review, §5.4]。
- 撰寫過程使用了大型語言模型協助摘要、抽取與統計計算，並由作者對照全文稽核 [review, §2]。

## 相關頁面
- 觀念：[[shap]]、[[grad-cam]]、[[probast-ai]]、[[uncertainty-quantification]]、[[external-validation]]、[[calibration]]、[[stroke-terms]]
- 議題：[[shap-feature-dependence]]、[[shap-rank-vs-incremental-value]]、[[gradcam-coarse-and-artifacts]]、[[validation-stage-discrimination]]、[[explanation-validity-untested]]、[[automation-bias-and-uncertainty]]、[[review-vs-original]]
- 比較：[[by-task]]、[[by-xai-paradigm]]、[[internal-vs-external]]
