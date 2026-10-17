# 01b · /conteudos/ — Conteúdos gratuitos

- **Rota:** `/conteudos/` · **Fonte:** `paginas/p01b_blog.py` + lista `POSTS` e função `post_cards` em `_comum.py` (exceção autorizada pelo orquestrador)
- **Mercado / ICP:** dono de agência ou gestor de tráfego R$10–80 mil/mês; chega pelo menu, rodapé, bio ou busca. Consciência: do problema.
- **Objetivo:** levar a um conteúdo real (aula ao vivo, playbook, aulas em gravação, artigo) e captar o WhatsApp para aviso de conteúdo novo.

## Fase 1 · Diagnóstico (baseline `screens/baseline/conteudos-390.png`)
- 6 cartões fictícios (aulas de 42 e 35 min, playbooks de 18 e 12 páginas, 2 artigos), todos com o mesmo link para o artigo. Eyebrow promete "Conteúdo gratuito toda semana" (não existe calendário). Lead "Sem cadastro para ler" falso para playbook e aulas. Formulário genérico ("Avisos de novos conteúdos"). Técnica sem quebras.

## Fase 2 · Research
- **FATOS:** artigo dos 4 funis (escrito nesta rodada, `01c-artigo.md`); Playbook Full10X "Mais clientes & receita", PDF, 147 páginas, plano de 6 semanas (`06-playbook.md`); aula ao vivo gratuita 25/10/2026 14h no Google Meet (FONTE 4a), página `https://www.fullxmarketing.com/`; aulas gratuitas em 5 aulas curtas, em gravação, cadastro para receber quando sair (`07-curso.md`, status CONCLUÍDA).
- **AUSENTES:** frequência de publicação, outros artigos, aulas gravadas com duração.

## Fase 3 · Brief RMBC
- Dor: "Já estudei tráfego, funil e venda e o mês ainda fecha na indicação." Mecanismo: o que falta é o sistema instalado, nos 4 canos. Promessa defensável: tudo aqui é material que existe e fala dos mesmos 4 canos. Provas: o próprio material (147 páginas, data da aula, artigo publicado). Objeções: "é mais conteúdo genérico?" → todos sobre os mesmos 4 canos, da operação própria; "vão me encher de mensagem?" → um aviso por conteúdo novo. CTA: abrir cada conteúdo; "Quero o aviso".
- Arquitetura: hero (o que tem aqui, de verdade) → filtro + 4 cartões → captura de aviso.

## Fase 4 · 15 headlines
1. O sistema da nossa agência, aberto de graça. *(escolhida)* 2. Aulas, playbook e artigo para agência. 3. Os 4 canos da agência, em material gratuito. 4. Comece pelo cano que vaza. 5. Tudo o que roda aqui, explicado. 6. Atrair, filtrar, fechar, sustentar: comece por aqui. 7. Material gratuito para quem já tem cliente. 8. Antes da mentoria, o conteúdo. 9. Você vê a tela, não a teoria. 10. O encanamento da agência, de graça. 11. Quatro materiais, um sistema. 12. Leia, assista, implante. 13. Do anúncio ao boleto pago, em material gratuito. 14. Pare de recomeçar o mês do zero: comece aqui. 15. O que a gente usa, aberto para você.
- Escolha: 1 — diz o que é, de onde vem (operação própria) e o preço, sem prometer frequência.

## Fase 5 · Copy
- **Eyebrow:** "Conteúdo gratuito" (antes "Conteúdo gratuito toda semana").
- **H1:** "O sistema da nossa agência, aberto de graça." (antes "Aulas, playbooks e artigos para agência.")
- **Lead:** "Uma aula ao vivo, um playbook de 147 páginas, aulas curtas em gravação e um artigo. Todos sobre os mesmos 4 canos: atrair, filtrar, fechar e sustentar." (antes "Tudo o que usamos… Sem cadastro para ler.")
- **Filtros:** Todos · Aulas · Playbook · Artigo.
- **Cartões (`POSTS`):** Aula ao vivo "Os 4 canos da agência, abertos na tela" · 25/10 · 14h → fullxmarketing.com · Playbook "Playbook Full10X: mais clientes e receita" · PDF · 147 páginas → /playbook/ · Aulas gratuitas "O sistema Full10X em 5 aulas curtas" · "Em gravação. Cadastre-se e receba cada aula quando ela sair." · Cadastro gratuito → /curso/ · Artigo "Os 4 funis que enchem a agenda comercial de uma agência" · 7 min de leitura → /conteudos/4-funis-agenda-comercial/.
- **Captura:** H2 "Saiu conteúdo novo, você fica sabendo." · lead "Quando a próxima aula ou o próximo material ficar pronto, mandamos o link no seu WhatsApp. Só isso: um aviso por conteúdo." · título do card "Aviso de conteúdo novo" · legenda "Para onde mandamos o aviso?" · botão "Quero o aviso" · erro do WhatsApp "Confira o WhatsApp: DDD + número." · conclusão "Pronto, você está na lista." + botão "Ler o artigo". `name=`, `fid='news'`, `data-funil='blog-newsletter'` mantidos.

