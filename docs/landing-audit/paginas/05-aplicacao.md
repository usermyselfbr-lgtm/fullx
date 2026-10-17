# 05 · /aplicacao — Aplicação para a mentoria individual Full10X

- **Rota:** `/aplicacao/` · **Fonte:** `paginas/p05_aplicacao.py` · destino do botão "Falar com o time" do site.
- **Mercado / ICP:** dono de agência ou gestor de tráfego com clientes próprios, R$10 mil a R$80 mil/mês, Brasil, consciente da solução (viu anúncio, aula ou clicou em "Falar com o time").
- **Objetivo:** `SubmitApplication` no formulário `aplicacao` (8 passos, corte 9).
- **Este arquivo guarda o brief RMBC único das três páginas da mentoria** (05, 04, 03). `04-mentoria.md` e `03-assista.md` só registram as diferenças de ângulo.

## Fase 1 · Diagnóstico (baseline `screens/baseline/aplicacao-*.png` + `dist/` anterior)
- Copy: H1 descritivo ("Aplicação para a mentoria Full10X."); eyebrow "Vagas limitadas por turma" (escassez sem base e formato errado: a mentoria publicada é individual); card "Cada turma tem [XX] vagas… grupo pequeno" (placeholder + fato inexistente); "implantar em 90 dias" (duração não decidida); passo 7 com `[R$X e R$Y]`. Nenhum argumento sobre o que a mentoria instala; nenhuma FAQ; uma única seção abaixo da dobra ("Quem é aprovado", boa).
- Conversão: quem chega por "Falar com o time" espera conversar; a página não explicava por que há formulário nem o que acontece depois. Sem CTA de retorno no fim da página (só a barra do celular).
- Técnica: 2 `.todo` visíveis, PROOF já corrigido pelo orquestrador; 0 overflow / 0 console no baseline.

## Fase 2 · Research (FONTE-DA-VERDADE)
**FATOS usados:** mentoria individual (AULA-A); faixa R$2.500 a R$5.000 (AULA-A, pergunta 7); resposta em até 48 h úteis (p05); +R$10 milhões em tráfego gerenciado; +2.300 clientes de serviço gerados; "a primeira agência passou de R$100 mil em 90 dias" (decisões do orquestrador); 4 canos Atrair/Filtrar/Fechar/Sustentar "na ordem em que o dinheiro passa"; CRM próprio com formulário que pontua, tarefas de SDR e WhatsApp dentro do CRM; régua de cobrança por WhatsApp; bio literal do Julio; frases literais: "Seu problema não é conhecimento. É instalação.", "Curso ensina a peça…", "Você vê a tela, não a teoria.", "Eu mostro o que roda, não o que li.", "Lead chega, mas sem verba. A semana vai embora em call com curioso.", "Só você vende. Sem roteiro e sem CRM, cada call é um chute.", "Cliente cancela em 3 meses. Boleto atrasa.", "É o critério que separa quem tem verba de quem é curioso, antes de gastar uma call.", "Sua agência anuncia todo dia e o mês ainda fecha na indicação? Então o problema não é mais lead. É o que acontece depois que ele chega." (ANUNCIOS 01). O próprio formulário da página pontua (`data-s`, `data-corte`).
**HIPÓTESES (não usadas como fato):** garantia de instalação; duração 30/90 dias; "Sistema de Demanda Qualificada"; "Não estude. Instale."; IA operacional como entrega.
**AUSENTES:** vídeo, Calendly, WhatsApp oficial, turma/vagas, garantia, cases nomeados, duração, quem conduz as sessões, cadência das sessões.

