# 06 · /playbook — Playbook Full10X (isca)

- **Rota:** `/playbook/` · **Fonte:** `paginas/p06_playbook_ebook.py` · **Arquivo da isca:** `static/playbook/Playbook-Full10X.pdf` → `/playbook/Playbook-Full10X.pdf`
- **Mercado / ICP:** dono de agência ou gestor de tráfego com clientes próprios (R$10 mil a R$80 mil/mês), Brasil, tráfego frio/orgânico e remarketing.
- **Objetivo:** captar Lead (formulário de 1 passo `playbook-ebook`, evento `Lead`) e entregar o PDF na hora (`data-dl="DOWNLOAD_URL"`).

## Decisão sobre a isca: (a) — o PDF real serve e passa a ser a isca

O que foi verificado (17/10):
- `~/Downloads/FULLX/Playbook-Full10X.pdf`: `pdfinfo` → `Title: Playbook Full10X`, `Author: Full10X`, `Pages: 147`, `Page size: 959.976 x 540 pts` (slides 16:9), 25.583.902 bytes, criado em 15/10/2026. Contagem conferida também por `/Type /Page` no binário (147) e por `kMDItemNumberOfPages = 147`.
- Páginas 1 a 20 lidas como imagem; texto das 147 páginas extraído do `Playbook-Full10X-editavel.pptx` (147 slides, mesma ordem e textos das páginas lidas).
- **Capa (pág. 1):** "FULL10X · FRAMEWORK COMERCIAL & AQUISIÇÃO QUALIFICADA · EDIÇÃO 2026 · 10X · PLAYBOOK FULL10X · **Mais clientes & receita** · O sistema completo de estruturação comercial + growth para donos de agência: da oferta ao fechamento, da primeira venda à retenção e à escala · OFERTA — AQUISIÇÃO — COMERCIAL — RETENÇÃO — ESCALA · 11 PARTES · 8 MÓDULOS DE MÉTODO". **Nenhum número proibido na capa.**
- **Índice real (pág. 7, "O método Full10X em 11 partes"):** 01 Onde você está · 02 Fundamentos (dois funis, unit economics, ciclo P.E.A.O.) · 03 Produto & pesquisa · 04 Esteira & oferta (ICP, degraus de valor, produto isca, 8 elementos, engenharia de preço) · 05 Criativos (ângulos, hooks, teste) · 06 Funis (VSL, social selling, páginas por canal, stacking, CRO) · 07 Máquina comercial (SDR, closer, dimensionamento, RH comercial, CRM) · 08 Retenção & LTV · 09 Gestão & escala · 10 Aceleradores (IA no comercial, receita sem novo investimento) · 11 Implementação (plano de 6 semanas, mapa de consulta, checklist mestre). Divisórias das partes nas págs. 9, 14, 28, 41, 59, 67, 83, 97, 117, 137, 142; fechamento na 147.
- **Por que serve:** conteúdo denso e aplicável, escrito para dono de agência (blocos "Na agência" em várias páginas), cobre exatamente a sequência da marca (atrair → filtrar → fechar → sustentar), termina em plano de implantação — e leva naturalmente ao próximo degrau (diagnóstico/mentoria: "ler não muda nada; implementar muda tudo", pág. 2 e 147).
- **Por que o `playbook.html` NÃO foi usado:** descreve outro material ("Playbook 0 a 100K", 47 páginas, "agência de R$150 mil/mês", "+150 clientes em 30+ países", modelos "que rodam na Inout") que não existe e usa números proibidos.
- **A promessa antiga ("formulário que qualifica, 18 páginas") foi abandonada:** esse PDF não existe. O playbook real fala de qualificação (pré-vendas, funil de diagnóstico com aplicação, lead scoring no CRM), mas não é um modelo de formulário pronto; a página agora promete o que o PDF entrega.
- **Cuidados com o conteúdo interno do PDF (não citados na página):** pág. 22 traz um "case de mercado · marca DTC de suplementos · R$1,57 mi em 10 meses" e benchmarks/percentuais (págs. 8, 15, 16, 87–92). A página não reproduz nenhum desses números. Pendência para o Julio: confirmar que pode distribuir publicamente o case da pág. 22 (de quem é a marca, se há autorização) e a nota de fontes da pág. 147 ("Síntese autoral, reescrita e adaptada… a partir d[e material estudado]").

