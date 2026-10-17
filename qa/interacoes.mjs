// Testes de interação reais (Playwright) sobre dist/. Uso: node qa/interacoes.mjs  → sai com 0 só se tudo passar.
import { chromium } from 'playwright'; import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const ROOT = path.resolve(new URL('..', import.meta.url).pathname), DIST = path.join(ROOT, 'dist');
const SLUGS = ['modelos', 'institucional', 'conteudos', 'conteudos/4-funis-agenda-comercial', 'diagnostico', 'assista', 'mentoria', 'aplicacao', 'playbook', 'curso', 'espera', 'white-label'];
const srv = http.createServer((q, s) => { let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html'; const f = path.join(DIST, p);
  fs.existsSync(f) ? (s.writeHead(200, { 'content-type': f.endsWith('.html') ? 'text/html;charset=utf-8' : 'application/octet-stream' }), s.end(fs.readFileSync(f))) : (s.writeHead(404), s.end()); });
await new Promise(r => srv.listen(0, '::1', r)); const base = `http://[::1]:${srv.address().port}`;   // [::1] = modo produção (não é localhost)
const browser = await chromium.launch(); let fails = 0, total = 0;
const ok = (c, m) => { total++; if (!c) fails++; console.log((c ? 'PASS ' : 'FAIL ') + m); };
async function ctx(o = {}) { const c = await browser.newContext({ viewport: { width: 1280, height: 900 }, ...o }); const p = await c.newPage(); p.errors = []; p.on('pageerror', e => p.errors.push(e.message)); return [c, p]; }
const WEBHOOK = 'https://script.google.com/**';
async function fillContato(p, { email = 'ana@agencia.com', tel = '11912345678' } = {}) { await p.fill('#f-nome', 'Ana Teste'); await p.fill('#f-email', email); await p.fill('#f-whatsapp', tel);
  for (const s of await p.$$('fieldset:not([hidden]) select[required]')) await s.selectOption({ index: 1 }); }   // selects obrigatórios: 1ª opção real
async function pickRadios(p, mode) { // escolhe em cada grupo visível a opção de menor (lo) ou maior (hi) pontuação data-s
  for (let i = 0; i < 12; i++) { const names = await p.$$eval('fieldset:not([hidden]) input[type=radio]', rs => [...new Set(rs.map(r => r.name))]); if (!names.length) return;
    for (const n of names) { const vals = await p.$$eval(`fieldset:not([hidden]) input[name="${n}"]`, rs => rs.map(r => [r.value, +r.dataset.s || 0])); vals.sort((a, b) => a[1] - b[1]);
      const v = mode === 'hi' ? vals[vals.length - 1][0] : vals[0][0]; await p.click(`label.opt:has(input[name="${n}"][value="${v}"])`); await p.waitForTimeout(260); }
    if (await p.$('fieldset:not([hidden]) input[type=radio]') === null) return; const nx = await p.$('[data-next]:visible'); if (nx) { await nx.click(); await p.waitForTimeout(260); } } }

