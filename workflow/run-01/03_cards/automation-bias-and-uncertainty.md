# 證據卡：automation-bias-and-uncertainty

來源頁：`wiki/issues/automation-bias-and-uncertainty.md`（熱圖永遠很肯定：自動化偏誤與不確定性）

- **C1**〔問題是什麼〕目前的 Grad-CAM 與 SHAP 多半是「決定性」的：它們一定會給你一張圖或一組數字，但不會告訴你模型自己有多少把握 [review, §5.1]。
- **C2**〔問題是什麼〕遇到訓練時沒看過的情況（像中風的模仿者：偏癱型偏頭痛、局部癲癇、腦炎；或嚴重的移動假影），模型照樣會畫出很亮的熱圖、照樣分配 SHAP 值 [review, §5.1]。
- **C3**〔問題是什麼〕使用者如果把「圖看起來合理」當成「推論是對的」，就是自動化偏誤 (automation bias) [review, §5.1]。
- **C4**〔證據〕inamdar2026：示範把不確定性與熱圖結合、對模糊切片暫緩判讀；但有切片層級資料外洩等問題，不能直接用於臨床 [review, §5.2]。
- **C5**〔Review 的立場〕XAI 必須搭配不確定性量化（Bayesian deep learning、Monte Carlo dropout、deep ensemble、conformal prediction）[review, §5.2]。
- **C6**〔Review 的立場〕法規面：標準的事後視覺化（例如一般的 Grad-CAM）已不再被視為演算法安全或可靠的決定性證據 [review, §5.3]。
- **C7**〔Review 的立場〕臨床轉譯的三項要求：資料來源與隔離的文件證明、跨廠牌的外部驗證、前瞻性臨床效益試驗 [review, §5.3]。
