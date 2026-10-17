# Auditoria do sistema compartilhado — `_sistema.py` + `_comum.py` (17/10/2026)

Escopo: só o que é comum às 12 páginas (CSS, ícones, rastreio, JS de formulário, `head()`, `config()`, `topbar()`, `footer()`, `faq()`, `privacy()`, `hp()`, `page()` e os helpers de formulário de `_comum.py`). Nada em `paginas/` foi tocado. Visual mantido; só mudou o que era bug, contraste ou alvo de toque.

## 1. Diagnóstico (antes)

| # | Achado | Onde | Gravidade |
|---|---|---|---|
| 1 | `WEBHOOK_URL:''` em todas as páginas: formulário em modo demonstração, nenhum lead gravado | `config()` | crítica |
| 2 | `WHATSAPP:'5500000000000'`: o estado de falha e o "Adiantar pelo WhatsApp" geravam `wa.me/5500000000000` (link quebrado) | `config()`, `finish()` | crítica |
| 3 | Honeypot só funcionava no envio final: `parcial()` testava `o.empresa_site` depois de `payload()` já ter apagado o campo | JS `parcial()` | alta |
| 4 | Estado "falha" só oferecia WhatsApp (que não existe): sem caminho para tentar de novo | `_comum.py form_card` | alta |
| 5 | `fetch` sem timeout: rede pendurada deixava o botão girando para sempre | JS `post()` | média |
| 6 | Backredirect prendia: toda visita re-armava `pushState`; quem voltava de `/espera/` caía de novo em `/espera/` | JS `BACK_URL` | alta |
| 7 | Sem vídeo e sem Calendly configurados, produção mostrava "Configure VIDEO_URL / CALENDLY_URL" e o formulário da VSL só liberava após 60–90 s | JS vídeo/`calendly()` | crítica |
| 8 | Telefone aceitava 10–13 dígitos (DDD 01, 12 dígitos etc.) | JS `valid()` | média |
| 9 | Dois listeners de rolagem disputavam `.top.scrolled` (limiares 8 px e 12 px) e UTMs eram gravadas duas vezes (TRACK + JS) | JS | baixa |
| 10 | `[data-go]` com valor que não é seletor (`05-aplicacao.html`) lançaria exceção; páginas contornavam removendo o atributo | JS | baixa |
| 11 | `data-dl` sem URL ficava `href="#"` visível ("Baixar o playbook" que não baixa) | JS `finish()` | média |
| 12 | `og:image` vazio em todas as páginas; sem `og:url`; sem CSP; `rel="noopener"` sem `noreferrer` | `head()`, `footer()` | média |
| 13 | Política de privacidade: texto genérico e link `#`; nenhuma página real de privacidade existe em `~/projetos/fullx-aula` | `privacy()`, `footer()` | média (LGPD) |
| 14 | Placeholder dos campos `#7d8698` sobre branco = 3,66:1 (abaixo de AA) | CSS `.fld input::placeholder` | média |
| 15 | Alvos de toque < 44 px no celular: chips (40), `.btn-sm` (40), links do rodapé (36), links legais (18), logo (26) | CSS | média |
| 16 | Formulário `position:sticky;top:90px` em `/mentoria` continuava sticky em telas baixas/estreitas | CSS | baixa |
| 17 | 65 regras CSS mortas (`.offer`, `.ticket`, `.screen`, `header.nav`, `body>.bar`, `.fit`, `.missing`, `.agenda`, `.creds`, `.count`, `.live`, `.date`…) herdadas de outro projeto; traçado da logo repetido 3× por página (11,7 KB) | CSS/ICONS | baixa (peso) |
| 18 | `allowfullscreen` + `allow="fullscreen"` no iframe gera aviso no console quando há vídeo | JS | baixa |
| 19 | Rodapé: "Gateway de pagamento" e "IA comercial" listados como produtos; `[RAZÃO SOCIAL · CNPJ]`; faixa de integrações cita Calendly e Make (não confirmados) | `footer()`, `strip()`, `app_mock()` | copy (pedido do orquestrador) |

