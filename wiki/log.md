# Ingest 與維護紀錄

## 2026-11-15
- ingest `review`：建立 review 頁；依 review 建立 9 個觀念頁、7 個議題頁、3 個比較頁的骨架；更新 index。
- ingest `kuzan2026`（Kuzan et al.）：新增論文頁；加入 by-task、by-xai-paradigm；議題頁新增證據：gradcam-coarse-and-artifacts、explanation-validity-untested；更新 index。
- ingest `tuxunjiang2025`（Tuxunjiang et al.）：新增論文頁；加入 by-task、by-xai-paradigm；議題頁新增證據：gradcam-coarse-and-artifacts、explanation-validity-untested；更新 index。
- ingest `inamdar2026`（Inamdar et al.）：新增論文頁；加入 by-task、by-xai-paradigm；議題頁新增證據：explanation-validity-untested、automation-bias-and-uncertainty；更新 index。
- ingest `li2026`（Li et al.）：新增論文頁；加入 by-task、by-xai-paradigm；議題頁新增證據：shap-feature-dependence、validation-stage-discrimination；更新 index。
- ingest `huangh2026`（Huang H. et al.）：新增論文頁；加入 by-task、by-xai-paradigm；議題頁新增證據：validation-stage-discrimination、review-vs-original；更新 index。
- ingest `gerbasi2022`（Gerbasi et al.）：新增論文頁；加入 by-task、by-xai-paradigm；議題頁新增證據：shap-rank-vs-incremental-value；更新 index。
- ingest `huangl2025`（Huang L. et al.）：新增論文頁；加入 by-task、by-xai-paradigm；議題頁新增證據：validation-stage-discrimination、shap-feature-dependence；更新 index。
- ingest `cao2026`（Cao et al.）：新增論文頁；加入 by-task、by-xai-paradigm；議題頁新增證據：validation-stage-discrimination；更新 index。
- 批次 ingest（8 篇）：
  - `gu2026`（Gu et al.）：新增論文頁、加入比較頁；議題頁新增證據：explanation-validity-untested。
  - `zatcepin2024`（Zatcepin et al.）：新增論文頁、加入比較頁；議題頁新增證據：explanation-validity-untested。
  - `hossain2025`（Hossain et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `ahmedmm2026`（Ahmed M.M. et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `tang2026`（Tang et al.）：新增論文頁、加入比較頁；議題頁新增證據：explanation-validity-untested。
  - `wangz2025`（Wang Z. et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `lee2023`（Lee et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `elsayed2025`（Elsayed et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
- 批次 ingest（8 篇）：
  - `bacon2026`（Bacon et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `ozkara2024`（Ozkara et al. (2024)）：新增論文頁、加入比較頁；議題頁新增證據：shap-feature-dependence。
  - `sakai2026`（Sakai et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `wangm2023`（Wang M. et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `zhangl2023`（Zhang L. et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `yin2022`（Yin et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `diaz2026`（Diaz et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `leey2026`（Lee Y. et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
- 批次 ingest（7 篇）：
  - `ahmedae2025`（Ahmed A.E. et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `jabal2022`（Jabal et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `wei2026`（Wei et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。
  - `ozkara2023`（Ozkara et al. (2023)）：新增論文頁、加入比較頁；議題頁新增證據：shap-feature-dependence。
  - `liu2025`（Liu et al.）：新增論文頁、加入比較頁；議題頁新增證據：validation-stage-discrimination。
  - `zhao2026`（Zhao et al.）：新增論文頁、加入比較頁；議題頁新增證據：validation-stage-discrimination。
  - `hu2025`（Hu et al.）：新增論文頁、加入比較頁；議題頁新增證據：無。

## 2026-11-15　維護與已知限制
- 產出簡報 run-01（主題：SHAP 與 Grad-CAM 的方法學限制）；流程與退回紀錄見 `workflow/run-01/`。
- **閱讀深度的限制（未完全做到 AGENTS.md §7 的「讀全文」）**：review 讀了第 1–5 節全文與第 6–7 節重點；31 篇 PDF 讀的是摘要頁，加上對「SHAP／Grad-CAM／外部驗證／校準／樣本數／AUC」的逐頁定點檢索，不是每一頁都精讀。wiki 上的數字都經 lint 回查到所標頁面，但 Methods 的細節（例如前處理、缺失值處理）沒有收進來。要加深時，請逐篇重新 ingest 並在這裡加一筆。
- **分類的限制**：`by-xai-paradigm` 的逐篇分組、`by-task` 的「風險與病因」「其他」是本 wiki 自己歸的；review 的逐篇編碼在補充資料（Table S3、S6），不在 `raw/` 裡。哪六篇屬於 review 所說的「鄰近神經血管模型」也因此沒有標。
- **待人工確認**：`review-vs-original` 登記 1 筆不一致（Huang H. et al. 的位置模型 AUC）。

## 2026-11-23　review 正式刊登後的更新
- review 已刊登：*Diagnostics* 2026, 16, 3833（Published 17 November 2026），https://www.mdpi.com/2075-4418/16/22/3833 。新增來源 `reviewpub`（正式刊登版 PDF）作為對照；原本依校樣 ingest 的 `review` 與章節出處不動。
- **回查**：wiki 中所有帶 `[review, §…]` 出處的句子共 164 個數字，逐一對刊登版全文，全部找得到（0 個不符）。也就是說，從校樣到刊登，wiki 引用到的數字沒有變動。
- **`review-vs-original` 的那一筆結案**：Huang H. et al. 位置模型 AUC，刊登版維持 0.791，並在 Table 1 標明是 XGB 模型；原文摘要的 0.793 是表現最佳模型的數字。兩者是不同演算法的結果，不是抄錯。紀錄保留，並補上說明。
- 更新 `review` 頁（刊登資訊、全文連結、DOI）、`index`、`huangh2026`、`AGENTS.md`、README 與網站首頁。簡報內容未更動（它不含刊登狀態的文字）。
