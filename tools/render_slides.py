#!/usr/bin/env python3
"""⑧ 渲染：把已通過 ⑦ 的逐頁稿轉成單一 HTML。本關不改任何文字。
用法：python tools/render_slides.py workflow/run-01"""
import json, os, re, sys, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools")); import slides_check
CITE = re.compile(r"\[([a-z0-9]+),\s*(p\.\d+|§[A-Za-z0-9.]+)\]")
E_ = html.escape
# 出處標籤的顯示縮寫（只影響顯示，不影響 claim 代號本身；對照表印在最後一頁）
ABBR = {"review": "回顧", "shap": "觀念SHAP", "grad-cam": "觀念GradCAM", "auc": "觀念AUC", "stroke-terms": "觀念名詞",
        "shap-feature-dependence": "議題1", "shap-rank-vs-incremental-value": "議題2", "gradcam-coarse-and-artifacts": "議題3",
        "validation-stage-discrimination": "議題4", "explanation-validity-untested": "議題5", "automation-bias-and-uncertainty": "議題6"}
def short(r):
    name, c = r.split("#"); return f"{ABBR.get(name, name)}·{c}"
def chips(it):
    if it.get("lay"): return f'<span class="chip lay">{E_(it["lay"])}·白話</span>'
    return "".join(f'<span class="chip" title="{E_(r)}">{E_(short(r))}</span>' for r in it.get("refs", []))
def li(b):
    return f'<li class="{"em" if b.get("em") else ""}"><span class="t">{E_(b["t"])}</span>{chips(b)}</li>'
def visual(v):
    t = v["type"]
    if t == "stack":
        tot = sum(p["v"] for p in v["parts"])
        segs = "".join(f'<div class="seg {p["c"]}" style="flex:{p["v"]}"><b>{p["v"]}</b><span>{E_(p["k"])}</span></div>' for p in v["parts"])
        return f'<figure class="vis stack"><figcaption>{E_(v["label"])}{chips(v)}</figcaption><div class="bar">{segs}</div><p class="legend">Low：沒有任何一篇</p></figure>'
    if t == "pair":
        return (f'<figure class="vis pair"><div class="nums"><div><b>{v["a"]["v"]}</b><span>{E_(v["a"]["k"])}</span></div><i>→</i>'
                f'<div class="hl"><b>{v["b"]["v"]}</b><span>{E_(v["b"]["k"])}</span></div></div><figcaption>AUC　{E_(v["cap"])}{chips(v)}</figcaption></figure>')
    if t == "bars":
        rows = "".join(f'<div class="row"><h4>{E_(r["k"])}{chips(r)}</h4>'
                       f'<div class="b a"><i style="width:{float(r["a"])*100:.1f}%"></i><b>{r["a"]}</b></div>'
                       f'<div class="b e {"down" if float(r["b"]) < float(r["a"]) else "up"}"><i style="width:{float(r["b"])*100:.1f}%"></i><b>{r["b"]}</b></div></div>' for r in v["rows"])
        return f'<figure class="vis bars"><figcaption><span class="k a">■ {E_(v["la"])}</span><span class="k e">■ {E_(v["lb"])}</span>　AUC（長條從 0 起算）</figcaption>{rows}</figure>'
    if t == "score":
        return '<div class="vis score">' + "".join(f'<div class="card"><b>{E_(r["v"])}</b><span>{E_(r["k"])}</span>{chips(r)}</div>' for r in v["items"]) + "</div>"
    return ""
def sources(slide, cards):
    seen = []
    for _, _, it in slides_check.items(slide):
        for r in it.get("refs", []):
            for m in CITE.finditer(cards.get(r, "")):
                s = f"{m.group(1)} {m.group(2)}"
                if s not in seen: seen.append(s)
    return "；".join(seen)