## Fase 3 · Brief RMBC (vale para 05, 04 e 03)
- **Avatar:** dono de agência / gestor de tráfego, R$10–80 mil/mês, vende serviço recorrente, já estudou tráfego e venda.
- **Consciência:** consciente da solução (sabe que precisa de "sistema"; duvida de mais um curso).
- **Dor central (literal):** "Lead chega, mas sem verba. A semana vai embora em call com curioso." + "o mês ainda fecha na indicação".
- **Inimigo:** a agência que vende, cobra e opera na mão do dono; o curso que ensina a peça e pula a ligação entre elas.
- **Mecanismo do problema:** a agência não trava por falta de técnica; vaza em pelo menos um dos quatro canos, porque nada está ligado: o lead não é filtrado, a venda depende do dono, a cobrança depende de lembrar.
- **Mecanismo da solução:** o sistema Full10X, os quatro canos Atrair → Filtrar → Fechar → Sustentar, rodando primeiro na nossa agência (CRM e cobrança próprios) e instalado com você.
- **Big idea:** "Seu problema não é conhecimento. É instalação." Você vê a tela, não a teoria.
- **Promessa defensável:** instalar na sua agência, com acompanhamento individual, o mesmo encanamento (anúncio, formulário que pontua, CRM, roteiro de venda, cobrança) que roda na nossa. Sem prazo de resultado e sem número de cliente prometido.
- **3 provas:** +R$10 milhões em tráfego gerenciado; +2.300 clientes de serviço gerados; a primeira agência passou de R$100 mil em 90 dias. Prova por demonstração: o formulário da própria página pontua e tem nota de corte.
- **Objeções e respostas:** preço → faixa publicada R$2.500–5.000, valor final na conversa; "já fiz curso" → curso ensina a peça, aqui é a ligação, na tela; "meu nicho" → o sistema é da agência, não do cliente final; "não tenho tempo" → falta de tempo é o sintoma; mentoria individual, ritmo combinado; "e se eu não for aprovado" → resposta na hora + conteúdo gratuito + pode reaplicar; "por que aplicação" → individual, parte da operação real.
- **Oferta:** mentoria individual Full10X de implantação. Sem bônus, sem garantia, sem escassez (nada disso existe).
- **CTA:** "Enviar aplicação" (form) / "Responder as 8 perguntas" (fim) / "Enviar minha aplicação" (barra do celular).
- **Arquitetura 05:** (1) hero: H1 + lead que explica o processo e o prazo + formulário + card "Você está usando o filtro agora" (prova por demonstração) + PROOF; (2) Quem é aprovado (qualifica e desqualifica); (3) O que a mentoria instala, 4 canos (mecanismo da solução); (4) Perguntas antes de aplicar (objeções) + CTA de volta ao formulário.
- **Ângulo por página:** 05 = quem já decidiu conversar (abre pelo filtro e pelo processo); 04 = tráfego pago morno (abre pela promessa-mecanismo "o sistema da nossa agência, instalado na sua"); 03 = tráfego pago mais frio, mesmo hook do anúncio 01 (abre pela dor "anuncia todo dia e fecha na indicação").

## Fase 4 · 15 headlines (05)
1. Antes de falar com o time, mostre onde sua agência vaza. *(escolhida)*
2. Aplique para instalar na sua agência o sistema que roda na nossa.
3. Oito perguntas separam você de uma conversa sobre a sua agência.
4. Este formulário já é parte do sistema que você vai instalar.
5. Conte onde o dinheiro escapa. Em até 48 horas úteis você sabe se a mentoria resolve.
6. Seu problema não é conhecimento. Aplique para a instalação.
7. A mentoria é individual. Por isso ela começa pelas suas respostas.
8. Quem tem verba chega na conversa. Este formulário decide.
9. Aplicação para a mentoria individual Full10X.
10. Mostre sua operação. A gente mostra qual cano instalar primeiro.
11. O mesmo filtro que você vai instalar decide se a conversa acontece.
12. Sua agência fecha na indicação? Comece por aqui.
13. Da indicação ao sistema: aplique para a mentoria individual.
14. Antes da call, a pontuação. Como na nossa agência.
15. Responda 8 perguntas e pare de recomeçar o mês do zero.
**Escolha:** a 1 casa com o botão de origem ("Falar com o time"), explica por que há formulário e usa o vocabulário da marca (vazar/cano) sem prometer o que não existe.

## Fase 5 · Copy (peças-chave; texto completo no `.py`)
- **Eyebrow:** Mentoria individual Full10X.
- **H1:** Antes de falar com o time, mostre onde sua agência vaza.
- **Lead:** São 8 perguntas sobre a sua operação. Lemos cada aplicação e respondemos no WhatsApp em até 48 horas úteis. Se fizer sentido, a conversa já começa pelo seu gargalo.
- **Card de prova:** "Você está usando o filtro agora" — cada resposta vale pontos e há nota de corte; é o cano Filtrar que a mentoria instala.
- **Quem é aprovado:** 4 × 4 itens (inclui "procura alguém para rodar o tráfego dos seus clientes no seu lugar" como desqualificador).
- **4 canos:** Atrair / Filtrar / Fechar / Sustentar com o que é instalado em cada um.
- **FAQ local `FAQ_05`:** preço, "já fiz curso", nicho, tempo, não aprovado, por que aplicação.
- **Microcopy:** passo 2 "A resposta chega no WhatsApp em até 48 horas úteis."; passo 5 "Contando você."; passo 6 "Onde sua agência mais vaza hoje? Escolha um. É por ele que a conversa começa."; passo 7 com a faixa R$2.500–5.000; passo 8 sem "90 dias"; erro do WhatsApp "Confira o WhatsApp: DDD + número."; conclusão "Vamos ler suas respostas e falar com você no WhatsApp em até 48 horas úteis."