Sem problema encontrado: XSS por UTM (valores só entram via `URLSearchParams.set`, `encodeURIComponent` e `JSON.stringify`; nenhum `innerHTML` com dado do usuário), `noscript` do pixel, eventos do Pixel/dataLayer (cada evento dispara 1×, `Lead` com `eventID` para deduplicar com a API de conversões), armazenamento de UTM (90 dias, primeiro/último toque, `_fbc` a partir do `fbclid`), Calendly carregado sob demanda com prefill (`name`, `email`, `a1`, `utm_*`), `role="alert"`, `aria-pressed` nos chips, labels, foco visível, zoom livre, um `<h1>` por página, `lang="pt-BR"`, `<main>`, nenhum `NN-xxx.html` sobrando em `dist/`, nenhum segredo no HTML (só o ID público do pixel e a URL pública do Apps Script).

## 2. Correções (31) — arquivo:linha, antes → depois

Commits: `2632673` (sistema), `797acca` (QA). Linhas referem-se a `_sistema.py` após o commit.

| # | Arquivo:linha | Antes → depois |
|---|---|---|
| 1 | `_sistema.py:1096` `config()` | `WEBHOOK_URL:''` → Apps Script real da aula (`…AKfycbwVAbcJL5B…/exec`); formulário sai do modo demonstração |
| 2 | `_sistema.py:1097` | `WHATSAPP:'5500000000000'` → `''` |
| 3 | `_sistema.py:886–887` | novo `WA`: aceita só `55`+DDD+8/9 dígitos e rejeita número de exemplo/repetido; todo `[data-wa]` nasce `hidden` sem número |
| 4 | `_sistema.py:976` `finish()` | `if(wa&&C.WHATSAPP)wa.href=…` → com `WA` mostra e monta `wa.me`; sem `WA` esconde (antes ficava `href="#"` ou `wa.me/5500000000000`) |
| 5 | `_sistema.py:1098` | `BACK_URL:''` → `'/espera/'` em todas, `''` quando `pagina=='backredirect'` |
| 6 | `_sistema.py:918–920` | backredirect arma só se não houve redirecionamento na sessão (`fx_back`) e se o referrer não é a própria `/espera/`; marca `fx_back` ao disparar → o 2º "voltar" sai |
| 7 | `_sistema.py:904–909` | novo: `.video[data-embed-key]` sem URL → esconde `.vsl-wrap`/`.video` e `.vsl-note` (fora do rascunho) e `need=0` para `.delayed[data-delay]`; com URL mantém o `data-delay` |
| 8 | `_sistema.py:915` | iframe sem `allowfullscreen` duplicado (`allow="fullscreen"` já cobre; evitava aviso no console) |
| 9 | `_sistema.py:992–994` `calendly()` | `.cal-ph "Configure CALENDLY_URL"` → `<p class="cal-txt">Recebemos seus dados. O time fala com você em até 24 horas úteis.</p>` (aviso só em rascunho); nada de `Schedule` sem agenda |
| 10 | `_comum.py:43` `form_card` | estado `fail`: só link WhatsApp → texto + `<button data-retry>Tentar de novo</button>` + WhatsApp secundário `hidden` |
| 11 | `_sistema.py:978–979` | novo `retry()`: reabre a última etapa, nav e privacidade, zera `enviado`, foca o botão |
| 12 | `_sistema.py:957` `parcial()` | `var o=payload(); if(o.empresa_site)` (sempre falso) → `if(vals().empresa_site)return` antes do payload |
| 13 | `_sistema.py:955` `post()` | `fetch` sem limite → `AbortController` com 10 s; estouro cai no estado `fail` |
| 14 | `_sistema.py:951` `payload()` | valores do formulário cortados em 500 caracteres antes do JSON (UTMs já eram 250) |
| 15 | `_sistema.py:942` `valid()` | tel `g.length>=10&&<=13` → `/^[1-9]\d(9\d{8}|[2-5]\d{7})$/` (DDD 11–99, celular 9+8 ou fixo 2–5+7) |
| 16 | `_sistema.py:977` | `data-dl` sem URL: `href="#"` visível → link `hidden` |
| 17 | `_sistema.py:927` | `[data-go]` só trata valores que começam com `#` (antes `querySelector('05-aplicacao.html')` lançaria) e rola com `behavior:'auto'` sob `prefers-reduced-motion` |
| 18 | `_sistema.py:883–884, 1001` | removida 2ª captura de UTM no `sessionStorage` (TRACK já faz) e o 2º listener de rolagem de `.top` (ficou só o da camada de movimento) |
| 19 | `_sistema.py:1073–1076` `head()` | `og:image` vazio removido; `og:url` e `og:locale` adicionados; `og:url` reescrito pelo build (`_gerar.py:23`) para `fullxmarketing.com/<slug>/` = canônico |
| 20 | `_sistema.py:1076` | nova meta CSP: `default-src 'self'`; scripts só inline + `connect.facebook.net` + `assets.calendly.com`; estilos inline + Google Fonts; `connect-src` Apps Script (+`script.googleusercontent.com` do redirect) e Meta; `frame-src` Calendly/YouTube/Vimeo/Panda/Vturb; `object-src 'none'`; `base-uri 'self'` — 0 violação nas 12 páginas |
| 21 | `_sistema.py:1082` | Google Fonts: `Inter+Tight:wght@500;600` → `500` (600 nunca usado no display); `display=swap` e `preconnect` já existiam |
| 22 | `_sistema.py:1133–1135` `privacy()` | "Seus dados ficam só com a Full10X" → finalidade + LGPD + link "Política de privacidade" (`href="#"` até existir página; pendência 5) |
| 23 | `_sistema.py:1137–1138` `hp()` | `<noscript>` com aviso "Ative o JavaScript para enviar este formulário" (o formulário é 100 % JS) |
| 24 | `_sistema.py:1121–1127` `footer()` | `foot-g` virou `<nav aria-label="Rodapé">`; Instagram `rel="noopener noreferrer"`; `[RAZÃO SOCIAL · CNPJ]` removido; coluna Softwares = CRM, Sistema de cobrança, IA operacional |
| 25 | `_sistema.py:831–833` `strip()` | lista fixa com Calendly/Make → parâmetro `items`, padrão só com o confirmado (WhatsApp, Pix e boleto via Asaas, Meta Ads, Google Agenda, Webhooks · n8n) |
| 26 | `_sistema.py:777, 808` | mock do produto: menu "IA comercial" → "IA (prévia)"; balão da arte do chat rotulado "IA comercial (prévia)" |
| 27 | `_sistema.py:377` | placeholder `#7d8698` → `#6b7589` (3,66:1 → 4,63:1, AA) |
| 28 | `_sistema.py:142, 545–546` | alvos de toque: logo do topo `min-height:44px`; sob `pointer:coarse` chips, `.btn-sm`, links do rodapé, legais, `.privacy a`, `.small a` ≥ 44 px (desktop inalterado) |
| 29 | `_sistema.py:547` | `/mentoria`: formulário `position:sticky;top:90px` vira `static` em `max-width:999px` ou `max-height:760px` |
| 30 | `_sistema.py` CSS v3 e JS movimento | 1.676 bytes de regras mortas de outro projeto removidas (`.offer`, `.ticket`, `.screen`, `header.nav`, `body>.bar`, `.fit`, `.missing`, `.agenda li`, `.out`, `.creds`, `.count`, `.time`, `.score-row`, `.live`, `.date`, `.compare .with`, `.card-h`, `.foot-in`, `dialog`, `.light.grid-bg`, `.bento .w3`, `.float{}`) e os seletores correspondentes no JS do holofote/cabeçalho/títulos |
| 31 | `_sistema.py:32, 744, 1140–1146` | traçado da palavra da logo definido 1× em `ICONS` (`<path id="fx-word">`) e reutilizado por `<use>` nas 3 logos (−7,6 KB/página); `_min()` tira comentários de linha inteira e indentação de CSS/JS no build (fontes continuam comentadas); `.cal` 660 → 680 px (altura real do widget, sem salto) |