def slide_html(s, n, cards):
    lay = s.get("layout", "")
    head = (f'<p class="kicker">{E_(s["kicker"])}</p>' if s.get("kicker") else "") + f'<h2>{E_(s["title"])}</h2>'
    if lay == "title":
        body = f'<div class="titlewrap"><p class="kicker">生成式 AI 課程　第 10 週作業</p><h1>{E_(s["title"])}</h1><p class="sub">{E_(s["sub"])}</p><ul class="meta">' + "".join(f"<li>{E_(b['t'])}</li>" for b in s["bullets"]) + "</ul></div>"
        head = ""
    elif lay == "two":
        body = '<div class="two">' + "".join(f'<section><h3>{E_(c["h"])}</h3><p class="tag">回答：{E_(c["tag"])}</p><ul>{"".join(li(b) for b in c["bullets"])}</ul></section>' for c in s["cols"]) + "</div>"
    elif lay == "flow":
        body = '<div class="flow">' + "".join(f'<span>{E_(x)}</span>' for x in s["steps"]) + f'</div><ul class="plain">{"".join(li(b) for b in s["bullets"])}</ul>' + '<p class="note">代號對照：' + "、".join(f"{v} = {k}" for k, v in ABBR.items()) + "；其餘為論文頁代號。完整內容見 workflow/run-01/03_cards/。</p>"
    else:
        ul = f'<ul>{"".join(li(b) for b in s["bullets"])}</ul>' if s.get("bullets") else ""
        v = visual(s["visual"]) if s.get("visual") else ""
        if v and s["visual"]["type"] == "score": body = v
        elif v: body = f'<div class="split">{ul}{v}</div>'
        else: body = ul
    note = f'<p class="note">註：{E_(s["note"]["t"])}{chips(s["note"])}</p>' if s.get("note") else ""
    src = sources(s, cards)
    foot = f'<footer><span class="src">{"出處：" + E_(src) if src else ""}</span><span class="pg">{s["n"]} / {n}</span></footer>'
    return f'<section class="slide {("lay-"+lay) if lay else ""}" id="s{s["n"]}"><div class="inner">{head}<div class="body">{body}{note}</div></div>{foot}</section>'