## 1. Diagnóstico (baseline `screens/baseline/playbook-*.png` e `dist/playbook/index.html`)
- Copy: headline forte e específica ("O formulário que separa lead com verba de curioso."), mas promete um PDF inexistente; capa com `[TÍTULO DO EBOOK]` e `[XX] páginas` visíveis; 3 capítulos inventados ("As 7 perguntas / A pontuação / O roteamento").
- Conversão: tela de sucesso diz "Também enviamos o link para o seu e-mail" — falso (não há automação de e-mail; `WEBHOOK_URL` vazio). `DOWNLOAD_URL` vazio: o botão de download não leva a lugar nenhum.
- Técnica: 0 overflow/0 erro no baseline; 2 `.todo` visíveis na capa; sem prova na dobra.

## 2. Research (FONTE-DA-VERDADE + PDF)
- **FATOS:** PDF real "Playbook Full10X · Mais clientes & receita", 147 páginas, 11 partes (índice acima), edição 2026, plano de 6 semanas (pág. 143), três modos de uso: leitura rápida 45 min / implementação 6 semanas / consulta pontual (pág. 2); "Ler não muda nada; implementar muda tudo" (págs. 2 e 147); "o problema não é falta de esforço: é falta de estrutura" (pág. 4). Números permitidos pelo orquestrador: "+R$10 milhões em tráfego gerenciado", "+2.300 clientes de serviço gerados" (linha PROOF compartilhada). Linguagem da marca: canos, "curioso × verba", "Seu problema não é conhecimento. É instalação."
- **HIPÓTESES:** o ICP baixa um material longo se souber por onde começar (por isso a página destaca os 3 modos de uso e "comece pela Parte 11").
- **AUSENTES:** envio por e-mail, autor nomeado no PDF, depoimentos de quem leu, versão "formulário que qualifica".

## 3. Brief RMBC
- **Avatar:** dono de agência R$10–80 mil/mês que já tem cliente, vive de indicação, vende sozinho e perde cliente no 3º mês.
- **Consciência:** consciente do problema (sabe que o mês oscila), não da solução.
- **Dor central:** "Cliente cancela em 3 meses. Boleto atrasa." / "Só você vende." (AULA-A).
- **Inimigo:** testar coisa solta sem sistema; mais horas no mesmo modelo.
- **Mecanismo do problema:** a agência não trava por falta de técnica, trava por falta de estrutura — oferta, comercial e retenção na mão do dono.
- **Mecanismo da solução:** o sistema Full10X na ordem em que o dinheiro passa (atrair → filtrar → fechar → sustentar), um módulo por vez, com dono e métrica.
- **Big idea:** a agência inteira num mapa só, com plano de instalação de 6 semanas.
- **Promessa defensável:** "147 páginas da oferta ao cliente que renova, com plano de 6 semanas para implantar." (tudo verificável no PDF).
- **3 provas:** o próprio PDF (índice real, capa real, nº de páginas); "+R$10 milhões em tráfego gerenciado"; "+2.300 clientes de serviço gerados".
- **Objeções:** "147 páginas, não tenho tempo" → leitura rápida de 45 minutos ou modo consulta; "é mais um PDF de teoria" → termina em plano de 6 semanas e checklist; "serve para o meu nicho?" → é sobre a operação de agência que vende serviço recorrente; "vão me encher de mensagem?" → aviso de privacidade compartilhado.
- **Oferta:** PDF grátis, download na hora após o formulário.
- **CTA:** "Liberar meu playbook" (form) / "Baixar o playbook grátis" (meio e barra do celular).
- **Arquitetura:** hero (promessa + capa real + formulário + prova) → o que tem dentro (3 blocos de partes reais) → como usar (3 modos reais) → CTA.

