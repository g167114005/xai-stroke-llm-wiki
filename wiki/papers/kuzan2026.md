---
type: paper
title: DWI 深度學習偵測急性缺血性中風：多中心外部驗證
key: kuzan2026
year: 2026
source_file: The Role of Artificial Intelligence in Diagnosing Acute Ischemic Stroke Using Diffusion MRI_ A Multicenter External Validation Study.pdf
task: 偵測分類
modality: DWI (MRI)
xai: Grad-CAM
validation: 外部驗證（2 家中心）
---
# Kuzan et al.（2026）DWI 深度學習偵測急性缺血性中風：多中心外部驗證

## 一句話
讓 AI 看腦部 MRI 判斷「有沒有中風」，並拿到另外兩家醫院測試，還跟放射科醫師比較。

## 研究設計
- 回溯性研究，共 732 例（急性缺血性中風與非中風對照），來自 3 家中心 [kuzan2026, p.1]。
- 中心 1 的資料用來訓練（452 例）與內部驗證（80 例）；中心 2、3 各 100 例只做外部驗證 [kuzan2026, p.1]。
- 所有影像先對同一張參考影像做 histogram matching [kuzan2026, p.3]。

## 模型與結果
- 模型：deep CNN
- 內部驗證：敏感度、特異度、準確度皆為 100%，AUC = 1.000 [kuzan2026, p.1]。
- 外部驗證：兩家中心都是敏感度 100%、特異度 98%、準確度 99%；AUC 分別為 0.987 與 0.986 [kuzan2026, p.1]。
- 表現與三位放射科專家相當 [kuzan2026, p.1]。

## XAI 怎麼做
- 用 Grad-CAM 把模型「看哪裡」畫成熱圖 [kuzan2026, p.1]。

## Review 的評論
- Review 選為正文詳述的研究之一 [review, §3]。
- Grad-CAM 熱圖大致對得上醫師標的病灶，但在病灶邊緣有局部對不準，review 認為這是深層特徵圖被降採樣後解析度不足造成的 [review, §3.1]。
- 解釋有拿到外部資料上看，但只是用眼睛看（qualitative），沒有量化 [review, §4.4]。
- 偏誤風險 (risk of bias)：High。30 篇裡有 28 篇是 High，只有 Li 與 Huang H. 兩篇是 Unclear，沒有任何一篇是 Low [review, §2]。

## 相關頁面
- 觀念：[[grad-cam]]、[[stroke-terms]]、[[auc]]、[[external-validation]]
- 議題：[[gradcam-coarse-and-artifacts]]、[[explanation-validity-untested]]
- 比較：[[by-task]]、[[by-xai-paradigm]]
- 裁判來源：[[review]]
