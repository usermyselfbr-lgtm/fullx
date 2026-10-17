# 04 · /mentoria — Mentoria individual Full10X (vídeo + aplicação + agenda)

- **Rota:** `/mentoria/` · **Fonte:** `paginas/p04_vsl_form_calendly.py`.
- **Mercado / ICP:** o mesmo do brief único (ver `05-aplicacao.md`, fase 3). Origem: tráfego pago morno, link "Mentoria" do menu.
- **Objetivo:** `SubmitApplication` no formulário `vsl-form-calendly` (4 passos, corte 8). `Schedule` só volta quando houver Calendly.

## Fase 1 · Diagnóstico (baseline `screens/baseline/mentoria-*.png`)
- H1 genérico ("Instale na sua agência o sistema que fecha cliente toda semana") com promessa sem prova (toda semana); nenhum mecanismo, nenhuma dor, nenhuma autoridade além da linha PROOF; "Como funciona" com "1. Assista" (vídeo inexistente) e "3. Agende" (Calendly inexistente); `done4` "Escolha o horário" abriria o aviso "Configure CALENDLY_URL"; botão final "Ver horários" prometia agenda; passo 4 com `[R$X e R$Y]`; sem barra de CTA no celular.

## Fase 2 · Research
Mesmos FATOS/HIPÓTESES/AUSENTES de `05-aplicacao.md`. Específico desta página: as 4 dores literais da AULA-A (itens 7 a 10 da seção 7 da fonte), a bio literal do Julio (AULA-A:653, com "Full10X") e a assinatura da variante B ("Eu mostro o que roda, não o que li.").

## Fase 3 · Brief (diferenças em relação ao brief único)
- **Ângulo:** promessa-mecanismo para quem já viu anúncio ou aula: "o sistema da nossa agência, instalado na sua".
- **Arquitetura:** (1) hero: H1 + lead com entregáveis e ICP + vídeo (some quando `VIDEO_URL` vazio) + PROOF | formulário 4 passos; (2) "Toda agência vaza em pelo menos um cano": 4 dores, uma por cano (mecanismo do problema); (3) "O que a mentoria instala, na ordem em que o dinheiro passa": 4 passos ligados (mecanismo da solução); (4) "Você vê a tela, não a teoria": bio + 3 números permitidos (autoridade); (5) Como funciona em 3 passos sem vídeo nem agenda + CTA; (6) FAQ local `FAQ_04` (mesmas objeções da 05 + "o que acontece depois que eu envio"); barra do celular.
- **Sem vídeo:** a lead e as seções carregam todo o argumento; nada diz "assista". **Com vídeo:** o player entra entre a lead e o PROOF e a página continua coerente.

## Fase 4 · 15 headlines
1. O sistema que roda a nossa agência, instalado na sua. *(escolhida)*
2. Seu problema não é conhecimento. É instalação.
3. Anúncio, formulário, CRM, roteiro e cobrança: ligados na sua agência.
4. Pare de recomeçar o mês do zero. Instale os quatro canos.
5. A mentoria individual que monta, na sua agência, o encanamento da nossa.
6. Curso ensina a peça. Aqui você liga as peças.
7. Sua agência vaza em algum cano. A mentoria fecha os quatro.
8. Do anúncio ao boleto pago, na ordem em que o dinheiro passa.
9. Quem tem verba chega na call. O curioso fica no formulário.
10. Você vê a tela, não a teoria. E monta a mesma na sua agência.
11. Daqui a 90 dias, sua agência vai depender de quem?
12. O encanamento de uma agência que vende sem depender do dono.
13. Instale na sua agência o CRM e a cobrança que rodam na nossa.
14. Feche cliente sem depender de indicação nem de você em toda call.
15. Mentoria individual Full10X: o sistema, não a aula.
**Escolha:** a 1 é específica (sistema de uma agência real), defensável (CRM e cobrança existem e rodam) e não promete prazo nem número.