## 4. Headlines (15)
1. Atrair, filtrar, fechar e sustentar: o playbook da agência inteira, grátis. ← **escolhida**
2. 147 páginas para a sua agência parar de depender de você.
3. Sua agência não precisa de mais esforço. Precisa de estrutura.
4. Da oferta ao cliente que renova, em 147 páginas.
5. O mapa da agência que vende sem o dono em toda call.
6. Seu problema não é conhecimento. É instalação. Comece por este playbook.
7. Os canos da agência, um por um, com plano de 6 semanas.
8. Por que o mês ainda fecha na indicação (e onde o seu funil vaza).
9. Pare de testar coisa solta. Siga a ordem em que o dinheiro passa.
10. O playbook que começa na oferta e termina no cliente que fica.
11. Mais clientes e receita: o Playbook Full10X, de graça.
12. Como estruturar pré-vendas, closer e retenção sem contratar consultoria.
13. 11 partes, 6 semanas, um módulo por vez.
14. Tudo o que acontece entre o anúncio e o boleto pago.
15. O que fazer quando a agência cresce e só você vende.
→ Escolhida a 1 (depois encurtada na fase 7 para "O playbook da agência inteira, grátis.", com a sequência no lead): usa a sequência oficial da marca (coerência com as outras páginas), descreve o que o PDF cobre de verdade e diz o preço (grátis) — nenhuma promessa que o material não sustente.

## 5. Copy completa
- **Eyebrow:** Playbook gratuito · PDF · 147 páginas
- **H1 (final):** O playbook da agência inteira, grátis. (a sequência atrair → filtrar → fechar → sustentar abre o lead)
- **Lead:** Oferta, criativo, funil, pré-vendas, closer, CRM e retenção, na ordem em que o dinheiro passa. No fim, um plano de 6 semanas para implantar um módulo por vez.
- **Formulário:** título "Grátis · download na hora"; legenda "Libere o seu PDF"; botão "Liberar meu playbook".
- **Prova:** linha PROOF compartilhada.
- **Capa em código:** PLAYBOOK FULL10X · EDIÇÃO 2026 / Mais clientes & receita / 147 páginas · PDF.
- **O que tem dentro (h2 "O que tem dentro das 147 páginas.")**
  - Partes 01 a 04 · Antes de anunciar — Em que fase a agência está, as 5 métricas de base (CAC, LTV, retorno, ticket e conversão), a conta que diz se dá para escalar, ICP, escada de valor e os 8 elementos de uma oferta.
  - Partes 05 a 07 · Atrair, filtrar e fechar — Ângulos e hooks, funil de diagnóstico com vídeo e aplicação, social selling, os 4 tipos de SDR, a call de decisão do closer, quantas pessoas o comercial precisa e o pipeline do CRM etapa por etapa.
  - Partes 08 a 11 · Sustentar e escalar — Pós-venda em 5 etapas, fluxos por WhatsApp e e-mail, KPIs e rotinas de gestão, IA no comercial e o plano de 6 semanas com checklist mestre.
- **Como usar (h2 "147 páginas não são para ler de uma vez.")**, lead "Ler não muda nada. Implementar muda. Escolha o modo que cabe no seu momento."
  - Leitura rápida · 45 min — Parte 02 inteira e, de cada módulo, só objetivo e armadilhas.
  - Implementação · 6 semanas — Uma parte por semana, com a métrica que precisa mexer.
  - Consulta · quando travar — A tabela "onde está o meu problema" leva direto ao módulo certo.
  - CTA: "Baixar o playbook grátis"
- **Sucesso:** "O playbook é seu." / "PDF de 25 MB: no 4G, salve para ler depois. Comece pela Parte 11, que diz por onde ir." / botão "Baixar o playbook (PDF)".
- **Barra do celular:** "Baixar o playbook grátis".
- **Title/description:** "Full10X · Playbook gratuito: mais clientes e receita para agência" / "Baixe grátis o Playbook Full10X: 147 páginas de oferta, funil, comercial e retenção para donos de agência, com plano de 6 semanas."