Confirmado em `_sistema.py`/`dist` (pedido dos agentes de copy): os ícones `clock` (linha ~736) e `file` (~741) **já existem** no bloco "ÍCONES EXTRAS (v2)" e saem em `dist/conteudos/index.html` (`id="i-clock"`, `id="i-file"`); nada a adicionar. A página 02 pode remover o `<style>` local que escondia `.cal-ph`.

## 3. Testes executados (saída real)

Build + regressão visual/técnica (12 páginas, 390 e 1440 px):

```
$ python3 _gerar.py && node qa/screens.mjs sistema
gerar rc=0 12 páginas em /Users/juliomyself/projetos/fullx-funis/dist
screens rc=0
aplicacao                                overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:252ms
assista                                  overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:244ms
conteudos                                overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:260ms
curso                                    overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:1406ms
diagnostico                              overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:1462ms
espera                                   overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:239ms
institucional                            overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:1711ms
mentoria                                 overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:244ms
modelos                                  overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:254ms
playbook                                 overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:282ms
white-label                              overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:254ms
conteudos/4-funis-agenda-comercial       overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:1434ms
```
0 rolagem horizontal, 0 erro/aviso de console (inclui violações de CSP) em 12/12. Prints em `docs/landing-audit/screens/sistema/`.
Os `lcp390` de 1,4–1,7 s em 4 páginas são artefato do harness (a mesma página medida isolada com `PerformanceObserver` dá `curso 324 ms P.lead`, `playbook 227 ms`, `institucional 270 ms H1`; o valor alto vem da entrada tardia do candidato após a troca da fonte Google na primeira largura do laço). Nenhuma imagem; LCP é texto.

