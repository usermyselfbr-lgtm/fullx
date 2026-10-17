// QA visual e técnico das páginas em dist/. Uso: node qa/screens.mjs <fase> [slug ...]
// Sobe um servidor estático em [::1] (hostname que não ativa o modo rascunho), tira prints em 5 larguras,
// detecta rolagem horizontal, erros de console, placeholders [ASSIM] visíveis e links internos quebrados.
import { chromium } from 'playwright';
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const ROOT = path.resolve(new URL('..', import.meta.url).pathname), DIST = path.join(ROOT, 'dist');
const fase = process.argv[2] || 'atual', only = process.argv.slice(3);
const slugs = fs.readdirSync(DIST, { recursive: true }).filter(f => f.endsWith('index.html')).map(f => path.dirname(f)).filter(s => !only.length || only.includes(s));
const WIDTHS = [360, 390, 768, 1024, 1440];
const srv = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const f = path.join(DIST, p); if (!f.startsWith(DIST) || !fs.existsSync(f)) { res.writeHead(404); return res.end('404'); }
  res.writeHead(200, { 'content-type': f.endsWith('.html') ? 'text/html; charset=utf-8' : 'application/octet-stream' }); fs.createReadStream(f).pipe(res);
});
await new Promise(r => srv.listen(0, '::1', r));
const base = `http://[::1]:${srv.address().port}`;
const out = path.join(ROOT, 'docs/landing-audit/screens', fase); fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch(); const report = {};
for (const slug of slugs) {
  const r = report[slug] = { console: [], overflow: [], todo: 0, placeholders: [], brokenLinks: [], lcp: null };
  for (const w of WIDTHS) {
    const ctx = await browser.newContext({ viewport: { width: w, height: 844 }, deviceScaleFactor: 1, reducedMotion: 'reduce' });
    const page = await ctx.newPage();
    page.on('console', m => { if (['error', 'warning'].includes(m.type())) r.console.push(`${w}: ${m.text().slice(0, 160)}`); });
    page.on('pageerror', e => r.console.push(`${w}: pageerror ${e.message.slice(0, 160)}`));
    await page.goto(`${base}/${slug}/`, { waitUntil: 'networkidle' });
    await page.evaluate(() => new Promise(r => setTimeout(r, 400)));
    const info = await page.evaluate(() => {
      const sw = document.documentElement.scrollWidth, iw = window.innerWidth;
      const wide = sw > iw + 1 ? [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > iw + 1).slice(0, 5).map(e => e.tagName.toLowerCase() + (e.className ? '.' + String(e.className).split(' ')[0] : '')) : [];
      const txt = document.body.innerText; const ph = [...new Set((txt.match(/\[[^\]\n]{2,80}\]/g) || []))].slice(0, 12);
      const links = [...document.querySelectorAll('a[href^="/"]')].map(a => a.getAttribute('href').split('#')[0]);
      return { sw, iw, wide, todo: document.querySelectorAll('.todo').length, ph, links: [...new Set(links)] };
    });
    if (info.sw > info.iw + 1) r.overflow.push(`${w}: scrollWidth ${info.sw} > ${info.iw} (${info.wide.join(', ')})`);
    r.todo = info.todo; r.placeholders = info.ph;
    if (w === 390) for (const l of info.links) { const f = path.join(DIST, l, 'index.html'); if (!fs.existsSync(f)) r.brokenLinks.push(l); }
    if (w === 390 || w === 1440) await page.screenshot({ path: path.join(out, `${slug.replace(/\//g, '__')}-${w}.png`), fullPage: true });
    if (w === 390) r.lcp = await page.evaluate(() => new Promise(res => { let v = null; new PerformanceObserver(l => { for (const e of l.getEntries()) v = Math.round(e.startTime); }).observe({ type: 'largest-contentful-paint', buffered: true }); setTimeout(() => res(v), 300); }));
    await ctx.close();
  }
  r.console = [...new Set(r.console)];
  console.log(`${slug.padEnd(40)} overflow:${r.overflow.length} console:${r.console.length} todo:${r.todo} placeholders:${r.placeholders.length} links-quebrados:${r.brokenLinks.length} lcp390:${r.lcp}ms`);
}
fs.writeFileSync(path.join(out, 'relatorio.json'), JSON.stringify(report, null, 2));
await browser.close(); srv.close();