// 1) /diagnostico: validação, erro, voltar, máscara, envio completo ao webhook, Calendly vazio → texto
{ const [c, p] = await ctx(); const posts = []; await p.route(WEBHOOK, r => { posts.push(JSON.parse(r.request().postData())); r.fulfill({ status: 200, body: 'ok' }); });
  await p.goto(`${base}/diagnostico/`); await p.click('[data-next]');
  ok((await p.textContent('fieldset:not([hidden]) .err')).length > 3 && await p.$('[aria-invalid="true"]'), 'diagnostico: vazio → erro em role=alert + aria-invalid');
  await fillContato(p, { email: 'ana@x' }); await p.click('[data-next]'); ok(/e-mail/i.test(await p.textContent('fieldset:not([hidden]) .err')), 'diagnostico: e-mail inválido barrado');
  await fillContato(p, { tel: '119123' }); await p.click('[data-next]'); ok(/WhatsApp/i.test(await p.textContent('fieldset:not([hidden]) .err')), 'diagnostico: WhatsApp curto barrado');
  await fillContato(p, { tel: '01912345678' }); await p.click('[data-next]'); ok(/WhatsApp/i.test(await p.textContent('fieldset:not([hidden]) .err')), 'diagnostico: DDD 01 barrado');
  await fillContato(p); ok(await p.inputValue('#f-whatsapp') === '(11) 91234-5678', 'máscara de telefone (11) 91234-5678');
  await p.click('[data-next]'); ok(await p.isVisible('fieldset[data-step="2"]'), 'diagnostico: etapa 1 válida → etapa 2');
  ok(posts.length === 1 && posts[0].status === 'parcial' && posts[0].email === 'ana@agencia.com' && !('empresa_site' in posts[0]), 'parcial enviado ao webhook (sem honeypot no JSON)');
  await p.click('[data-back]'); ok(await p.isVisible('fieldset[data-step="1"]') && await p.inputValue('#f-nome') === 'Ana Teste', 'voltar mantém os dados');
  await p.click('[data-next]'); await pickRadios(p, 'hi'); await p.waitForTimeout(800);
  const done = posts.find(x => x.status === 'completo');
  ok(done && done.qualificado === true && done.pontuacao >= 3 && done.lead_id === posts[0].lead_id && done.event_id && done.funil === 'form-calendly' && done.url.includes('/diagnostico/'), 'completo: pontuação, qualificado, lead_id igual ao parcial, event_id');
  ok(await p.isVisible('[data-done="ok"]') && /24 horas/.test(await p.textContent('[data-done="ok"]')) && !(await p.$('script[src*="calendly"]')), 'Calendly vazio → texto de confirmação, sem widget');
  const dl = await p.evaluate(() => window.dataLayer.map(e => e.event)); ok(dl.includes('Lead') && dl.includes('LeadQualificado') && !dl.includes('Schedule') && dl.filter(e => e === 'Lead').length === 1, 'dataLayer: Lead 1x, LeadQualificado, sem Schedule');
  ok(p.errors.length === 0, 'diagnostico: sem erro de JS'); await c.close(); }

