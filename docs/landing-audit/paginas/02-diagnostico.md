# 02 · /diagnostico — Call de diagnóstico (30 minutos)

- **Rota:** `/diagnostico/` · **Fonte:** `paginas/p02_form_calendly.py` (gera `02-form-calendly.html` → `dist/diagnostico/index.html`).
- **Mercado / ICP:** dono de agência de marketing ou gestor de tráfego com clientes próprios, R$10 mil a R$80 mil/mês, Brasil. Tráfego **morno** (viu conteúdo ou anúncio da Full10X).
- **Objetivo:** pedido de call gratuita de 30 minutos (formulário `form-calendly`, 3 passos, corte 3, evento `Lead`; `Schedule` quando o Calendly existir). Quem não passa no corte vai para o playbook (`NOK()`).

## Fase 1 · Diagnóstico da página anterior (dist + `screens/baseline/diagnostico-*.png`)

**Copy**
- H1 "Descubra em 30 minutos onde sua agência perde venda." é boa: promessa clara, prazo, linguagem do ICP. Mantida como base.
- Lead "uma call com um especialista": quem é o especialista? Vago e genérico. Fala "captação, comercial e cobrança" em vez dos 4 canos da marca (Atrair, Filtrar, Fechar, Sustentar).
- Não diz que a call é gratuita nem que é sem compromisso. Não avisa que pode haver convite para a mentoria (a home é honesta: "Fica quem quiser").
- Passo 2 "Escolha o horário · A agenda abre logo depois" é falso hoje (sem Calendly).
- Card "Números de referência: custo por lead qualificado, taxa de fechamento e churn esperados para o seu tamanho" promete benchmark por tamanho de agência sem fonte. A FONTE-DA-VERDADE não tem esse dado.
- Nenhuma seção de problema (por que alguém marcaria a call), nenhuma descrição do que acontece nos 30 minutos, nenhum "para quem é / não é", nenhuma prova (nem a linha `PROOF`).
- FAQ = `FAQ_BASE` (perguntas de curso/mentoria: "Isso é curso?"), nenhuma pergunta de quem vai marcar uma call (é venda? quem atende? custa?).
- Botão final "Ver horários" e tela de sucesso "Escolha o melhor horário. Seus dados já estão preenchidos na agenda." + caixa cinza "Agenda de demonstração. Configure CALENDLY_URL no topo do arquivo." visível ao visitante depois de enviar.

**Conversão**
- Página curta demais para tráfego morno: pede a call sem dar razão nem reduzir o risco percebido ("vão me vender algo").
- Fim da página sem CTA de retorno ao formulário (só a barra do celular).

**Técnica**
- Baseline: 0 rolagem horizontal, 0 erro de console. Canônico `grupofull10x.com` (o build troca pelo domínio). No print de 390 px a barra fixa do celular aparece sobre o cartão do formulário: é efeito do print de página inteira com `reducedMotion` (a barra fica sempre visível), não do uso real.

## Fase 2 · Research (FONTE-DA-VERDADE)

**FATOS (pode usar)**
- "+R$10 milhões em tráfego gerenciado"; "+2.300 clientes de serviço gerados" (decisão do orquestrador; via `PROOF`).
- 4 canos "na ordem em que o dinheiro passa": Atrair, Filtrar, Fechar, Sustentar. "Toda agência vaza em pelo menos um." (AULA-A)
- Dores literais: "O mês depende de indicação. Você anuncia para cliente e não para a própria agência." / "Lead chega, mas sem verba. A semana vai embora em call com curioso." / "Só você vende. Sem roteiro e sem CRM, cada call é um chute." / "Cliente cancela em 3 meses. Boleto atrasa." (AULA-A)
- CRM próprio em produção: pipeline, formulário que pontua o lead, tarefas de SDR, WhatsApp no CRM, aba de campanhas com coleta do Meta Ads e origem da venda. Sistema de cobrança próprio com régua por WhatsApp (roda com Asaas por baixo).
- "Você vê a tela, não a teoria." / "No final eu apresento a mentoria FULLX. Fica quem quiser." (AULA-A)
- Mentoria **individual**, investimento "entre R$2.500 e R$5.000" (decisão do orquestrador).
- Público: "Tem agência entre R$10 mil e R$80 mil por mês" / não é para "Ainda não tem nenhum cliente. Procura fórmula sem implementar." (p05)
- Confirmação sem agenda: "o time fala com você em até 24 horas úteis" (decisão do orquestrador).

