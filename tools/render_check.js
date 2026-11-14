// ⑨ 渲染檢查：無頭瀏覽器逐頁量測，內容不可超出 1280×720 的版面，且同時只能顯示一頁。
// 用法：node tools/render_check.js workflow/run-01   （需要 playwright 與 Chrome）
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const root = path.resolve(__dirname, '..'); const run = path.join(root, process.argv[2]);
  const shots = path.join(run, 'shots'); fs.mkdirSync(shots, { recursive: true });
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/usr/bin/google-chrome', args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('file://' + path.join(root, 'slides', 'index.html'));
  const n = await p.locator('.slide').count(); const rows = []; let bad = 0;
  for (let i = 0; i < n; i++) {
    await p.evaluate(k => go(k), i); await p.waitForTimeout(80);
    const r = await p.evaluate(() => {
      const s = document.querySelector('.slide.on'), inner = s.querySelector('.inner'), body = s.querySelector('.body'), R = s.getBoundingClientRect();
      const over = Math.max(inner.scrollHeight - inner.clientHeight, body.scrollHeight - body.clientHeight, 0);
      let out = 0; s.querySelectorAll('h1,h2,li,figure,.card,.flow span,.note,footer,section').forEach(e => { const q = e.getBoundingClientRect(); if (q.right > R.right + 1 || q.bottom > R.bottom + 1 || q.left < R.left - 1) out++; });
      const foot = s.querySelector('footer').getBoundingClientRect().height;
      const vis = [...document.querySelectorAll('.slide')].filter(e => getComputedStyle(e).display !== 'none').length;
      return { over, out, vis, foot: Math.round(foot), title: (s.querySelector('h2,h1') || {}).textContent };
    });
    const ok = r.over <= 1 && r.out === 0 && r.foot <= 96 && r.vis === 1; if (!ok) bad++;
    rows.push(`| ${i + 1} | ${r.title} | ${r.over} | ${r.out} | ${r.foot} | ${r.vis} | ${ok ? '✅' : '❌'} |`);
    await p.screenshot({ path: path.join(shots, `s${String(i + 1).padStart(2, '0')}.png`) });
  }
  await b.close();
  console.log(`檢查 ${n} 頁；不合格 ${bad} 頁。${bad ? '❌' : '✅'}\n\n| 頁 | 標題 | 垂直溢出(px) | 超出版面的元素 | 頁尾高度(px) | 同時顯示頁數 | 結果 |\n|---|---|---|---|---|---|---|\n` + rows.join('\n'));
  process.exit(bad ? 1 : 0);
})();
