# 證據卡：huangl2025

來源頁：`wiki/papers/huangl2025.md`（以 ASPECTS 分區做 CT radiomics 預測惡性腦水腫）

- **C1**〔研究設計〕多中心回溯性研究，5 家中風中心共 708 位病人 [huangl2025, p.1]。
- **C2**〔研究設計〕3 家中心的資料以 7:3 分成訓練與內部驗證，其餘 2 家做外部驗證 [huangl2025, p.3]。
- **C3**〔研究設計〕development 506 人、外部驗證 202 人 [huangl2025, p.4]。
- **C4**〔模型與結果〕融合模型 AUC：訓練 0.91、內部驗證 0.78（95 %CI：0.70–0.87）、外部驗證 0.88（95 %CI：0.82–0.94）[huangl2025, p.1]。
- **C5**〔模型與結果〕外部驗證中，只用臨床變項的模型 AUC 為 0.71 [huangl2025, p.1]。
- **C6**〔模型與結果〕在外部資料上，各模型的校準 (calibration) 普遍變差 [huangl2025, p.5]。
- **C7**〔XAI 怎麼做〕用 SHAP 解釋特徵貢獻；最重要的包括 ASPECTS 與 NIHSS [huangl2025, p.1]，review 另列出多期側枝循環分數 (CS) [review, §3.3]。
- **C8**〔Review 的評論〕Review 選為正文詳述的研究之一 [review, §3]。
- **C9**〔Review 的評論〕直接從 ASPECTS 分區抽特徵，避開了「手動圈梗塞」這個臨床瓶頸 [review, §3.3]。
- **C10**〔Review 的評論〕內部 0.78 → 外部 0.88（Δ = +0.100）[review, §4.3]。
- **C11**〔Review 的評論〕偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。
