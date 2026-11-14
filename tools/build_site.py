#!/usr/bin/env python3
"""把 wiki/ 轉成可瀏覽的靜態網頁（wiki-site/）並產生首頁 index.html，供 GitHub Pages 使用。
只做格式轉換，不改內容。用法：python tools/build_site.py"""
import os, re, glob, html, markdown
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "https://github.com/g167114005/xai-stroke-llm-wiki"
CSS = """:root{--bg:#F6F3EC;--ink:#1A2331;--mut:#5A6475;--rule:#D8D2C5;--acc:#0E6B70;--warn:#B3432A;--card:#FFFDF8}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.75 "Noto Sans TC","PingFang TC","Microsoft JhengHei",system-ui,sans-serif}
header{border-bottom:1px solid var(--rule);background:var(--card)}header div,main{max-width:860px;margin:0 auto;padding:14px 24px}
header a{margin-right:18px;font-weight:600}main{padding-top:28px;padding-bottom:80px}a{color:var(--acc)}
h1{font-size:30px;line-height:1.3;margin:.2em 0 .6em}h2{font-size:21px;margin:1.8em 0 .5em;padding-bottom:4px;border-bottom:2px solid var(--rule)}h3{font-size:18px;margin:1.4em 0 .3em}
table{border-collapse:collapse;width:100%;font-size:15px;margin:1em 0;display:block;overflow-x:auto}th,td{border:1px solid var(--rule);padding:6px 10px;text-align:left;vertical-align:top}th{background:var(--card)}
.meta{font-size:14px;color:var(--mut);background:var(--card);border:1px solid var(--rule);border-radius:8px;padding:10px 16px;margin-bottom:8px}.meta b{color:var(--ink)}
.cite{font:12.5px ui-monospace,Consolas,monospace;color:var(--mut);background:var(--card);border:1px solid var(--rule);border-radius:4px;padding:0 5px;white-space:nowrap}
blockquote{margin:1em 0;padding:8px 16px;border-left:4px solid var(--warn);background:var(--card)}code{background:var(--card);border:1px solid var(--rule);border-radius:4px;padding:0 4px;font-size:.9em}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin:24px 0}.cards a{display:block;background:var(--card);border:1px solid var(--rule);border-top:5px solid var(--acc);border-radius:8px;padding:18px 20px;text-decoration:none;color:var(--ink)}
.cards b{display:block;font-size:20px;color:var(--acc);margin-bottom:4px}.cards span{font-size:15px;color:var(--mut)}"""
def page(title, body, up=""):
    nav = f'<header><div><a href="{up}index.html">首頁</a><a href="{up}wiki-site/index.html">Wiki</a><a href="{up}slides/index.html">簡報</a><a href="{REPO}">GitHub</a></div></header>'
    return f'<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{nav}<main>{body}</main></body></html>'
def main():
    out = os.path.join(ROOT, "wiki-site"); os.makedirs(out, exist_ok=True)
    files = {os.path.splitext(os.path.basename(p))[0]: p for p in glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True)}
    for name, p in files.items():
        text = open(p, encoding="utf-8").read(); meta = ""
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if m:
            kv = [l.split(":", 1) for l in m.group(1).splitlines() if ":" in l]
            meta = '<div class="meta">' + "　".join(f"<b>{html.escape(k.strip())}</b> {html.escape(v.strip())}" for k, v in kv if k.strip() not in ("title",)) + "</div>"
            text = text[m.end():]
        text = re.sub(r"\[\[([^\]]+)\]\]", lambda x: f"[{x.group(1)}]({x.group(1)}.html)" if x.group(1) in files else x.group(1), text)
        text = re.sub(r"\[([a-z0-9]+), (p\.\d+|§[A-Za-z0-9.]+)\]", r'<span class="cite">\1 \2</span>', text)
        text = re.sub(r"(?m)^(?=\S)(?<!\n\n)", "", text)
        body = markdown.markdown(text, extensions=["tables", "sane_lists", "nl2br"])
        title = re.search(r"<h1>(.*?)</h1>", body, re.S)
        open(os.path.join(out, name + ".html"), "w", encoding="utf-8").write(page(re.sub("<.*?>", "", title.group(1)) if title else name, meta + body, "../"))
    n = len(files) - 2
    home = f"""<h1>XAI 中風影像 LLM Wiki</h1>
<p>生成式 AI 課程第 10 週作業｜北醫 G167114005 醫學院人工智慧醫療碩士在職專班 碩二 鄭為遠</p>
<p>主題：可解釋 AI（SHAP、Grad-CAM）用在急性缺血性中風神經影像。先用「先討論、後生成」建立 LLM Wiki（ingest 32 份來源、{n} 頁），再用一張事先畫好的 Graph，只用 wiki 的內容產生教學簡報。</p>
<div class="cards">
<a href="wiki-site/index.html"><b>LLM Wiki</b><span>{n} 頁：論文頁、觀念頁、議題頁、比較頁。每個數字都標到來源頁碼。</span></a>
<a href="slides/index.html"><b>教學 HTML 簡報</b><span>解釋，不等於可信：SHAP 與 Grad-CAM 的六個方法學限制（13 頁，← → 換頁）</span></a>
<a href="{REPO}/blob/main/workflow/GRAPH.md"><b>Graph 設計</b><span>十個節點、每關只能看什麼、錯在哪一關就退回哪一關。</span></a>
<a href="{REPO}/tree/main/workflow/run-01"><b>一次實際執行的紀錄</b><span>檢索、覆蓋率、證據卡、大綱、逐頁稿、忠實度報告、渲染檢查報告與截圖。</span></a>
<a href="{REPO}/blob/main/AGENTS.md"><b>AGENTS.md</b><span>訪談後寫成的規則：出處到頁碼、數字可回查、矛盾時以 review 為準。</span></a>
<a href="{REPO}/blob/main/docs/01_訪談紀錄.md"><b>訪談紀錄</b><span>先討論：AI 問了八題，確認需求摘要後才建檔。</span></a>
</div>
<p style="color:var(--mut);font-size:15px">原始論文 PDF 與尚未刊出的校樣不在此公開；來源清單見 <a href="{REPO}/blob/main/sources.csv">sources.csv</a>。已知限制見 <a href="wiki-site/log.html">log</a>。</p>"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page("XAI 中風影像 LLM Wiki", home))
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    print("wiki-site:", len(files), "頁；index.html")
if __name__ == "__main__": main()