## Fase 5 · Copy (peças-chave)
- **H1:** O sistema que roda a nossa agência, instalado na sua.
- **Lead:** Anúncio, formulário que pontua o lead, CRM, roteiro de venda e cobrança, ligados entre si e montados com você na sua operação. Para donos de agência e gestores de tráfego que faturam de R$10 mil a R$80 mil por mês.
- **Formulário:** título "Aplicação · 4 perguntas"; passo 1 "Para o time falar com você se você for aprovado."; passo 4 com R$2.500–5.000; botão "Enviar aplicação" (era "Ver horários").
- **done4:** "Você foi aprovado." / "O time fala com você em até 24 horas úteis para marcar a conversa. Fique de olho no WhatsApp que você informou."
- **Autoridade:** bio literal + stats "+R$10 milhões / em tráfego gerenciado", "+2.300 / clientes de serviço gerados", "+R$100 mil / a primeira agência passou de R$100 mil em 90 dias".
- **Como funciona:** 1. Responda 4 perguntas · 2. O time fala com você (24 h úteis) · 3. Conversa sobre a sua agência.

## Fase 6 · Implementação
- `.py` reescrito; contrato do formulário intacto (`data-corte=8`, `data-funil="vsl-form-calendly"`, `SubmitApplication`, `fid`, `name`, `data-s`). Wrapper `delayed wait data-delay="60"` mantido para o cenário com vídeo. `<div data-calendly>` removido do `done4` (comentário no `.py` explica como recolocar). Listas locais `DORES_04`, `CANOS_04`, `FAQ_04`. `mbar('Aplicar para a mentoria')` adicionado.
- `python3 _gerar.py` → `12 páginas em …/dist` (rc=0); `todo` = 0.

## Fase 7 · Ajuste visual
- `node qa/screens.mjs 04-v1 mentoria` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:248ms`. No 1440 os números da autoridade quebravam em 2 linhas dentro do `split` → autoridade virou cabeçalho + `stats` em largura cheia.
- `node qa/screens.mjs 04-v2 mentoria` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:230ms`. PNGs conferidos.
- Observação: nos prints o formulário aparece vazio porque o `_sistema.py` atual ainda segura o `.delayed` por 60 s e mostra o texto "Configure VIDEO_URL" no player; o ajuste anunciado pelo orquestrador (esconder player e liberar formulário com `VIDEO_URL` vazio) resolve sem mudança nesta página.

## Fase 8 · Engenharia
- 1 `h1`, 5 `h2`; CTA "Responder as 4 perguntas" e barra do celular → `#form`; links internos `/institucional/` e `/playbook/` válidos; 0 erro de console.

## Fase 9 · Revisão editorial
- Proibidos buscados no `dist/` (vagas, turma, grupo pequeno, garantia, gateway, IA comercial, clichês): 0. Único "90 dias" visível é a frase permitida da primeira agência. "toda semana" removido do H1 (prometia frequência sem prova).

## Fase 10 · Documentação
- **Antes → depois:** H1 "Instale na sua agência o sistema que fecha cliente toda semana." → "O sistema que roda a nossa agência, instalado na sua."; "Aplique e agende sua call"/"Ver horários" → "Aplicação · 4 perguntas"/"Enviar aplicação"; done "Você foi aprovado para a call. Escolha o horário…" → "Você foi aprovado. O time fala com você em até 24 horas úteis para marcar a conversa."; +3 seções (dores, canos, autoridade).
- **Bloqueios:** nenhum.
- **Pendências para o Julio:** quando existir agenda, recolocar `<div data-calendly></div>` no `done4` e voltar o passo 3 de "Como funciona" para agenda.
- **Sugestões para arquivos compartilhados:** com vídeo configurado, os botões `data-go="#form"` levam ao formulário ainda bloqueado pelo `data-delay`; sugerir que o clique num CTA libere o `.delayed` (`_sistema.py`).
- **Status:** CONCLUÍDA.

### Checklist COPY
- [x] Mesmo mecanismo, promessa e objeções das páginas 05 e 03
- [x] Funciona sem vídeo e sem agenda
- [x] Só números permitidos, com a redação da home
### Checklist ENGENHARIA
- [x] `todo:0 placeholders:0 overflow:0 console:0` (04-v2)
- [x] Contrato do formulário intacto; hierarquia de títulos; links válidos
