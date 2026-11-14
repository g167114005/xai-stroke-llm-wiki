---
type: issue
title: SHAP 遇到彼此相關的特徵：排名會跟著算法設定變
---
# SHAP 遇到彼此相關的特徵：排名會跟著算法設定變

## 問題是什麼
中風影像的變項常常是「同一件事的不同量法」：ASPECTS、梗塞體積、灌流不足體積、年齡、白質病變彼此相關 [review, §4.1]。
SHAP 要算「拿掉某個特徵會怎樣」，就得假設拿掉後用什麼值來補。不同的補法（interventional／marginal、conditional、tree path-dependent）回答的其實是不同的問題 [review, §4.1]。
用 marginal 的補法時，可能會評估到現實中幾乎不存在的特徵組合 [review, §4.1]。

## 證據
- [[li2026]]：SHAP 排名靠前的 lentiform nucleus 病灶負荷、WMH、M6 病灶負荷彼此可能相關，個別排名不宜當成獨立的生物效應 [review, §4.1] [li2026, p.2]。
- [[huangl2025]]：SHAP 排名靠前的 ASPECTS、NIHSS、側枝循環分數屬於 review 所說彼此相依的中風變項 [review, §3.3] [review, §4.1]。
- [[ozkara2024]]：只用影像參數建模，候選變項包含多個 CBV 閾值、mismatch ratio、hypoperfusion index 與數種側枝循環分數 [ozkara2024, p.3]，正是 review 所說彼此相依的變項 [review, §4.1]。

## Review 的立場
- 特徵獨立並不是 Shapley value 的公理；相關特徵之間功勞怎麼分，是所選 value function 的結果，不是演算法「出錯」[review, §4.1]。
- 個別 SHAP 值是「這個模型」的解釋量，不是唯一的生物或因果效應 [review, §4.1]。
- Group-SHAP 可以估計一組生理相關特徵的合計貢獻，但它改變的是解釋的對象，並沒有找回生物學的標準答案 [review, §4.1]。
- 建議：作者應交代 explainer 怎麼處理特徵相依與 background/reference distribution，可行時做敏感度分析 [review, §6.1]。

## 相關頁面
[[shap]]、[[radiomics]]、[[shap-rank-vs-incremental-value]]、[[review]]