Interações reais (Playwright, Chromium, servidor em `[::1]` = modo produção, sem classe `draft`):

```
$ node qa/interacoes.mjs
interacoes rc=0
45/45 aprovados
```
O que os 45 cobrem: `/diagnostico` vazio → `role=alert` + `aria-invalid`; e-mail inválido; WhatsApp curto e DDD 01 barrados; máscara `(11) 91234-5678`; etapa 1 → 2; envio **parcial** ao webhook com `status:'parcial'` e sem `empresa_site`; "Voltar" mantém os dados; envio **completo** com `pontuacao`, `qualificado`, `lead_id` igual ao do parcial, `event_id`, `funil`, `url`; Calendly vazio → texto "até 24 horas úteis" e nenhum `script[src*=calendly]`; `dataLayer` com `Lead` 1×, `LeadQualificado`, sem `Schedule`; nota de corte baixa → caixa `nok` com link `/playbook/`; webhook abortado → caixa `fail` com "Tentar de novo", sem `wa.me`; retry reabre o formulário e reenvia; honeypot preenchido → 0 requisições e caixa `ok`; `/assista` sem `VIDEO_URL` → `.video` e `.vsl-note` ocultos e `.delayed` liberado na hora; com `VIDEO_URL` e `data-delay=1` → iframe do YouTube e liberação após 1 s, lembrada em `sessionStorage`; `/conteudos` filtro esconde os outros e troca `aria-pressed`, "todos" restaura; FAQ abre/fecha; Tab chega ao CTA e Enter o ativa; menu do celular abre com `aria-expanded=true`; nenhum link/botão visível < 40 px a 390 px com toque; `prefers-reduced-motion` → título visível na hora e barra de leitura oculta; backredirect: `/aplicacao` arma 1×, "voltar" → `/espera/?origem=aplicacao`, `/espera/` não arma, 2º "voltar" sai de verdade e a origem não re-arma na sessão; nas 12 páginas: âncoras internas existem, 0 `wa.me` visível, 1 `<h1>`, `lang=pt-BR`, `og:url` = canônico, sem `og:image` vazio, `<main>`, 0 erro de JS.