CSS = """
:root{--bg:#F6F3EC;--ink:#1A2331;--mut:#5A6475;--rule:#D8D2C5;--acc:#0E6B70;--acc2:#E3F0EF;--warn:#B3432A;--amb:#B97F12;--card:#FFFDF8}
*{box-sizing:border-box}html,body{margin:0;height:100%;background:#12171F;color:var(--ink);font-family:"Noto Sans TC","Noto Sans CJK TC","PingFang TC","Microsoft JhengHei","Heiti TC",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
#stage{position:fixed;left:50%;top:50%;width:1280px;height:720px;transform-origin:center center}
.slide{position:absolute;inset:0;background:var(--bg);display:none;flex-direction:column;overflow:hidden}
.slide.on{display:flex}
.inner{flex:1;min-height:0;padding:50px 72px 0;display:flex;flex-direction:column}
.kicker{margin:0 0 6px;font-size:17px;font-weight:700;letter-spacing:.14em;color:var(--warn)}
h2{margin:0 0 22px;font-size:38px;line-height:1.25;font-weight:800;letter-spacing:.01em;text-wrap:balance}
.body{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;padding-bottom:10px}
ul{margin:0;padding:0;list-style:none}
li{position:relative;padding:9px 0 9px 26px;font-size:23px;line-height:1.5}
li::before{content:"";position:absolute;left:4px;top:22px;width:8px;height:8px;border-radius:50%;background:var(--acc)}
li.em{font-weight:700;background:var(--acc2);border-left:5px solid var(--acc);padding-left:20px;margin-top:8px;border-radius:0 6px 6px 0}
li.em::before{display:none}
.chip{display:inline-block;margin-left:8px;padding:1px 6px;border:1px solid var(--rule);border-radius:4px;font:500 11px/1.5 ui-monospace,"SF Mono",Consolas,monospace;color:var(--mut);vertical-align:middle;white-space:nowrap;background:var(--card)}
.chip.lay{border-style:dashed}
.note{margin:16px 0 0;font-size:15px;line-height:1.6;color:var(--mut)}
footer{display:flex;justify-content:space-between;gap:24px;align-items:flex-end;padding:10px 72px 16px;border-top:1px solid var(--rule);margin:0;font-size:11.5px;line-height:1.45;color:var(--mut)}
footer .src{flex:1;overflow-wrap:anywhere}footer .pg{font-variant-numeric:tabular-nums;font-weight:600;white-space:nowrap}
.split{display:grid;grid-template-columns:1.15fr 1fr;gap:44px;align-items:center}
.vis{margin:0}figcaption{font-size:15px;color:var(--mut);margin-bottom:10px}
.stack .bar{display:flex;height:112px;border-radius:8px;overflow:hidden;gap:3px}
.seg{display:flex;flex-direction:column;justify-content:center;align-items:center;color:#fff;min-width:64px}.seg b{font-size:40px;line-height:1}.seg span{font-size:14px;margin-top:4px}
.seg.hi{background:var(--warn)}.seg.un{background:var(--amb)}.legend{font-size:15px;color:var(--mut);margin:10px 0 0}
.pair .nums{display:flex;align-items:center;justify-content:center;gap:22px;margin-bottom:14px}
.pair .nums div{flex:1;text-align:center;background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:22px 8px}
.pair .nums div.hl{border-color:var(--acc)}.pair b{display:block;font-size:64px;line-height:1;font-weight:800;font-variant-numeric:tabular-nums}
.pair span{display:block;margin-top:8px;font-size:16px;color:var(--mut)}.pair i{font-style:normal;font-size:34px;color:var(--mut)}.pair figcaption{text-align:center;font-size:17px;color:var(--ink);font-weight:600;margin:0}
.bars .row{margin-bottom:16px}.bars h4{margin:0 0 5px;font-size:17px}
.bars .b{display:flex;align-items:center;gap:10px;height:24px;margin-bottom:4px}.bars .b i{display:block;height:100%;border-radius:0 4px 4px 0}
.bars .b b{font-size:17px;font-variant-numeric:tabular-nums}.bars .a i{background:#9AA5B5}.bars .e.up i{background:var(--acc)}.bars .e.down i{background:var(--warn)}
.bars .k{margin-right:14px}.bars .k.a{color:#7C8798}.bars .k.e{color:var(--acc)}
.score{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px}
.score .card{background:var(--card);border:1px solid var(--rule);border-top:5px solid var(--warn);border-radius:8px;padding:22px 16px 16px;display:flex;flex-direction:column;gap:10px;align-items:flex-start}
.score b{font-size:46px;line-height:1;font-weight:800;font-variant-numeric:tabular-nums;white-space:nowrap}.score span:not(.chip){font-size:17px;line-height:1.45}.score .chip{margin-left:0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:36px}.two section{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:26px 28px}
.two h3{margin:0;font-size:32px;font-weight:800;color:var(--acc)}.two .tag{margin:4px 0 12px;font-size:18px;font-weight:700}.two li{font-size:20px;padding:7px 0 7px 22px}.two li::before{top:19px;width:7px;height:7px}
.flow{display:flex;flex-wrap:wrap;gap:8px 6px;margin-bottom:26px}.flow span{position:relative;background:var(--acc);color:#fff;font-size:16px;font-weight:600;padding:8px 14px 8px 20px;clip-path:polygon(0 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%,10px 50%)}
.flow span:nth-child(-n+2){background:var(--ink)}.flow span:nth-child(7){background:var(--amb)}
.lay-title .inner{padding-top:0;justify-content:center}.titlewrap{border-left:8px solid var(--warn);padding-left:36px}
h1{margin:0;font-size:84px;line-height:1.15;font-weight:900;letter-spacing:.02em}.sub{margin:18px 0 40px;font-size:30px;line-height:1.4;font-weight:500;max-width:900px}
.meta li{font-size:18px;color:var(--mut);padding:3px 0}.meta li::before{display:none}.lay-title .body{justify-content:center}
#bar{position:fixed;left:0;bottom:0;height:4px;background:var(--acc);transition:width .2s}
#hint{position:fixed;right:14px;bottom:10px;font-size:12px;color:#8892A2}
@media (prefers-reduced-motion:reduce){#bar{transition:none}}
@media print{html,body{background:#fff;height:auto}#stage{position:static;transform:none!important;width:auto;height:auto}.slide{display:flex!important;position:relative;width:1280px;height:720px;page-break-after:always}#bar,#hint{display:none}@page{size:1280px 720px;margin:0}}
"""
JS = """
const S=[...document.querySelectorAll('.slide')];let i=0;
function fit(){const k=Math.min(innerWidth/1280,innerHeight/720);document.getElementById('stage').style.transform=`translate(-50%,-50%) scale(${k})`}
function go(n){i=Math.max(0,Math.min(S.length-1,n));S.forEach((s,j)=>s.classList.toggle('on',j===i));document.getElementById('bar').style.width=((i+1)/S.length*100)+'%';history.replaceState(null,'','#'+(i+1))}
addEventListener('resize',fit);addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' ','Enter'].includes(e.key)){e.preventDefault();go(i+1)}else if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();go(i-1)}else if(e.key==='Home')go(0);else if(e.key==='End')go(S.length-1)});
document.getElementById('stage').addEventListener('click',e=>{go(i+(e.clientX<innerWidth/3?-1:1))});
let x0=null;addEventListener('touchstart',e=>x0=e.touches[0].clientX);addEventListener('touchend',e=>{if(x0===null)return;const d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>40)go(i+(d<0?1:-1));x0=null});
fit();go((parseInt(location.hash.slice(1))||1)-1);
"""
def main():
    run = sys.argv[1]
    d = json.load(open(os.path.join(ROOT, run, "05_drafts.json"), encoding="utf-8"))
    cards = slides_check.load_cards(run); n = len(d["slides"])
    body = "".join(slide_html(s, n, cards) for s in d["slides"])
    out = f'<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E_(d["topic"])}</title><style>{CSS}</style></head><body><main id="stage">{body}</main><div id="bar"></div><div id="hint">← → 換頁</div><script>{JS}</script></body></html>'
    os.makedirs(os.path.join(ROOT, "slides"), exist_ok=True)
    open(os.path.join(ROOT, "slides", "index.html"), "w", encoding="utf-8").write(out)
    print("slides/index.html", len(out), "bytes,", n, "頁")
if __name__ == "__main__": main()
