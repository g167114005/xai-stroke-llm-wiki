# 證據卡：inamdar2026

來源頁：`wiki/papers/inamdar2026.md`（TrustNet：結合不確定性量化與量化 Grad-CAM 的 CT 中風偵測）

- **C1**〔研究設計〕TrustNet 是小型 CNN，結合 Monte Carlo dropout 與量化的 Grad-CAM [inamdar2026, p.1]。
- **C2**〔研究設計〕在 2023 張腦部 CT 上驗證，並與常用分類網路比較 [inamdar2026, p.1]。
- **C3**〔模型與結果〕準確度 94.67%、特異度 100%、敏感度 91.6%、precision 100% [inamdar2026, p.1]。
- **C4**〔XAI 怎麼做〕用 MoRF（most relevant first）擾動曲線檢驗解釋：把模型認為重要的區域拿掉，看預測變多少 [inamdar2026, p.15]。
- **C5**〔XAI 怎麼做〕因為定位較集中、AUPC 較低而選用 Grad-CAM [inamdar2026, p.8]。
- **C6**〔XAI 怎麼做〕用 Pearson correlation coefficient 比較一般推論與 MCD 推論的顯著圖是否一致 [inamdar2026, p.9]。
- **C7**〔Review 的評論〕Review 選為正文詳述的研究之一 [review, §3]。
- **C8**〔Review 的評論〕資料是 2023 張內部切片（來自 94 位病人）加上 2501 張外部公開切片；上面的特異度與敏感度是剔除 34 張高不確定性切片後算的 [review, §3.1]。
- **C9**〔Review 的評論〕以切片而非病人為單位切分資料，又在事後依閾值翻轉標籤，所以 review 認為它是概念展示，不是經臨床驗證的流程 [review, §3.1]。
- **C10**〔Review 的評論〕30 篇中唯一做了量化 fidelity 檢驗（MoRF／AUPC）的研究；但這仍不等於拿病灶遮罩做解剖位置驗證 [review, §4.4]。
- **C11**〔Review 的評論〕偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。