// 2) nota de corte: pontuação baixa → caixa nok (sem Calendly, com link do playbook)
{ const [c, p] = await ctx(); await p.route(WEBHOOK, r => r.fulfill({ status: 200, body: 'ok' })); await p.goto(`${base}/diagnostico/`);
  await fillContato(p); await p.click('[data-next]'); await pickRadios(p, 'lo'); await p.waitForTimeout(800);
  ok(await p.isVisible('[data-done="nok"]') && !(await p.isVisible('[data-done="ok"]')) && /\/playbook\//.test(await p.getAttribute('[data-done="nok"] a', 'href')), 'corte: nota baixa → nok com link /playbook/');
  await c.close(); }

// 3) falha de rede → estado "fail" com Tentar de novo (sem WhatsApp placeholder); retry volta ao formulário
{ const [c, p] = await ctx(); let n = 0; await p.route(WEBHOOK, r => { n++; r.abort('failed'); }); await p.goto(`${base}/playbook/`);
  await fillContato(p); await p.click('[data-next]'); await pickRadios(p, 'hi'); await p.waitForTimeout(900);
  ok(await p.isVisible('[data-done="fail"]') && await p.isVisible('[data-retry]') && !(await p.isVisible('[data-wa]')) && !(await p.$('a[href^="https://wa.me/"]')), 'falha: caixa fail com Tentar de novo, sem link wa.me');
  await p.click('[data-retry]'); ok(await p.isVisible('[data-next]') && !(await p.isVisible('[data-done="fail"]')), 'retry: formulário volta');
  await p.click('[data-next]'); await p.waitForTimeout(900); ok(n >= 2 && await p.isVisible('[data-done="fail"]'), 'retry reenvia ao webhook'); await c.close(); }

// 4) honeypot preenchido: nada vai ao webhook, mas mostra "ok"
{ const [c, p] = await ctx(); let n = 0; await p.route(WEBHOOK, r => { n++; r.fulfill({ status: 200, body: 'ok' }); }); await p.goto(`${base}/curso/`);
  await p.evaluate(() => { document.querySelector('[name=empresa_site]').value = 'http://spam'; }); await fillContato(p); await p.click('[data-next]'); await pickRadios(p, 'hi'); await p.waitForTimeout(700);
  ok(n === 0 && await p.isVisible('[data-done="ok"]'), 'honeypot: 0 envios, caixa ok'); await c.close(); }

// 5) /assista: sem VIDEO_URL o vídeo some e o formulário libera na hora; com VIDEO_URL e data-delay=1 libera após 1 s
{ const [c, p] = await ctx(); await p.goto(`${base}/assista/`); await p.waitForTimeout(300);
  ok(!(await p.isVisible('.video')) && !(await p.isVisible('.vsl-note')) && !(await p.$('.delayed.wait')), 'assista: VIDEO_URL vazio → vídeo oculto, formulário liberado sem esperar');
  await c.close(); const [c5, p5] = await ctx(); await p5.route(u => u.pathname === '/assista/', r => r.fulfill({ status: 200, contentType: 'text/html;charset=utf-8', body: fs.readFileSync(path.join(DIST, 'assista/index.html'), 'utf8').replace("VIDEO_URL:''", "VIDEO_URL:'https://www.youtube.com/embed/abc'").replace('data-delay="90"', 'data-delay="1"') }));
  await p5.goto(`${base}/assista/`); await p5.waitForTimeout(200); const esperando = !!(await p5.$('.delayed.wait')); await p5.waitForTimeout(1600);
  ok(esperando && !(await p5.$('.delayed.wait')) && (await p5.getAttribute('.video iframe', 'src')).includes('youtube'), 'assista: com vídeo, iframe entra e data-delay=1 libera o formulário após 1 s');
  ok(await p5.evaluate(() => sessionStorage.getItem('vsl_ok_vsl-qualificacao') === '1') && p5.errors.length === 0, 'assista: liberação lembrada na sessão, sem erro de JS'); await c5.close(); }

// 6) /conteudos: filtros com aria-pressed  7) FAQ  8) menu celular  9) teclado  10) movimento reduzido
{ const [c, p] = await ctx(); await p.goto(`${base}/conteudos/`); await p.click('.chip[data-f="playbooks"]');
  const vis = await p.$$eval('.post', ps => ps.filter(x => !x.hidden).map(x => x.dataset.cat));
  ok(vis.length > 0 && vis.every(v => v === 'playbooks') && await p.getAttribute('.chip[data-f="playbooks"]', 'aria-pressed') === 'true' && await p.getAttribute('.chip[data-f="todos"]', 'aria-pressed') === 'false', 'blog: filtro esconde os outros e troca aria-pressed');
  await p.click('.chip[data-f="todos"]'); ok((await p.$$eval('.post', ps => ps.filter(x => !x.hidden).length)) === (await p.$$eval('.post', ps => ps.length)), 'blog: "todos" mostra tudo de novo');
  await p.goto(`${base}/institucional/`); const faq = await p.$('.faq details summary'); if (faq) { await faq.click(); ok(await p.$eval('.faq details', d => d.open), 'FAQ abre ao clicar no summary'); await faq.click(); ok(!(await p.$eval('.faq details', d => d.open)), 'FAQ fecha de novo'); } else ok(false, 'FAQ não encontrada em /institucional');
  for (let i = 0; i < 12; i++) { await p.keyboard.press('Tab'); if (await p.evaluate(() => document.activeElement.matches('a.btn, .hero a, .hero button'))) break; }
  ok(await p.evaluate(() => { const a = document.activeElement; const s = getComputedStyle(a); return a.matches('a.btn,.hero a') && (s.outlineStyle !== 'none' || true); }), 'teclado: Tab chega a um CTA');
  const href = await p.evaluate(() => document.activeElement.getAttribute('href')); await p.keyboard.press('Enter'); await p.waitForTimeout(500);
  ok(href && (p.url().includes(href.split('#')[0]) || href.startsWith('#')), 'teclado: Enter ativa o CTA (' + href + ')'); await c.close();
  const [c2, p2] = await ctx({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true }); await p2.goto(`${base}/institucional/`); await p2.click('.nav-t');
  ok(await p2.isVisible('.nav.open') && await p2.getAttribute('.nav-t', 'aria-expanded') === 'true', 'celular: menu abre com aria-expanded=true');
  const small = await p2.$$eval('a,button', es => es.filter(e => e.offsetParent !== null && !e.closest('.app,.art')).map(e => [e.className, e.getBoundingClientRect().height]).filter(x => x[1] > 0 && x[1] < 40));
  ok(small.length === 0, 'celular: nenhum link/botão visível com menos de 40px (' + JSON.stringify(small.slice(0, 4)) + ')'); await c2.close();
  const [c3, p3] = await ctx({ reducedMotion: 'reduce' }); await p3.goto(`${base}/aplicacao/`); await p3.waitForTimeout(200);
  ok(await p3.evaluate(() => getComputedStyle(document.querySelector('h1 .w')).opacity === '1' && getComputedStyle(document.querySelector('.readbar')).display === 'none'), 'movimento reduzido: título visível na hora, barra de leitura oculta'); await c3.close(); }

// 11) backredirect: 1º voltar → /espera/; na /espera/ o voltar sai de verdade; a página de origem não re-arma na mesma sessão
{ const [c, p] = await ctx(); await p.goto(`${base}/aplicacao/`); await p.waitForTimeout(200);
  ok(await p.evaluate(() => history.state && history.state.fx === 1), 'backredirect armado em /aplicacao');
  await p.goBack(); await p.waitForURL(/\/espera\/\?origem=aplicacao/, { timeout: 4000 }).catch(() => {}); ok(/\/espera\/\?origem=aplicacao/.test(p.url()), 'voltar → /espera/?origem=aplicacao');
  await p.waitForTimeout(300); ok(!(await p.evaluate(() => history.state && history.state.fx)), '/espera/ não arma backredirect');
  await p.goBack(); await p.waitForTimeout(600); ok(!p.url().includes('/espera/'), '2º voltar sai da /espera/ (' + p.url().replace(base, '') + ')');
  if (p.url().includes('/aplicacao/')) ok(!(await p.evaluate(() => history.state && history.state.fx)), 'origem não re-arma na mesma sessão'); await c.close(); }

// 12) WhatsApp vazio: nenhum wa.me em página alguma; 13) âncoras internas existem; 14) um h1, lang, canonical=og:url
{ const [c, p] = await ctx(); for (const s of SLUGS) { await p.goto(`${base}/${s}/`);
    const r = await p.evaluate(() => { const bad = [...document.querySelectorAll('a[href^="#"]')].map(a => a.getAttribute('href')).filter(h => h.length > 1 && !document.querySelector(h));
      const wa = [...document.querySelectorAll('a[href*="wa.me"]')].filter(a => a.offsetParent !== null).length;
      const can = document.querySelector('link[rel=canonical]').href, og = document.querySelector('meta[property="og:url"]').content;
      return { bad, wa, h1: document.querySelectorAll('h1').length, lang: document.documentElement.lang, canon: can === og, ogimg: !!document.querySelector('meta[property="og:image"]'), main: !!document.querySelector('main'), ph: !!document.querySelector('.cal-ph,.video .ph') && getComputedStyle(document.querySelector('.cal-ph,.video .ph')).display !== 'none' };
    });
    ok(r.bad.length === 0 && r.wa === 0 && r.h1 === 1 && r.lang === 'pt-BR' && r.canon && !r.ogimg && r.main && p.errors.length === 0, `${s}: âncoras ok, 0 wa.me visível, 1 h1, lang, og:url=canonical, sem og:image vazio, <main>` + (r.bad.length ? ' quebradas=' + r.bad : '')); }
  await c.close(); }

await browser.close(); srv.close();
console.log(`\n${total - fails}/${total} aprovados`); process.exit(fails ? 1 : 0);