Auxiliares: `node qa/css-mortas.mjs` → `regras 537 mortas 65` antes, `regras 530 mortas 59` depois (as 59 restantes são estados dinâmicos — `.scrolled`, `.open`, `[disabled]`, `.shake`, `.todo`, rascunho — e componentes do sistema que as páginas podem voltar a usar: `.plan*`, `.quote*`, `.trust`, `.cal*`). Contraste medido (WCAG): `--tx-3` escuro 6,48:1, `--tx-2` escuro 9,75:1, `--tx-3` claro 5,77:1, erro 6,57:1, placeholder antes 3,66:1 → depois 4,63:1, `.todo` 10,16:1, `.plan.hot` tx-3 5,64:1. Peso final (KB): espera 91, modelos 91, playbook 96, curso 100, assista 100, mentoria 101, aplicacao 101, conteudos 102, diagnostico 102, artigo 107, white-label 109, institucional 119 (11/12 ≤ 110 KB; a institucional carrega bento + mock do produto + mais texto; antes eram 127 KB).

## 4. Bloqueios e NÃO VERIFICADO

- **Envio real ao Apps Script** (resposta 200 e linha na planilha): NÃO VERIFICADO — os testes interceptam `script.google.com` para não gravar lead falso; a URL é a mesma que já recebe os leads da aula (`~/projetos/fullx-aula/index.html`).
- **Calendly real** (prefill e evento `Schedule` via `postMessage`): NÃO VERIFICADO — não existe `CALENDLY_URL`.
- **Pixel da Meta em produção**: no teste o pixel responde "Bot traffic detected" (esperado em headless); eventos conferidos só no `dataLayer`.
- **CSP com provedores de vídeo**: `frame-src` libera YouTube, Vimeo, Panda, Vturb/ConverteAI; outro host precisa entrar na meta em `head()`.
- `content-visibility:auto` não aplicado: as páginas pesam ~100 KB sem imagem e LCP é texto (< 350 ms); o ganho não compensa o risco de salto nas âncoras e no `IntersectionObserver` de revelação.
- Dados estruturados (Organization/WebSite) não adicionados: a FONTE-DA-VERDADE não fecha nome oficial (Full10X × FULLX), sede, Instagram nem razão social.

## 5. Pendências para o Julio

| # | O que falta | Onde entra | Efeito enquanto falta |
|---|---|---|---|
| 1 | Número de WhatsApp do time (55 + DDD + número) | `WHATSAPP` em `config()` | Botões "Falar pelo WhatsApp" ficam ocultos (nenhum link quebrado) |
| 2 | Link do Calendly (ou decisão de não usar agenda) | `CALENDLY_URL` nas páginas 02, 04, 09 | Conclusão mostra só o texto "o time fala com você em até 24 horas úteis" |
| 3 | Vídeo de vendas gravado (URL de embed) | `VIDEO_URL` (03, 04) e `TRAILER_URL` (07) | Bloco do vídeo some e o formulário aparece direto; `data-delay` volta a valer quando houver vídeo |
| 4 | PDF do playbook (o orquestrador cuida da compressão de `static/playbook/Playbook-Full10X.pdf`) e link do curso | `DOWNLOAD_URL` (06, 08), `CURSO_URL` (07) | Botão de download fica oculto no estado "ok" até a URL existir |
| 5 | Página de Política de Privacidade (LGPD) — não existe em nenhum projeto | `privacy()` e `footer()` apontam para `href="#"` | Link não leva a lugar nenhum; o texto já diz a finalidade do dado |
| 6 | Imagem `og:image` 1200×630 (`static/og.png`) | comentário em `head()` | Prévia no WhatsApp sem imagem (a tag vazia foi removida) |
| 7 | Razão social/CNPJ, Instagram oficial, nome oficial da marca (Full10X × FULLX) | `footer()`, dados estruturados | Rodapé só com "Full10X"; Instagram aponta para `instagram.com/`; sem JSON-LD |
| 8 | Confirmar na planilha que o Apps Script grava os campos novos (`pontuacao`, `qualificado`, `funil`, `lead_id`, `status`, `ft_*`) | planilha de leads da aula | Primeiro lead real cria as colunas sozinho (comportamento do `Code.gs`) |
| 9 | `#planos` em `/white-label`: nenhuma âncora nem link com esse nome existe hoje (a página foi reescrita pelo agente de copy) | `paginas/p09` | Nada quebrado; só registrar se a seção de planos voltar |
