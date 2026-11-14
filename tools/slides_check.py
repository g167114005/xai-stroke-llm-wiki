#!/usr/bin/env python3
"""⑦ 忠實度檢查（程式部分）。用法：python tools/slides_check.py workflow/run-01
規則：每個要點都要有 claim 代號（或標明取自觀念頁的白話解釋，且不含數字）；
要點與圖表裡的數字必須在所引的 claim 文字裡找得到。claim 來自已通過 lint 的 wiki，
所以數字可再往回追到 raw/ 的頁碼。"""
import json, os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools")); import lint
def load_cards(run):
    cards = {}
    for p in glob.glob(os.path.join(ROOT, run, "03_cards", "*.md")):
        name = os.path.splitext(os.path.basename(p))[0]
        for m in re.finditer(r"^- \*\*(C\d+)\*\*〔([^〕]*)〕(.*)$", open(p, encoding="utf-8").read(), re.M):
            cards[f"{name}#{m.group(1)}"] = m.group(3)
    return cards
def items(slide):
    for b in slide.get("bullets", []): yield "要點", b.get("t", ""), b
    for c in slide.get("cols", []):
        for b in c["bullets"]: yield f"欄「{c['h']}」", b["t"], b
    if slide.get("note"): yield "註", slide["note"]["t"], slide["note"]
    v = slide.get("visual")
    if v:
        if v["type"] == "stack": yield "圖", v["label"] + " " + " ".join(f"{p['k']} {p['v']}" for p in v["parts"]), v
        if v["type"] == "pair": yield "圖", f"{v['a']['v']} {v['b']['v']} {v['cap']}", v
        if v["type"] == "bars":
            for r in v["rows"]: yield "圖", f"{r['k']} {r['a']} {r['b']}", r
        if v["type"] == "score":
            for r in v["items"]: yield "圖", f"{r['v']} {r['k']}", r
def main():
    run = sys.argv[1]; cards = load_cards(run)
    d = json.load(open(os.path.join(ROOT, run, "05_drafts.json"), encoding="utf-8"))
    errs, rows, n_item, n_num = [], [], 0, 0
    if not 8 <= len(d["slides"]) <= 15: errs.append(f"頁數 {len(d['slides'])} 不在 8–15")
    for s in d["slides"]:
        bad = 0
        for kind, text, it in items(s):
            n_item += 1
            if it.get("meta"):
                continue
            if it.get("lay"):
                p = os.path.join(ROOT, "wiki", "concepts", it["lay"] + ".md")
                if not os.path.exists(p) or "## 白話解釋" not in open(p, encoding="utf-8").read():
                    errs.append(f"第 {s['n']} 頁 {kind}：白話來源不存在 {it['lay']}"); bad += 1
                if lint.numbers(text):
                    errs.append(f"第 {s['n']} 頁 {kind}：白話要點不可含數字 → {text[:30]}"); bad += 1
                continue
            refs = it.get("refs", [])
            if not refs:
                errs.append(f"第 {s['n']} 頁 {kind}：沒有 claim 代號 → {text[:30]}"); bad += 1; continue
            miss = [r for r in refs if r not in cards]
            if miss:
                errs.append(f"第 {s['n']} 頁 {kind}：claim 不存在 {miss}"); bad += 1; continue
            src = lint.norm(" ".join(cards[r] for r in refs))
            for n in lint.numbers(text):
                n_num += 1
                if not lint.found(n, src):
                    errs.append(f"第 {s['n']} 頁 {kind}：數字「{n}」不在所引 claim 中 → {text[:30]}"); bad += 1
        rows.append(f"| {s['n']} | {s['title']} | {'✅' if not bad else f'❌ {bad}'} |")
    out = ["## 程式檢查", "", f"檢查 {len(d['slides'])} 頁、{n_item} 個要點與圖表項目、{n_num} 個數字；錯誤 {len(errs)} 個。" + (" ✅" if not errs else " ❌"), "",
           "| 頁 | 標題 | 結果 |", "|---|---|---|"] + rows
    if errs: out += ["", "### 錯誤"] + [f"- {e}" for e in errs]
    print("\n".join(out)); return 1 if errs else 0
if __name__ == "__main__": sys.exit(main())