**HIPÓTESES (não usar como fato)**
- Duração/formato da mentoria além de "individual"; "Sistema de Demanda Qualificada"; "Não estude. Instale."
- Que a call é por vídeo/Google Meet (nenhuma fonte diz o meio da call de diagnóstico).

**AUSENTES**
- Benchmarks de CPL qualificado, taxa de fechamento e churn por tamanho de agência → card reescrito sem prometer benchmark.
- Nome de quem atende a call (o time da Eikon é interno: não citar nomes) → "o time da Full10X".
- Calendly, WhatsApp oficial (pendências comuns).

## Fase 3 · Brief RMBC

- **Avatar:** dono de agência (ou gestor com carteira própria) de R$10 a R$80 mil/mês que já anuncia e já tem cliente, mas o mês oscila.
- **Nível de consciência:** consciente do problema, entrando em consciente da solução (viu conteúdo da Full10X; conhece a dor, não sabe qual parte da operação atacar primeiro).
- **Dor central (literal):** "A semana vai embora em call com curioso." / "O mês depende de indicação."
- **Inimigo:** tentar consertar tudo ao mesmo tempo (mais tráfego, mais curso) sem saber em qual cano o dinheiro escapa.
- **Mecanismo do problema:** a agência vaza em um ponto específico do encanamento (Atrair, Filtrar, Fechar ou Sustentar); mexer nos outros não resolve.
- **Mecanismo da solução:** diagnóstico cano por cano, comparando com o sistema Full10X que roda na nossa operação (CRM, formulário que pontua, régua de cobrança).
- **Big idea:** 30 minutos para saber qual cano vaza primeiro na sua agência.
- **Promessa defensável:** sair da call com o gargalo nomeado e uma ação para aplicar na mesma semana, com ou sem a Full10X.
- **Provas (reais):** +R$10 milhões em tráfego gerenciado; +2.300 clientes de serviço gerados; CRM e cobrança próprios rodando na nossa agência.
- **Objeções → resposta:**
  1. "É venda disfarçada." → É diagnóstico. No final, se o caso pedir, apresentamos a mentoria individual e o investimento. Fica quem quiser.
  2. "Quanto custa?" → Nada. Gratuita, sem compromisso.
  3. "Quem atende?" → O time da Full10X, que opera a própria agência com esse sistema.
  4. "Preciso preparar números?" → Não. Três dados de cabeça bastam.
  5. "E se eu não me encaixar?" → O formulário mostra na hora; quem ainda não está no momento recebe o playbook gratuito.
  6. "Meu nicho é diferente." → O sistema é de captação, comercial e operação de agência de serviço recorrente.
- **Oferta:** call de diagnóstico, 30 minutos, gratuita.
- **CTA:** "Pedir minha call" (formulário) / "Marcar minha call" (barra e fechamento).
- **Arquitetura:**
  1. Hero + formulário: promessa, para quem, gratuita, como marcar, prova (`PROOF`).
  2. Problema (4 canos com as dores literais): o visitante se reconhece num cano.
  3. Como são os 30 minutos (steps): tira o medo do desconhecido e mostra o convite honesto para a mentoria.
  4. O que você leva (3 cards): tangibiliza a entrega sem benchmark inventado.
  5. Para quem é / não é (compare): filtra e prepara quem cai no `NOK`.
  6. FAQ local (`FAQ_02`): objeções de quem vai marcar uma call.
  7. Fechamento com CTA para o formulário.

## Fase 4 · 15 headlines

1. Descubra em 30 minutos onde sua agência perde venda. *(promessa, atual)*
2. Em 30 minutos, a gente acha o cano que está vazando na sua agência. *(mecanismo)*
3. Atrair, Filtrar, Fechar ou Sustentar: em qual a sua agência vaza? *(mecanismo, pergunta)*
4. 30 minutos para nomear o gargalo que segura o faturamento da sua agência. *(especificidade)*
5. Você anuncia todo dia e o mês fecha na indicação? Em 30 minutos você sabe por quê. *(problema-solução)*
6. Saia da call com o gargalo da sua agência nomeado e uma ação para a semana. *(entregável)*
7. Antes de colocar mais verba, descubra em qual cano o dinheiro escapa. *(contrarian)*
8. Uma call de 30 minutos olhando a sua operação pelos 4 canos que rodam na nossa. *(mecanismo + prova)*
9. Onde sua agência perde venda: no anúncio, no filtro, na call ou no boleto? *(especificidade)*
10. A gente abriu a nossa operação cano por cano. Agora olhamos a sua. *(história)*
11. Descubra em 30 minutos em qual dos 4 canos sua agência perde venda. *(promessa + mecanismo)*
12. Lead sem verba, call que não fecha, cliente que cancela: em 30 minutos você sabe qual atacar primeiro. *(problema)*
13. Diagnóstico de 30 minutos para dono de agência que cansou de recomeçar o mês do zero. *(avatar)*
14. Seu problema não é conhecimento. Em 30 minutos, mostramos onde falta instalação. *(marca)*
15. Qual cano vaza primeiro na sua agência? Uma call gratuita de 30 minutos responde. *(pergunta + oferta)*

