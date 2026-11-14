---
type: comparison
title: 依臨床任務對照
---
# 依臨床任務對照

## 對照表
| 論文 | 任務 | 影像 | 模型 | XAI | 驗證方式 | review 的偏誤風險 |
|---|---|---|---|---|---|---|
| [[kuzan2026]] | 偵測分類 | DWI (MRI) | deep CNN | Grad-CAM | 外部驗證（2 家中心） | High |
| [[tuxunjiang2025]] | 偵測分類 | 多序列 MRI（DWI、T1WI、T2WI、FLAIR） | Vision Transformer（cross-attention） | Grad-CAM | 外部驗證（2 家中心） | High |
| [[inamdar2026]] | 偵測分類 | CT | 輕量 CNN（TrustNet）＋Monte Carlo dropout | 量化 Grad-CAM＋不確定性量化 (UQ) | 內部切片＋外部公開切片 | High |
| [[hossain2025]] | 偵測分類 | CT | ViT-LSTM | Attention map＋SHAP＋LIME | 內部＋Kaggle 公開資料 | High |
| [[ahmedmm2026]] | 偵測分類 | CT＋臨床資料 | SwinT–BiLSTM＋ensemble classifier | LIME＋SHAP＋Attention map＋enhanced Grad-CAM | cross-validation | High |
| [[lee2023]] | 偵測分類 | DWI (MRI) | Inception-v3、EfficientNet-b0、modified LeNet | Grad-CAM | 內部 | High |
| [[elsayed2025]] | 偵測分類 | CT | ViT＋VGG16 混合分類器 | Grad-CAM＋LIME | 內部（Kaggle 公開資料） | High |
| [[diaz2026]] | 偵測分類 | NCCT | 兩階段 CNN（先分解剖區、再分類） | Grad-CAM | 內部；Kaggle 只驗證前段分類器 | High |
| [[li2026]] | 功能預後 | 多參數 MRI（DWI、FLAIR 等） | 融合模型（LASSO 選特徵） | SHAP | 外部驗證（第 5 家中心） | Unclear |
| [[huangh2026]] | 功能預後 | DWI (MRI) | nomogram（Radscore＋Locscore＋臨床） | SHAP | 外部驗證（5 家中心） | Unclear |
| [[gerbasi2022]] | 功能預後 | 追蹤 DWI＋T2-FLAIR (MRI) | tree ensemble | TreeSHAP | nested cross-validation（無外部驗證） | High |
| [[wangz2025]] | 功能預後 | multi-PLD ASL (MRI) | SVM（comprehensive model） | SHAP | 內部（permutation test） | High |
| [[bacon2026]] | 功能預後 | EEG＋結構 MRI | DS-CMF（雙流跨模態融合） | SHAP（Kernel Explainer） | 內部 cross-validation | High |
| [[ozkara2024]] | 功能預後 | CTA＋CT perfusion | XGBoost（另比較 CatBoost、Random Forest） | SHAP | 內部（單一中心） | High |
| [[zhangl2023]] | 功能預後 | NCCT | SVM（fusion model） | SHAP | 內部測試集（兩中心） | High |
| [[huangl2025]] | 併發症與無效再通 | NCCT＋CTA | 臨床＋radiomics 融合模型 | SHAP | 外部驗證（2 家中心） | High |
| [[cao2026]] | 併發症與無效再通 | 動態 CTA | 多種 ML 模型（Boruta＋LASSO 選特徵） | SHAP（review 另記 LIME） | 外部驗證（另一家醫院） | High |
| [[gu2026]] | 併發症與無效再通 | MRI（梗塞位置與 radiomics） | SVM（Topo-Rad） | SHAP | 外部驗證（另一家醫院） | High |
| [[tang2026]] | 風險與病因 | 頸動脈 CTA | Swin Transformer 特徵＋傳統特徵融合 | SHAP＋Grad-CAM | 內部測試集 | High |
| [[sakai2026]] | 風險與病因 | 頸部 CTA | CatBoost | SHAP | 內部 | High |
| [[leey2026]] | 風險與病因 | 灌流 MRI | XGBoost | SHAP | 內部 | High |
| [[zatcepin2024]] | 其他（影像定量） | TSPO PET＋MRI | random forest regressor | SHAP | leave-one-out | High |
| [[wangm2023]] | 其他（障礙程度分級） | MRI（T2 Propeller） | Random Forest、LDA 等多種模型 | SHAP | 內部 | High |
| [[yin2022]] | 其他（毛毛樣腦血管病） | MRA | ResNet18（transfer learning） | Grad-CAM | 內部測試集 | High |

## 怎麼讀這張表
- 任務分類參考 review 的三個決策點：再灌流分流（偵測分類）、急性併發症、功能預後 [review, §3]；「風險與病因」「其他」是本 wiki 為了放進全部來源而加的分類。
- 「review 的偏誤風險」是預測模型的評等，不是解釋可信度的評等；兩者 review 分開評 [review, §5.4]。
- 名詞看不懂請先讀 [[stroke-terms]]；偏誤風險怎麼評見 [[probast-ai]]。

## 相關頁面
[[by-xai-paradigm]]、[[internal-vs-external]]、[[stroke-terms]]、[[probast-ai]]、[[review]]