## Fase 6 · Implementação
- `paginas/p05_aplicacao.py` reescrito; `name=`, `data-s`, `data-corte=9`, `data-funil="aplicacao"`, `data-evento="SubmitApplication"` e `fid` intactos. Listas locais `FAQ_05` e `CANOS_05`. Só classes existentes (`card`, `k`, `compare`, `grid g2`, `faq`, `cta-row`, `btn-m`).
- `python3 _gerar.py` → `12 páginas em …/dist` (rc=0); `grep -c 'class="todo"' dist/aplicacao/index.html` → 0.

## Fase 7 · Ajuste visual
- `node qa/screens.mjs 05-v1 aplicacao` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:288ms`. No 390 px o card de prova empurrava o formulário para baixo da dobra → card movido para baixo do formulário (coluna direita no desktop, logo após o formulário no celular); rótulo "1. Cano" → "Cano 1".
- `node qa/screens.mjs 05-v2 aplicacao` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:295ms`. PNGs 390 e 1440 conferidos: cartões dos canos com alturas iguais por linha, compare equilibrado, FAQ legível no fundo claro.

## Fase 8 · Engenharia
- 1 `h1`, 3 `h2`, `h3` dentro de cartões; links internos `/institucional/` (logo) e `/playbook/` (NOK compartilhado) existem; CTA final e barra do celular usam `data-go="#form"` (id do `form_card`); `data-pos` distintos (`fim-da-pagina`, `barra-celular`). 0 erro de console. Sem imagem nova (nenhum `alt` a acrescentar).

## Fase 9 · Revisão editorial
- Leitura na ordem do visitante; busca por proibidos no `dist/` (vagas, turma, grupo pequeno, garantia, gateway, IA comercial, 90 dias, clichês) → nenhuma ocorrência na página (o único "90 dias" do HTML é comentário de rastreio de UTM do sistema). Cortados: "Aprovamos só quem conseguimos ajudar de verdade" do hero (mantido só na FAQ), adjetivos e a escassez.

## Fase 10 · Documentação
- **Antes → depois:** H1 "Aplicação para a mentoria Full10X." → "Antes de falar com o time, mostre onde sua agência vaza."; eyebrow "Vagas limitadas por turma" → "Mentoria individual Full10X"; card "Cada turma tem [XX] vagas…" → "Você está usando o filtro agora…"; "Está pronto para implantar em 90 dias" → removido; `[R$X e R$Y]` → "entre R$2.500 e R$5.000"; +2 seções (4 canos, FAQ) e CTA final.
- **Mudanças técnicas:** apenas texto/estrutura no `.py`; nenhum CSS novo; nenhum inline além de `margin`/`max-width` de layout.
- **Testes executados:** ver fases 6 e 7 (saídas literais acima).
- **Bloqueios:** nenhum.
- **Pendências para o Julio:** confirmar se a conversa pós-aprovação é com o time (texto atual) ou com o Julio; cadência das sessões da mentoria (a FAQ "não tenho tempo" evita afirmar).
- **Sugestões para arquivos compartilhados:** `NOK()` aponta para `/playbook/`, cujo PDF ainda não existe (orquestrador decide).
- **Status:** CONCLUÍDA.

### Checklist (seção COPY)
- [x] Above the fold diz o que é, para quem, o que acontece e o que fazer
- [x] Mecanismo nomeado (4 canos) e igual ao das páginas 04 e 03
- [x] Só números permitidos (+R$10 milhões, +2.300, R$100 mil em 90 dias via PROOF/página 04)
- [x] Objeções reais na FAQ
- [x] Sem turma, vagas, garantia, duração, cases
- [x] CTAs com verbo e consequência

### Checklist (seção ENGENHARIA)
- [x] `todo:0 placeholders:0 overflow:0 console:0` (05-v2)
- [x] Contrato do formulário intacto (`name`, `data-s`, `data-corte`, `data-funil`, `data-evento`, `fid`)
- [x] Hierarquia h1 > h2 > h3; links internos válidos