**Escolhida: 1** — já fala a língua do anúncio e do ICP (match mensagem-página para tráfego morno), cabe em 4 linhas no celular; a especificidade dos 4 canos (9) entra no subtítulo em vez de alongar o H1.

## Fase 5 · Copy completa

**Hero**
- Eyebrow: Call de diagnóstico · 30 minutos · gratuita
- H1: Descubra em 30 minutos onde sua agência perde venda.
- Lead: No anúncio, no filtro, na call ou no boleto. Numa call gratuita com o time da Full10X, olhamos a sua operação pelos 4 canos que rodam na nossa agência e você sai com o gargalo nomeado e uma ação para a semana.
- Passos: 1 Responda 3 perguntas · Para a call começar pelo seu caso, não pelo básico. / 2 Marque o horário · O time confirma com você pelo WhatsApp em até 24 horas úteis. / 3 Faça a call · 30 minutos com o time, cano por cano.
- Prova: `PROOF`.
- Formulário: título "Peça sua call"; passo 1 "Para onde mandamos a confirmação?" · "É por este WhatsApp que o time combina o horário."; passo 2 "Hoje, você é…" · "Para a gente preparar a call certa."; passo 3 "Quanto sua agência fatura por mês?" · "Média dos últimos 3 meses. Fica só entre você e o time."; botão final "Pedir minha call".
- Sucesso (`done2`): "Recebemos." / "O time confirma o horário com você pelo WhatsApp em até 24 horas úteis." / "Enquanto isso, pense em qual dos 4 canos você acha que vaza. Na call, a gente confere." / (só com Calendly configurado) "Se preferir, escolha agora um horário na agenda abaixo." + agenda.

**Problema** — H2: Toda agência vaza em pelo menos um cano. Lead: Quatro canos, na ordem em que o dinheiro passa. Na call, descobrimos qual deles trava o seu faturamento primeiro.
- Atrair: O mês depende de indicação. Você anuncia para cliente e não para a própria agência.
- Filtrar: Lead chega, mas sem verba. A semana vai embora em call com curioso.
- Fechar: Só você vende. Sem roteiro e sem CRM, cada call é um chute.
- Sustentar: Cliente cancela em 3 meses. Boleto atrasa e você cobra no braço.

**Como são os 30 minutos** — H2: Como são os 30 minutos.
1. Suas respostas, lidas antes · A call começa no seu faturamento e no seu perfil, não em apresentação.
2. Os 4 canos, um por um · De onde vem o lead, como ele é filtrado, quem vende e como o cliente paga. Comparando com o que roda na nossa operação.
3. O gargalo com nome · Qual cano vaza primeiro e por que mexer nos outros agora não resolve.
4. Uma ação para a semana · Algo que você aplica em dias, com ou sem a Full10X.
- Nota de honestidade: Se o seu caso pedir acompanhamento, no final apresentamos a mentoria individual Full10X. Fica quem quiser. Quem não quiser sai com o diagnóstico do mesmo jeito.

**O que você leva** — H2: O que você leva da call.
- Mapa do gargalo · Em qual dos 4 canos a sua agência vaza: Atrair, Filtrar, Fechar ou Sustentar.
- O que medir · Os números para acompanhar no cano que vaza. São os que acompanhamos na nossa operação, do lead que entra à venda fechada.
- Próximo passo · Uma ação para aplicar na mesma semana, com ou sem a Full10X.

**Para quem é** — H2: Para quem é a call.
- É para você se: tem agência ou carteira própria de clientes como gestor de tráfego · fatura entre R$10 mil e R$80 mil por mês · quer saber onde agir antes de gastar mais em tráfego ou em curso.
- Ainda não é para você se: ainda não tem nenhum cliente (comece pelo playbook gratuito) · procura fórmula pronta sem mexer na operação · trabalha em uma agência e não decide.