## Fase 6 · Implementação
- `p01b_blog.py` reescrito; grade `g2` (4 cartões em 2×2 em vez de 3+1 órfão); `post_cards(len(POSTS),'b')`.
- `_comum.py` (só o autorizado): `POSTS` com 4 conteúdos reais e o link como 6º item da tupla; `post_cards` usa `href="{href}"` da tupla; assinatura `post_cards(n, uid)` mantida; `TH_ART`/`TH_IC` sem mudança. Artigo por último para a página do artigo não se recomendar.
- `python3 _gerar.py` → `12 páginas em .../dist` rc=0. Links gerados: `https://www.fullxmarketing.com/`, `/playbook/`, `/curso/`, `/conteudos/4-funis-agenda-comercial/` (URL absoluta passa intacta: o regex do build só reescreve `0N-nome.html`).

## Fase 7 · Ajuste visual
- `node qa/screens.mjs 01bc-v1 conteudos` → `conteudos overflow:0 console:0 todo:1 placeholders:1 links-quebrados:0 lcp390:217ms`. Print 1440 conferido: 2×2 com cartões de mesma altura, hero em 2 linhas, formulário centralizado. O `todo:1` é o `[RAZÃO SOCIAL · CNPJ]` do rodapé compartilhado.

## Fase 8 · Engenharia
- Filtro testado no navegador (Playwright, script temporário fora do repo): `aulas 2 · playbooks 1 · artigos 1 · todos 4` (rc=0). h1 único, h2 da captura, h3 nos cartões. `console:0`, `links-quebrados:0`.
- **Página 01 (institucional)** chama `post_cards(3,'i')` sob "Comece pelo conteúdo gratuito. Material gratuito para aplicar sozinho, na ordem dos canos.": agora mostra aula ao vivo → /fullxmarketing.com, playbook → /playbook/, aulas → /curso/ (antes: 3 cartões fictícios para o mesmo artigo). `node qa/screens.mjs 01b-inst institucional` → `institucional overflow:0 console:0 todo:1 placeholders:1 links-quebrados:0 lcp390:1434ms` (o todo é o mesmo rodapé). O texto da 01 casa com os cartões.

## Fase 9 · Revisão editorial
- Sem "toda semana", sem duração inventada, sem nº de páginas fora do PDF real. Única promessa de frequência: "um aviso por conteúdo".

## Fase 10 · Documentação
- **Bloqueios:** nenhum.
- **Pendências para o Julio:** (1) depois de 25/10 o cartão "Aula ao vivo" vence: trocar por "gravação" (se houver) ou nova data em `POSTS`; (2) quando a aula 1 for gravada, atualizar o cartão das aulas; (3) quem pede aviso precisa de alguém que mande o aviso: o formulário cai no webhook (`WEBHOOK_URL` ainda vazio).
- **Sugestão para o sistema:** nenhuma além do rodapé com CNPJ (pendência comum).

## Status final: CONCLUÍDA

### Checklist 19 (só o verificado)
- COPY: [x] só conteúdo real · [x] cada cartão com o link certo · [x] hero sem promessa falsa · [x] microcopy do formulário reescrita · [x] filtros com as categorias que sobraram
- ENGENHARIA: [x] overflow 0 · [x] console 0 · [x] links quebrados 0 · [x] filtro funcionando (teste real) · [x] 01 institucional conferida · [ ] todo 0 (rodapé compartilhado)
