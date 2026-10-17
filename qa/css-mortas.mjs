// Lista regras CSS cujo seletor não casa com nenhum elemento em nenhuma página de dist/ (pseudo-classes ignoradas).
// Uso: node qa/css-mortas.mjs
import { chromium } from 'playwright'; import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const ROOT = path.resolve(new URL('..', import.meta.url).pathname), DIST = path.join(ROOT, 'dist');
const slugs = ['modelos', 'institucional', 'conteudos', 'conteudos/4-funis-agenda-comercial', 'diagnostico', 'assista', 'mentoria', 'aplicacao', 'playbook', 'curso', 'espera', 'white-label'];
const srv = http.createServer((q, s) => { let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html'; const f = path.join(DIST, p);
  fs.existsSync(f) ? (s.writeHead(200, { 'content-type': f.endsWith('.html') ? 'text/html;charset=utf-8' : 'application/octet-stream' }), s.end(fs.readFileSync(f))) : (s.writeHead(404), s.end()); });
await new Promise(r => srv.listen(0, '::1', r)); const base = `http://[::1]:${srv.address().port}`;
const browser = await chromium.launch(); const page = await (await browser.newContext({ viewport: { width: 1280, height: 800 } })).newPage();
const matched = new Map(); let rules = null;
for (const s of slugs) {
  await page.goto(`${base}/${s}/`, { waitUntil: 'load' });
  const r = await page.evaluate(() => { const out = [];
    const walk = (rs, media) => { for (const r of rs) { if (r.type === 1) { let m = false;
      for (const sel of r.selectorText.split(/,(?![^(]*\))/)) { const clean = sel.replace(/:has\([^)]*\)/g, '').replace(/::?[a-z-]+(\([^)]*\))?/g, '').trim() || '*';
        try { if (document.querySelector(clean)) { m = true; break; } } catch (e) { m = true; } }
      out.push([media + '|' + r.selectorText, m]); } else if (r.cssRules) walk(r.cssRules, media + (r.media ? r.media.mediaText : '')); } };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules, ''); } catch (e) {} } return out; });
  if (!rules) rules = r.map(x => x[0]); r.forEach(([k, m]) => matched.set(k, (matched.get(k) || false) || m));
}
const dead = rules.filter(k => !matched.get(k));
console.log('regras', rules.length, 'mortas', dead.length); dead.forEach(k => console.log('  ' + k.slice(0, 150)));
await browser.close(); srv.close();