## 6. Implementação
- `paginas/p06_playbook_ebook.py` reescrito: capa com título e nº de páginas reais, `PARTES` e `MODOS` como listas locais, `PROOF` sob o formulário, nova seção "como usar" (`sec mist`), `DOWNLOAD_URL:'/playbook/Playbook-Full10X.pdf'`. `name=`, `data-funil="playbook-ebook"`, `data-evento="Lead"`, `fid="form"` intactos.
- PDF copiado: `cp ~/Downloads/FULLX/Playbook-Full10X.pdf static/playbook/` → `cmp` sem diferença (`rc=0`); 25.583.902 bytes.
- `python3 _gerar.py` → `12 páginas em …/dist` (`rc=0`); `grep -c 'class="todo"' dist/playbook/index.html` → `0`.

## 7. Ajuste visual
- `06-v1`: H1 longo quebrava em 7 linhas no 1440 (coluna estreita do `split`). Ajuste: H1 encurtado para **"O playbook da agência inteira, grátis."** e a sequência "Atrair, filtrar, fechar e sustentar" foi para o lead (mesma promessa, 3 linhas).
- `06-v2` (1440 e 390 conferidos): capa legível, cards iguais, sem texto cortado. A barra fixa do celular aparece sobre o formulário só no print de página inteira (comportamento `position:fixed` do sistema, igual ao baseline).

## 8. Engenharia
- Teste Playwright (servidor local em `dist/`): preencher e enviar o formulário → `playbook okVisible= true href= /playbook/Playbook-Full10X.pdf h1= 1 robots= 0`; `pageerrors 0`.
- `curl -sI http://localhost:4321/playbook/Playbook-Full10X.pdf` → `HTTP/1.0 200 OK`.
- CTAs do meio e da barra do celular → `#form`. Capa com `aria-hidden`. Hierarquia h1 > h2 > h3.

## 9. Revisão editorial
- Removidos: promessa de PDF inexistente, "Também enviamos o link para o seu e-mail" (falso), capítulos inventados. Toda afirmação sobre o conteúdo aponta para uma página real do PDF (índice pág. 7, modos de uso pág. 2, consulta pág. 144, plano pág. 143, SDR pág. 84, 8 elementos págs. 48–49, pós-venda em 5 etapas pág. 97).
- Busca de proibidos no `dist/playbook/index.html` (`150 mil|+420|+150|30 países|4 mil tatuadores|Inout|enviamos…`) → `0`.

## 10. Documentação / resultado
- **Antes → depois:** H1 "O formulário que separa lead com verba de curioso." → "O playbook da agência inteira, grátis."; capa `[TÍTULO DO EBOOK] / [XX] páginas` → "Mais clientes & receita / 147 páginas · PDF"; capítulos "As 7 perguntas / A pontuação / O roteamento" → "Partes 01 a 04 / 05 a 07 / 08 a 11" com o conteúdo real; sucesso "enviamos para o seu e-mail" → "PDF de 25 MB… Comece pela Parte 11"; botão "Quero o playbook" → "Liberar meu playbook".
- **Último relatório (`screens/06-v2/relatorio.json`):** `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:211ms`.
- **Pendências para o Julio:** (1) confirmar a distribuição pública do case "marca DTC de suplementos, R$1,57 mi" (pág. 22) e da nota de fontes (pág. 147) do PDF; (2) o PDF tem 25 MB — se quiser, gerar versão comprimida para celular; (3) envio do PDF por e-mail/WhatsApp depende de `WEBHOOK_URL` + automação (a página não promete envio); (4) `DOWNLOAD_URL` é caminho relativo: funciona quando `dist/` for publicado em fullxmarketing.com (o PDF entra no deploy, 25 MB).
- **Checklist COPY (verificado):** [x] promessa bate com o material real · [x] nenhum número fora dos permitidos · [x] zero placeholder visível · [x] CTA diz o que acontece · [x] sem clichês da lista · [x] sem promessa de e-mail.
- **Checklist ENGENHARIA (verificado):** [x] formulário envia e libera o download (Playwright) · [x] PDF responde 200 · [x] 1 h1 · [x] 0 erro de console · [x] 0 rolagem horizontal em 390 e 1440 · [x] contrato `name/data-funil/data-evento/fid` preservado.
- **Status: CONCLUÍDA.**
