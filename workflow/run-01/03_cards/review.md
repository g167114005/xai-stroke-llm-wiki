# 證據卡：review

來源頁：`wiki/papers/review.md`（Explainable AI for Acute Ischemic Stroke Neuroimaging — SHAP 與 Grad-CAM 的 critical review）

- **C1**〔研究設計〕資料庫只查 PubMed/MEDLINE，範圍 1 January 2021 到 15 August 2026；作者明說這不是 PRISMA 系統性回顧，也沒有事先註冊 [review, §2]。
- **C2**〔研究設計〕找到 34 筆；初篩排除 2 筆、2 筆拿不到全文，最後評讀 30 篇原始研究（24 篇急性 AIS 核心研究＋六篇鄰近的神經血管模型）[review, §2]。
- **C3**〔研究設計〕其中 8 篇在正文詳述，其餘 22 篇放在補充資料，但全部都做了評讀 [review, §2]。
- **C4**〔研究設計〕兩套評讀分開做：預測模型的偏誤風險用 probast-ai；解釋本身用八個面向的 XAI 評讀 [review, §2]。
- **C5**〔研究設計〕三位醫師各自獨立評分，通訊作者只負責仲裁 [review, §2]。
- **C6**〔模型與結果〕整體偏誤風險：High 28 篇（93.3%）、Unclear 兩篇（6.7%，Li et al. 與 Huang H. et al.），沒有一篇是 Low [review, §2]。
- **C7**〔模型與結果〕High 主要來自分析領域（Domain 4：26/30，86.7%）[review, §2]。
- **C8**〔模型與結果〕適用性 (applicability) 有高度疑慮的有 19 篇（63.3%）[review, §2]。
- **C9**〔模型與結果〕仲裁前三位評分者的一致性偏低（整體 RoB κ = 0.084），但三人完全一致的研究占 76.7%（23/30）；作者用 kappa paradox 解釋這個落差 [review, §2]。
- **C10**〔模型與結果〕8 篇正文詳述的研究裡，只有四篇報告了 calibration [review, §5.4]。
- **C11**〔XAI 怎麼做〕依主要的解釋方式分兩群：影像顯著圖（Grad-CAM 類，n = 10）與特徵歸因（SHAP，n = 20）[review, §4.4]。
- **C12**〔XAI 怎麼做〕20 篇 SHAP 研究沒有任何一篇交代 background/reference distribution [review, §4.4]。
- **C13**〔XAI 怎麼做〕10 篇影像顯著圖研究的定位全都只做質性評估（用眼睛看代表性熱圖）[review, §4.4]。
- **C14**〔XAI 怎麼做〕只有一篇（Inamdar et al.）做了量化的解釋 fidelity 檢驗 [review, §4.4]。
- **C15**〔XAI 怎麼做〕有把解釋拿到外部資料檢視的只有兩篇，而且都是質性的 [review, §4.4]。
- **C16**〔XAI 怎麼做〕30 篇中有 10 篇（33.3%）的解釋性主張被評為 overstated [review, §4.4]。
- **C17**〔Review 的評論〕結論：Grad-CAM 熱圖與 SHAP 排名可以輔助解讀，但「看起來合理」加上「AUC 很高」，不能證明解釋是忠實的，更不能證明因果 [review, §7]。
- **C18**〔Review 的評論〕作者自己列的限制：只查一個資料庫、只收英文文獻 [review, §2]；評分者間一致性偏低，不能排除評分者或仲裁者門檻的共同影響 [review, §5.4]。
- **C19**〔Review 的評論〕撰寫過程使用了大型語言模型協助摘要、抽取與統計計算，並由作者對照全文稽核 [review, §2]。
