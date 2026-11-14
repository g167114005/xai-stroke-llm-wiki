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

## 論文頁（已 ingest 31 篇，另加 review）

### 偵測分類
- [[kuzan2026]]：Kuzan et al.（2026）DWI 深度學習偵測急性缺血性中風：多中心外部驗證
- [[tuxunjiang2025]]：Tuxunjiang et al.（2025）Cross-attention ViT 用多序列 MRI 判斷中風嚴重度
- [[inamdar2026]]：Inamdar et al.（2026）TrustNet：結合不確定性量化與量化 Grad-CAM 的 CT 中風偵測
- [[hossain2025]]：Hossain et al.（2025）ViT-LSTM 混合模型做 CT 中風偵測與分類
- [[ahmedmm2026]]：Ahmed M.M. et al.（2026）Swin Transformer–BiLSTM 與 ensemble 做多模態中風偵測與風險預測
- [[lee2023]]：Lee et al.（2023）CNN 在超急性期 DWI 上偵測中風並分類血管供應區
- [[elsayed2025]]：Elsayed et al.（2025）EBDS：ViT＋VGG16 混合模型做 CT 中風診斷
- [[diaz2026]]：Diaz et al.（2026）AGTS-Net：依解剖分區的兩階段 NCCT 中風分類

### 功能預後
- [[li2026]]：Li et al.（2026）多參數 MRI 預測中風預後：梗塞位置＋radiomics＋腦部衰弱度
- [[huangh2026]]：Huang H. et al.（2026）Spatial radiomics nomogram 預測 AIS 不良預後（多中心）
- [[gerbasi2022]]：Gerbasi et al.（2022）追蹤 DWI 與 T2-FLAIR 的 radiomics 對 AIS 預後的價值
- [[wangz2025]]：Wang Z. et al.（2025）多 PLD ASL 全腦與梗塞區 radiomics 預測 AIS 預後
- [[bacon2026]]：Bacon et al.（2026）可解釋的雙流 EEG-MRI 融合找出中風運動恢復的結構—功能特徵
- [[ozkara2024]]：Ozkara et al. (2024)（2024）只用影像參數預測前循環 LVO 病人的功能預後
- [[zhangl2023]]：Zhang L. et al.（2023）NCCT radiomics 預測接受傳統治療的 AIS 病人預後
- [[jabal2022]]：Jabal et al.（2022）可解釋 ML 預測取栓後 3 個月功能預後
- [[ozkara2023]]：Ozkara et al. (2023)（2023）ML 預測遠端中型血管阻塞 (DMVO) 病人的短期預後
- [[liu2025]]：Liu et al.（2025）時間變化與組織層級的側枝循環預測取栓後恢復

### 併發症與無效再通
- [[huangl2025]]：Huang L. et al.（2025）以 ASPECTS 分區做 CT radiomics 預測惡性腦水腫
- [[cao2026]]：Cao et al.（2026）動態 CTA 全腦動靜脈側枝評估預測無效再通
- [[gu2026]]：Gu et al.（2026）梗塞位置圖譜＋radiomics 預測取栓後惡性腦水腫
- [[hu2025]]：Hu et al.（2025）可解釋 ML 預測取栓後臨床無效再灌流

### 風險與病因
- [[tang2026]]：Tang et al.（2026）頸動脈斑塊 CTA 的深度學習＋傳統特徵融合模型預測中風風險
- [[sakai2026]]：Sakai et al.（2026）可解釋 ML 判斷 ESUS 病人的鈣化頸動脈斑塊是不是元兇
- [[leey2026]]：Lee Y. et al.（2026）灌流 MRI 的 hypoperfusion intensity ratio 預測 MCA 阻塞是否源自顱內動脈粥狀硬化
- [[wei2026]]：Wei et al.（2026）CTA 斑塊與血管周圍脂肪 radiomics 預測同側中風復發
- [[zhao2026]]：Zhao et al.（2026）以血管周圍脂肪特徵預測第二型糖尿病病人的中風事件（多中心）

### 其他
- [[zatcepin2024]]：Zatcepin et al.（2024）用機器學習找出簡化 TSPO PET 定量所需的資訊
- [[wangm2023]]：Wang M. et al.（2023）用 MRI 與可解釋 ML 判斷中風病人的認知與運動障礙程度
- [[yin2022]]：Yin et al.（2022）MRA 深度學習區分出血型與缺血型毛毛樣腦血管病
- [[ahmedae2025]]：Ahmed A.E. et al.（2025）急診中風影像 AI 的系統性回顧
