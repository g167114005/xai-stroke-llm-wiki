# 目錄

主題：可解釋 AI（SHAP、Grad-CAM）用在急性缺血性中風神經影像。規則見專案根目錄的 `AGENTS.md`。

第一次來：先讀 [[stroke-terms]] → [[shap]] → [[grad-cam]] → [[review]]。

## 裁判來源
- [[review]]：我們的 critical review（MDPI Diagnostics，已接受）

## 觀念頁
- [[shap]]：SHAP（Shapley Additive exPlanations）
- [[grad-cam]]：Grad-CAM（Gradient-weighted Class Activation Mapping）
- [[radiomics]]：Radiomics（影像組學）
- [[auc]]：AUC（ROC 曲線下面積）
- [[external-validation]]：外部驗證（external validation）
- [[calibration]]：校準（calibration）
- [[probast-ai]]：PROBAST+AI（預測模型偏誤風險評估工具）
- [[uncertainty-quantification]]：不確定性量化（uncertainty quantification, UQ）
- [[stroke-terms]]：中風影像常見名詞（給非醫療背景的讀者）

## 議題頁
- [[shap-feature-dependence]]：SHAP 遇到彼此相關的特徵：排名會跟著算法設定變
- [[shap-rank-vs-incremental-value]]：SHAP 排名高，不等於有額外的預測價值
- [[gradcam-coarse-and-artifacts]]：Grad-CAM 的三個弱點：解析度粗、怕假影、看不到非影像資料
- [[validation-stage-discrimination]]：換一家醫院，AUC 會怎麼變？結果並不一致
- [[explanation-validity-untested]]：解釋本身幾乎沒有被驗證過
- [[automation-bias-and-uncertainty]]：熱圖永遠很肯定：自動化偏誤與不確定性
- [[review-vs-original]]：Review 與原始論文不一致的地方（依規則採 review，但全部列出）

## 比較頁
- [[by-task]]：依臨床任務對照
- [[by-xai-paradigm]]：依解釋方式對照
- [[internal-vs-external]]：內部 vs 外部驗證的 AUC

## 論文頁（已 ingest 16 篇，另加 review）

### 偵測分類
- [[kuzan2026]]：Kuzan et al.（2026）DWI 深度學習偵測急性缺血性中風：多中心外部驗證
- [[tuxunjiang2025]]：Tuxunjiang et al.（2025）Cross-attention ViT 用多序列 MRI 判斷中風嚴重度
- [[inamdar2026]]：Inamdar et al.（2026）TrustNet：結合不確定性量化與量化 Grad-CAM 的 CT 中風偵測
- [[hossain2025]]：Hossain et al.（2025）ViT-LSTM 混合模型做 CT 中風偵測與分類
- [[ahmedmm2026]]：Ahmed M.M. et al.（2026）Swin Transformer–BiLSTM 與 ensemble 做多模態中風偵測與風險預測
- [[lee2023]]：Lee et al.（2023）CNN 在超急性期 DWI 上偵測中風並分類血管供應區
- [[elsayed2025]]：Elsayed et al.（2025）EBDS：ViT＋VGG16 混合模型做 CT 中風診斷

### 功能預後
- [[li2026]]：Li et al.（2026）多參數 MRI 預測中風預後：梗塞位置＋radiomics＋腦部衰弱度
- [[huangh2026]]：Huang H. et al.（2026）Spatial radiomics nomogram 預測 AIS 不良預後（多中心）
- [[gerbasi2022]]：Gerbasi et al.（2022）追蹤 DWI 與 T2-FLAIR 的 radiomics 對 AIS 預後的價值
- [[wangz2025]]：Wang Z. et al.（2025）多 PLD ASL 全腦與梗塞區 radiomics 預測 AIS 預後

### 併發症與無效再通
- [[huangl2025]]：Huang L. et al.（2025）以 ASPECTS 分區做 CT radiomics 預測惡性腦水腫
- [[cao2026]]：Cao et al.（2026）動態 CTA 全腦動靜脈側枝評估預測無效再通
- [[gu2026]]：Gu et al.（2026）梗塞位置圖譜＋radiomics 預測取栓後惡性腦水腫

### 風險與病因
- [[tang2026]]：Tang et al.（2026）頸動脈斑塊 CTA 的深度學習＋傳統特徵融合模型預測中風風險

### 其他
- [[zatcepin2024]]：Zatcepin et al.（2024）用機器學習找出簡化 TSPO PET 定量所需的資訊
