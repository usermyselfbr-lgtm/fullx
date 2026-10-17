# 08 · /espera — Antes de sair (backredirect)

- **Rota:** `/espera/` (noindex,nofollow, aplicado no build por `_rotas.NOINDEX`) · **Fonte:** `paginas/p08_backredirect.py`
- **Mercado / ICP:** quem aperta "voltar" em outra página do funil (dono de agência/gestor que não converteu na oferta principal).
- **Objetivo:** recuperar o visitante com uma oferta menor: o mesmo Playbook Full10X da página 06. Formulário `backredirect` (nome + e-mail, evento `Lead`) → download na hora (`data-dl="DOWNLOAD_URL"` = `/playbook/Playbook-Full10X.pdf`).
- **Isca:** decisão (a), registrada em `06-playbook.md` (PDF real de 147 páginas, "Playbook Full10X · Mais clientes & receita"). O arquivo fica servido em `/playbook/…`; esta página só aponta para ele.

## 1. Diagnóstico (baseline `screens/baseline/espera-*.png`)
- Copy curta e boa no tom, mas descreve um material que não existe ("modelo de formulário que qualifica lead").
- Promessa falsa de entrega: título "Receba no e-mail" e sucesso "Enviado. Confira seu e-mail." — não há envio de e-mail (`WEBHOOK_URL` vazio, nenhuma automação).
- `DOWNLOAD_URL` vazio: botão de download morto. Sem bullets: o visitante não sabe o que leva.
- Técnica: 0 overflow, 0 erro, link de saída "Não, obrigado. Ir para o site." → `01-institucional.html` (mantido).

## 2. Research
- **FATOS:** o mesmo da página 06 (PDF de 147 páginas, 11 partes, plano de 6 semanas, edição 2026).
- **HIPÓTESES:** quem sai não lê página longa; precisa de promessa + 3 bullets + 2 campos (Rapid Lead Generator).
- **AUSENTES:** envio por e-mail.

## 3. Brief RMBC (curto)
- Consciência: consciente do problema, recusou a oferta maior. Dor: "o mês depende de indicação; só você vende". Mecanismo: falta estrutura, não esforço. Promessa: levar o playbook inteiro grátis, download na hora. Prova: o próprio material (nº de páginas e partes reais). Objeção principal: "não quero compromisso" → 2 campos, sem WhatsApp, link de saída visível. CTA: "Baixar o playbook grátis".
- Arquitetura: marca → eyebrow → H1 → lead → 3 bullets → formulário → link de saída. Sem menu e sem rodapé.

## 4. Headlines (15)
1. Antes de sair, leve o playbook. 147 páginas, grátis. ← **escolhida**
2. Leve pelo menos o playbook. É grátis.
3. Não vai seguir agora? Leve o mapa da agência inteira.
4. Saia com o plano de 6 semanas na mão.
5. 147 páginas de oferta, funil, comercial e retenção. De graça.
6. A call fica para depois. O playbook pode ir agora.
7. Não precisa decidir nada hoje. Só leve o playbook.
8. Seu problema não é conhecimento. É instalação. Comece por aqui.
9. Um PDF para parar de recomeçar o mês do zero.
10. Atrair, filtrar, fechar e sustentar, no seu ritmo.
11. Leve o que a gente ensina, sem call e sem compromisso.
12. O playbook inteiro, em troca de um e-mail.
13. Vai embora? Leve o plano de 6 semanas.
14. Mais clientes e receita: o playbook, grátis, antes de você sair.
15. Fica a dica: 147 páginas para ler quando der.
→ Escolhida a 1: mantém o "antes de sair" (contexto da página), troca o vago "pelo menos" por uma especificidade verdadeira (147 páginas) e diz o preço.

## 5. Copy completa
- **Eyebrow:** Antes de sair
- **H1:** Antes de sair, leve o playbook. 147 páginas, grátis.
- **Lead:** Não quis seguir agora? Tudo bem. O Playbook Full10X fica com você para aplicar no seu ritmo.
- **Bullets:**
  1. As 5 métricas que dizem se a agência pode escalar: CAC, LTV, retorno, ticket e conversão.
  2. Pré-vendas e vendas no papel: os 4 tipos de SDR, a call do closer e o pipeline do CRM.
  3. O plano de 6 semanas para implantar um módulo por vez, com checklist.
- **Formulário:** título "Grátis · download na hora"; legenda "Libere o seu PDF"; campos nome e e-mail (inalterados); botão "Baixar o playbook grátis".
- **Sucesso:** "O playbook é seu." / "PDF de 25 MB: no 4G, salve para ler depois." / "Baixar o playbook (PDF)".
- **Saída:** "Não, obrigado. Ir para o site." → `01-institucional.html`.
- **Description:** "Leve grátis o Playbook Full10X: 147 páginas de oferta, funil, comercial e retenção para donos de agência."

## 6. Implementação
- `paginas/p08_backredirect.py`: H1, lead, 3 bullets (lista local `BULLETS`, renderizados com a classe existente `proof-line` em coluna, inline style mínimo), título/legenda/botão do formulário e tela de sucesso reescritos; `DOWNLOAD_URL:'/playbook/Playbook-Full10X.pdf'`. Campos `nome`/`email`, `data-funil="backredirect"`, `data-evento="Lead"` intactos. Link de saída mantido em `01-institucional.html` (vira `/institucional/` no build, conferido no `dist`).
- `python3 _gerar.py` → `12 páginas` (`rc=0`); `todo=0` no `dist/espera/index.html`.

## 7. Ajuste visual
- `08-v1` (390 e 1440 conferidos): H1 em 4 linhas no celular, bullets alinhados à esquerda dentro de 460px, formulário e link de saída visíveis, sem corte. Nenhum ajuste necessário.

## 8. Engenharia
- Playwright: envio do formulário → `espera okVisible= true href= /playbook/Playbook-Full10X.pdf h1= 1 robots= 1` (noindex presente); `pageerrors 0`.
- Sem menu e sem rodapé (Rapid Lead Generator); sem backredirect próprio.

## 9. Revisão editorial
- Removidos "Receba no e-mail" e "Enviado. Confira seu e-mail." (não há envio). "Leve pelo menos o playbook" → promessa específica com o nº real de páginas. Busca de proibidos no `dist/espera/index.html` → `0`.

## 10. Documentação / resultado
- **Antes → depois:** H1 "Leve pelo menos o playbook. É grátis." → "Antes de sair, leve o playbook. 147 páginas, grátis."; lead "modelo de formulário que qualifica lead" → "O Playbook Full10X fica com você para aplicar no seu ritmo."; +3 bullets reais; sucesso falso de e-mail → download na tela.
- **Último relatório (`screens/08-v1/relatorio.json`):** `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:224ms`.
- **Pendências para o Julio:** ligar `BACK_URL` nas outras páginas apontando para `/espera/` (decisão de quais páginas usam backredirect); demais pendências do PDF em `06-playbook.md`.
- **Checklist COPY:** [x] promessa + 3 bullets + formulário · [x] números só os do PDF (147 páginas, 6 semanas, 5 métricas, 4 tipos de SDR) · [x] zero placeholder · [x] sem promessa de e-mail.
- **Checklist ENGENHARIA:** [x] download liberado após envio · [x] noindex · [x] link de saída → /institucional/ · [x] 0 erro de console · [x] 0 rolagem horizontal.
- **Status: CONCLUÍDA.**