**FAQ (FAQ_02)**
- A call é venda disfarçada? → A call é um diagnóstico da sua agência. No final, se o seu caso pedir acompanhamento, apresentamos a mentoria individual Full10X, com investimento entre R$2.500 e R$5.000. Fica quem quiser. Quem não quiser sai com o gargalo nomeado e a ação do mesmo jeito.
- Quanto custa? → Nada. A call é gratuita e sem compromisso.
- Quem atende? → O time da Full10X, que roda a própria agência com o CRM e o sistema de cobrança que construímos para ela. A conversa parte do que funciona aqui, na tela.
- Preciso ter números em mãos? → Planilha não. Ajuda saber de cabeça quanto a agência fatura, quantos clientes ativos tem e de onde veio o último cliente. O resto levantamos na conversa.
- E se eu não me encaixar? → O próximo passo aparece assim que você envia. Se a call ainda não fizer sentido para o seu momento, indicamos o playbook gratuito para você começar hoje.
- Como eu marco o horário? → Depois de enviar, o time confirma o horário com você pelo WhatsApp em até 24 horas úteis.
- Meu nicho é diferente. Serve? → O diagnóstico olha captação, comercial e operação de agência. Serve para quem vende serviço recorrente, seja qual for o nicho do cliente.

**Fechamento** — H2: Descubra qual cano vaza primeiro. Lead: Três perguntas, 30 minutos de call, sem custo. Você sai com o gargalo nomeado e uma ação para a semana. CTA: Marcar minha call (→ #form). Barra do celular: Marcar minha call.

## Fase 6 · Implementação
- `paginas/p02_form_calendly.py` reescrito com a copy da fase 5. Sem tocar em `name=`, `data-s`, `data-corte` (3), `data-funil` (`form-calendly`), `data-evento` (`Lead`) nem `fid`.
- Seções novas: problema (4 canos, `grid g4`), "Como são os 30 minutos" (`split` + `steps`), "Para quem é" (`compare`, dentro da mesma seção clara de "O que você leva"), fechamento (`cta_panel` com `data-go="#form"`). FAQ local `FAQ_02` (7 perguntas). `PROOF` no hero.
- `done2` sem agenda: "Recebemos." + "O time confirma o horário com você pelo WhatsApp em até 24 horas úteis." A linha "Se preferir, escolha agora um horário na agenda abaixo." (`.cal-only`) e o widget só aparecem quando o Calendly carrega (classe `.cal`). A caixa "Configure CALENDLY_URL" (`.cal-ph`) fica oculta nesta página. Isso vem de um `<style>` mínimo dentro do bloco do formulário (`CAL_CSS`).
- `NOK()` mantido (mesmo destino: playbook), só com o título trocado localmente: "Recebemos sua aplicação." → "Recebemos seu pedido." (aqui ninguém aplicou para nada).
- Botão final "Ver horários" → "Pedir minha call"; título do cartão "Agende sua call" → "Peça sua call"; barra do celular "Agendar minha call" → "Marcar minha call".
- `python3 _gerar.py` → `rc=0`, `12 páginas em .../dist`; `grep -c 'class="todo"' dist/diagnostico/index.html` → `0`.

## Fase 7 · Ajuste visual
- `node qa/screens.mjs 02-v1 diagnostico` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:1565ms`. No print de 1440, a seção "Para quem é" com fundo `mist` deixou o título do cartão branco ("Ainda não é para você se") quase ilegível.
- Correção: "Para quem é" passou para dentro da seção clara de "O que você leva" (o mesmo fundo onde `compare` é usado em p05). `02-v2` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:1420ms`. Recorte de 1440 conferido: cartões alinhados e texto legível.
- `02-v3` (versão final) → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:1541ms`.

## Fase 8 · Engenharia
- Teste de formulário com Playwright (script temporário no scratchpad, 390 px):
  - perfil `dono` + `10-30k` → `{"box":["ok"],"text":"Recebemos. O time confirma o horário com você pelo WhatsApp em até 24 horas úteis. ...","calOnly":"none","calph":"none","final":"Pedir minha call","h":"H1,H2,H2,H2,H2,H2,H2","noAlt":0} errs: 0`
  - perfil `comecando` + `ate-6k` → `{"box":["nok"], ... "Baixar o playbook grátis"}` `errs: 0` (mais tarde, título "Recebemos seu pedido." confirmado no dist: `grep -c` → `1`).
  - Com Calendly simulado (classe `.cal` no container) → `"calOnly":"block"`: a frase da agenda aparece só quando há agenda.
- Hierarquia: 1 H1 e 6 H2; os títulos de cartão e de passo são H3. Nenhuma `<img>` sem `alt`. CTA final e barra do celular → `#form`. O link do NOK → `/playbook/` (0 links quebrados no relatório).
- Varredura do dist por termos proibidos (`transforme|desbloqueie|revolucion|próximo nível|extraordin|Sistema de Demanda|Não estude|+420|+150|R$150|gateway|especialista`): só sobram ocorrências de "calendly" no código e na config, nenhuma em texto visível.

## Fase 9 · Revisão editorial
- Li a página na ordem do visitante: promessa → 4 canos → como é a call (com o aviso honesto da mentoria logo no título da seção) → entregáveis → para quem é → FAQ → fechamento.
- Cortes: "especialista" (vago) virou "time da Full10X"; saiu o benchmark "esperados para o seu tamanho" (sem fonte), e o card passou a citar só "os que acompanhamos na nossa operação"; saiu "churn" (a régua de cobrança está desligada, não há número para sustentar); saiu "Ao vivo, com o plano de ação" (o meio da call não está definido).
- Números na página: só `PROOF` (+R$10 milhões, +2.300) e a faixa R$2.500 a R$5.000 na FAQ, os três permitidos pelo orquestrador; "R$10 mil e R$80 mil" é faixa de público, não resultado.

## Fase 10 · Resumo
- **Estratégia:** página de agendamento para tráfego morno. A promessa forte já existia; o que faltava era razão para marcar e redução de risco: problema nomeado nos 4 canos, roteiro dos 30 minutos, pitch avisado com antecedência, filtro de público e FAQ de quem desconfia de call gratuita.
- **Antes → depois (peças-chave):**
  - Lead: "Uma call com um especialista para mapear captação, comercial e cobrança." → "No anúncio, no filtro, na call ou no boleto. Numa call gratuita com o time da Full10X, olhamos a sua operação pelos 4 canos que rodam na nossa agência…"
  - Passo 2: "Escolha o horário · A agenda abre logo depois." → "Marque o horário · O time confirma com você pelo WhatsApp em até 24 horas úteis."
  - Card: "Números de referência: CPL qualificado, fechamento e churn esperados para o seu tamanho" → "O que medir: os números para acompanhar no cano que vaza. São os que acompanhamos na nossa operação, do lead que entra à venda fechada."
  - Sucesso: "Escolha o melhor horário. Seus dados já estão preenchidos na agenda." + aviso de configuração → "Recebemos. O time confirma o horário com você pelo WhatsApp em até 24 horas úteis." (agenda aparece por baixo quando existir)
  - FAQ: `FAQ_BASE` (curso) → `FAQ_02` (venda disfarçada, custo, quem atende, números em mãos, não me encaixo, horário, nicho).
- **Bloqueios:** nenhum.
- **Pendências para o Julio:**
  1. Confirmar quem do time faz as calls de diagnóstico e por qual meio (Meet, WhatsApp, telefone). A página diz só "o time da Full10X" e "30 minutos com o time".
  2. Confirmar que o time consegue responder em até 24 horas úteis pelo WhatsApp: é a promessa da tela de sucesso enquanto não houver Calendly.
  3. Quem cai no corte vai para `/playbook`, e o PDF ainda não existe (`DOWNLOAD_URL` vazio).
- **Sugestões para arquivos compartilhados:** em `_comum.py`, o título do `NOK()` poderia virar parâmetro (ou "Recebemos suas respostas."), porque "aplicação" não serve para call nem para demonstração; em `_sistema.py`, `calendly()` sem URL poderia deixar o container vazio em vez de mostrar `.cal-ph` ao visitante (aí `CAL_CSS` desta página pode sair); e os ícones `clock`/`file` usados em `TH_IC` (`_comum.py`) não existem no sprite.
- **Status final:** CONCLUÍDA.

### Checklist 19 (marcado só o verificado)
**COPY**
- [x] Headline com resultado e prazo (15 alternativas, escolha justificada)
- [x] Para quem é, explícito (hero + seção "Para quem é")
- [x] Mecanismo nomeado (4 canos: Atrair → Filtrar → Fechar → Sustentar)
- [x] Só números permitidos (PROOF, faixa da mentoria)
- [x] Objeções reais na FAQ (venda disfarçada, custo, quem atende, números, encaixe)
- [x] Pitch avisado com honestidade ("Fica quem quiser")
- [x] CTAs com verbo ("Pedir minha call", "Marcar minha call")
- [x] Sem clichês proibidos (varredura no dist)
- [x] Funciona com e sem Calendly (testado)
**ENGENHARIA**
- [x] `todo:0 placeholders:0 overflow:0 console:0` (02-v3)
- [x] 0 links quebrados; CTAs → `#form`; NOK → playbook
- [x] H1 único, H2 por seção, sem img sem alt
- [x] Contrato do formulário intacto (name, data-s, corte 3, funil, evento)
- [x] Fluxos ok/nok testados no navegador, 0 erros de console
