#!/usr/bin/env python3
"""③ 證據卡：一張卡只看一個 wiki 頁，把帶出處的句子原樣抽出來並編號。
用法：python tools/cards.py <run 資料夾> <wiki 頁名> [<wiki 頁名> ...]"""
import os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CITE = re.compile(r"\[[a-z0-9]+,\s*(?:p\.\d+|§[A-Za-z0-9.]+)\]")
def main():
    run = sys.argv[1]; out = os.path.join(ROOT, run, "03_cards"); os.makedirs(out, exist_ok=True)
    idx = {os.path.splitext(os.path.basename(p))[0]: p for p in glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True)}
    for name in sys.argv[2:]:
        text = open(idx[name], encoding="utf-8").read()
        title = re.search(r"^title: (.+)$", text, re.M).group(1)
        body = text.split("\n---\n", 1)[1]
        sec, n, lines = "", 0, [f"# 證據卡：{name}", "", f"來源頁：`{os.path.relpath(idx[name], ROOT).replace(os.sep, '/')}`（{title}）", ""]
        for raw in body.splitlines():
            s = raw.strip()
            if s.startswith("## "):
                sec = s[3:]; continue
            if sec == "相關頁面" or not CITE.search(s) or s.startswith("|---"):
                continue
            for part in ([s] if s.startswith("|") else re.split(r"(?<=[\]。])\n", s)):
                n += 1
                part = re.sub(r"^[-\d.]+\s*", "", part).replace("[[", "").replace("]]", "")
                lines.append(f"- **C{n}**〔{sec}〕{part}")
        open(os.path.join(out, name + ".md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
        print(f"{name}: {n} 條")
if __name__ == "__main__":
    main()
