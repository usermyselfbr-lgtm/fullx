# 03 · /assista — Mentoria individual Full10X (vídeo + qualificação)

- **Rota:** `/assista/` · **Fonte:** `paginas/p03_vsl_qualificacao.py`.
- **Mercado / ICP:** o mesmo do brief único (`05-aplicacao.md`, fase 3). Origem: tráfego pago, o mais frio dos três (hook do anúncio 01).
- **Objetivo:** `SubmitApplication` no formulário `vsl-qualificacao` (5 passos, corte 8).

## Fase 1 · Diagnóstico (baseline `screens/baseline/assista-*.png`)
- H1 "Como agências de R$10 mil a R$30 mil passam a fechar cliente toda semana" (promessa sem prova e faixa diferente da aplicação); seção "O que você vai ver no vídeo" com 3 `[PONTO DO VÍDEO]`; nota "Ative o som. O formulário aparece durante o vídeo" (falsa sem vídeo); passo 5 com `[R$X e R$Y]`; done com botão "Adiantar pelo WhatsApp" apontando para o número placeholder `5500000000000`; formulário invisível por 90 s; sem barra de CTA.

## Fase 2 · Research
Mesmos FATOS/HIPÓTESES/AUSENTES de `05-aplicacao.md`. Específico: hook literal do anúncio 01 ("Sua agência anuncia todo dia e o mês ainda fecha na indicação? Então o problema não é mais lead. É o que acontece depois que ele chega.").

## Fase 3 · Brief (diferenças)
- **Ângulo:** problema-solução com match de anúncio; o mecanismo aparece como "o problema é o que acontece depois que o lead chega".
- **Arquitetura:** (1) hero centrado: H1 pergunta + lead + vídeo (some sem `VIDEO_URL`) + formulário 5 passos + PROOF; (2) "O que o sistema instala na sua agência": 3 pontos verdadeiros (Filtrar, Fechar, Sustentar) + linha de prova (substitui os `[PONTO DO VÍDEO]` e funciona com ou sem vídeo); (3) "Para quem é" (compare enxuto, mesmo critério da 05) + CTA; (4) FAQ local `FAQ_03`; barra do celular.

## Fase 4 · 15 headlines
1. Sua agência anuncia todo dia e o mês ainda fecha na indicação? *(escolhida)*
2. O problema não é mais lead. É o que acontece depois que ele chega.
3. Você enche a agenda de call e o mês não fecha?
4. Lead sem verba come a sua semana. Instale o filtro antes da call.
5. Toda agência vaza em pelo menos um cano. Veja qual é o seu.
6. Por que a agência que anuncia todo dia ainda vive de indicação.
7. Curioso na call, boleto atrasado, só você vendendo: um sistema resolve os três.
8. Seu problema não é conhecimento. É instalação.
9. O que acontece depois do lead decide o seu mês.
10. Anúncio você já sabe rodar. Falta o encanamento depois dele.
11. Filtro, CRM, roteiro e cobrança: o que roda na nossa agência.
12. Daqui a 30 dias, de onde vem o seu próximo cliente?
13. A semana vai embora em call com curioso? Comece pelo filtro.
14. Agência de R$10 mil a R$80 mil: pare de recomeçar o mês do zero.
15. Você gerencia o tráfego do cliente. Quem gerencia o da sua agência?
**Escolha:** a 1 repete o hook do anúncio 01 (match mensagem-página) e nomeia a dor que o ICP reconhece em 5 segundos.

## Fase 5 · Copy (peças-chave)
- **Eyebrow:** Mentoria individual Full10X (era "Assista antes de aplicar").
- **H1:** Sua agência anuncia todo dia e o mês ainda fecha na indicação?
- **Lead:** Então o problema não é mais lead. É o que acontece depois que ele chega. Na mentoria individual Full10X você instala na sua agência o filtro, o CRM, o roteiro de venda e a cobrança que rodam na nossa.
- **3 pontos:** Um filtro antes da call · Um comercial que não depende só de você · Uma cobrança que não depende de lembrar.
- **Formulário:** "Aplicação · 5 perguntas"; passo 4 "Onde sua agência mais vaza hoje?"; passo 5 com R$2.500–5.000.
- **done3:** "Aplicação recebida." / "O time fala com você pelo WhatsApp em até 24 horas úteis, já com o cano que você marcou como ponto de partida." (botão de WhatsApp removido enquanto não houver número oficial).

## Fase 6 · Implementação
- `.py` reescrito; contrato intacto (`data-corte=8`, `vsl-qualificacao`, `SubmitApplication`, `name`, `data-s`, `fid`). `delayed wait data-delay="90"` mantido para o cenário com vídeo; nota "Ative o som…" removida. Listas locais `PONTOS_03`, `FAQ_03`.
- `python3 _gerar.py` → `12 páginas em …/dist` (rc=0); `todo` = 0.

## Fase 7 · Ajuste visual
- `node qa/screens.mjs 03-v1 assista` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:275ms`. Defeito: compare em seção escura deixava o título "Não é para você se" claro sobre cartão branco (ilegível) → temas trocados (3 pontos em seção escura, "Para quem é" em seção clara).
- `node qa/screens.mjs 03-v2 assista` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:242ms`. PNGs conferidos. O espaço vazio no hero é o formulário segurado pelo `.delayed` do sistema atual (ver nota da 04).

## Fase 8 · Engenharia
- 1 `h1`, 3 `h2`; CTA "Responder as 5 perguntas" e barra do celular → `#form`; links internos válidos; 0 erro de console.

## Fase 9 · Revisão editorial
- Proibidos no `dist/`: 0. Promessa "fechar cliente toda semana" removida. Ritmo: lead em 3 frases curtas.

## Fase 10 · Documentação
- **Antes → depois:** H1 "Como agências de R$10 mil a R$30 mil passam a fechar cliente toda semana." → "Sua agência anuncia todo dia e o mês ainda fecha na indicação?"; "O que você vai ver no vídeo" + 3 `[PONTO DO VÍDEO]` → "O que o sistema instala na sua agência" com 3 pontos verdadeiros; done "Um especialista vai falar com você…" + botão WhatsApp → texto sem botão; + "Para quem é" e CTA.
- **Bloqueios:** nenhum.
- **Pendências para o Julio:** quando houver WhatsApp oficial, recolocar o botão "Adiantar pelo WhatsApp" no `done3`; quando houver vídeo, ajustar `data-delay` ao minuto da oferta.
- **Sugestões para arquivos compartilhados:** a mesma da 04 (CTA libera o `.delayed`).
- **Status:** CONCLUÍDA.

### Checklist COPY
- [x] Match com o anúncio 01; mecanismo e objeções iguais às páginas 05 e 04
- [x] Seção do vídeo funciona sem vídeo
### Checklist ENGENHARIA
- [x] `todo:0 placeholders:0 overflow:0 console:0` (03-v2)
- [x] Contrato do formulário intacto; hierarquia; links válidos
