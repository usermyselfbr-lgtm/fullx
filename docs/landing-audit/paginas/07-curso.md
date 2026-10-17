# 07 · /curso — Aulas gratuitas Full10X (isca)

- **Rota:** `/curso/` · **Fonte:** `paginas/p07_playbook_curso.py` · **Funil:** `playbook-curso` · **Evento:** `CompleteRegistration`
- **Mercado / ICP:** dono de agência e gestor de tráfego com clientes próprios (R$10 mil a R$80 mil/mês), Brasil, que depende de indicação e opera tudo na mão.
- **Objetivo:** cadastro (nome, e-mail, WhatsApp) para receber as 5 aulas curtas quando forem publicadas; ponte para a aula ao vivo de 25/10.

## Decisão (saída escolhida)
**Saída (a): reposicionar.** A página deixa de vender "curso gratuito em 5 aulas com login" (não existe) e passa a ser **"Aulas gratuitas Full10X: o sistema em 5 aulas curtas — cadastre-se para receber a aula 1"**, dizendo com todas as letras que as aulas vão ser gravadas a partir do conteúdo da aula ao vivo de 25/10 e que o cadastro garante o envio por e-mail/WhatsApp quando cada uma sair, **sem data**. Motivo para não bloquear (b): a promessa restante é só "você recebe quando sair", sem prazo, sem login e sem duração; o botão pós-cadastro leva para algo que existe hoje (a aula ao vivo). O risco que sobra (ninguém gravar) está registrado nas pendências.

## Fase 1 · Diagnóstico da página anterior
- **Copy:** H1 "O sistema de uma agência que vende toda semana, em 5 aulas curtas." promete resultado sem prova e vende um produto inexistente. Sub "Assista no seu ritmo" e `done7` "Enviamos o login… Você já pode começar a primeira aula" são falsos (não há área de membros nem aula). Durações inventadas (18/14/22/16/20 min) e stat "90 min no total". Módulo "Escalar: IA no comercial" cita produto que não existe. Nenhuma prova, nenhuma objeção, nenhum "para quem".
- **Conversão:** player vazio com "Configure TRAILER_URL" ocupa a dobra; CTA final "Comece a aula 1 hoje" impossível de cumprir; sem ponte para a escada de valor (aula ao vivo / mentoria).
- **Técnica (baseline):** 0 overflow, 0 console; `data-dl="CURSO_URL"` com `href="#"` vira link morto porque `CURSO_URL` é vazio.

## Fase 2 · Research (FONTE-DA-VERDADE)
**FATOS**
- Não existe curso em 5 aulas, área de membros nem trailer (seção 5; brief: "curso em 5 aulas gravado" não pode ser vendido).
- Aula ao vivo: "Domingo, 25/10, às 14h (Brasília), no Google Meet. O link chega pelo WhatsApp."; "100 lugares"; gratuita; "A gravação, só para quem se inscreveu"; página = fullxmarketing.com (seção 4a).
- 4 canos "Atrair / Filtrar / Fechar / Sustentar, na ordem em que o dinheiro passa" (+ Escalar, brief). "4 funis" (AULA-B).
- CRM próprio (pipeline, formulário que pontua, tarefas de SDR, WhatsApp no CRM) e cobrança própria com régua por WhatsApp: em uso. IA operacional: "o que estamos construindo".
- Números permitidos: "+R$10 milhões em tráfego gerenciado", "+2.300 clientes de serviço gerados", "a primeira agência passou de R$100 mil em 90 dias".
- Frases do Julio: "Seu problema não é conhecimento. É instalação."; "Você vê a tela, não a teoria."; "Para quem já tem cliente e cansou de recomeçar o mês do zero."; "Daqui a 90 dias, sua agência vai depender de quem?"; "Lead chega, mas sem verba. A semana vai embora em call com curioso."
- Mentoria individual, "entre R$2.500 e R$5.000".

**HIPÓTESES**
- As 5 aulas serão cortadas/gravadas a partir do conteúdo da aula de 25/10 (decisão do orquestrador; precisa do compromisso do Julio).
- Envio por e-mail/WhatsApp depende de `WEBHOOK_URL` + automação (hoje o formulário está em modo demonstração).

**AUSENTES**
- Data de publicação das aulas, duração de cada uma, títulos finais, trailer, `CURSO_URL`, depoimentos.

## Fase 3 · Brief RMBC
- **Avatar:** dono de agência R$10–80 mil/mês, já estudou tráfego e funil, o mês ainda fecha na indicação.
- **Consciência:** consciente do problema (tráfego frio/isca).
- **Dor central:** "O mês depende de indicação." / "A semana vai embora em call com curioso."
- **Inimigo:** curso que ensina a peça solta e pula como as peças se ligam.
- **Mecanismo do problema:** a agência trava por falta de sistema; vende, cobra e opera na mão do dono.
- **Mecanismo da solução:** sistema Full10X em 4 canos, na ordem em que o dinheiro passa (Atrair → Filtrar → Fechar → Sustentar) + Escalar.
- **Big idea:** um cano por aula, na ordem em que o dinheiro passa; você descobre onde a sua agência vaza.
- **Promessa defensável:** 5 aulas curtas e gratuitas, uma por etapa; a aula 1 chega no seu e-mail e WhatsApp quando for publicada.
- **Provas:** +R$10 milhões em tráfego gerenciado; +2.300 clientes de serviço gerados; CRM e cobrança próprios rodando na nossa agência.
- **Objeções:** "Quando sai?" → sem data, avisamos no e-mail/WhatsApp; enquanto isso, aula ao vivo 25/10. "É pago/tem pegadinha?" → grátis, sem cartão; mentoria existe para quem quiser, com faixa de preço dita. "Já fiz curso" → aqui é a operação aberta, cano por cano. "Meu nicho é outro" → sistema de captação/comercial/operação de agência. "É igual à aula ao vivo?" → mesmo sistema, separado por etapa; a ao vivo tem perguntas e data.
- **Oferta:** 5 aulas gratuitas por etapa + aviso de publicação. **CTA:** "Quero receber a aula 1".
- **Arquitetura:** (1) Hero: o que é, para quem, estado real (gravação em andamento), formulário 1 passo. (2) Problema: 4 vazamentos nomeados = 4 canos. (3) Ementa: 5 aulas sem duração. (4) Como chega + quem fala (prova e bio publicada). (5) Para quem é / não é. (6) Ponte para a aula ao vivo (existe hoje). (7) FAQ local. (8) CTA final por consequência.

## Fase 4 · 15 headlines
1. O sistema Full10X em 5 aulas curtas, na ordem em que o dinheiro passa.
2. Onde a sua agência vaza: 5 aulas curtas, uma por cano.
3. Seu problema não é conhecimento. São 5 aulas para ver a instalação.
4. Atrair, filtrar, fechar, sustentar e escalar. Uma aula curta para cada.
5. Cadastre-se e receba a aula 1 do sistema Full10X.
6. A agência que vende sem depender de indicação, em 5 aulas curtas.
7. Você já estudou tráfego. Agora veja os canos ligados, em 5 aulas.
8. 5 aulas gratuitas para parar de recomeçar o mês do zero.
9. O que acontece depois que o lead chega, em 5 aulas curtas.
10. Curso ensina a peça. Estas 5 aulas mostram como as peças se ligam.
11. Do anúncio ao boleto pago: o sistema Full10X em 5 aulas.
12. Toda agência vaza em pelo menos um cano. 5 aulas para achar o seu.
13. As 5 etapas que tiram a venda e a cobrança da mão do dono.
14. Aula 1 a caminho: o sistema Full10X, cano por cano.
15. Por que o lead chega sem verba, e as outras 4 perguntas destas aulas.

**Escolhida: 1.** Diz o que é (sistema Full10X), o formato (5 aulas curtas) e o mecanismo com o vocabulário já publicado ("na ordem em que o dinheiro passa"), sem prometer resultado que a página não prova.

## Fase 5 · Copy completa
- **Eyebrow:** Aulas gratuitas Full10X · 5 aulas curtas
- **H1:** O sistema Full10X em 5 aulas curtas, na ordem em que o dinheiro passa.
- **Sub:** Uma aula para cada etapa: Atrair, Filtrar, Fechar, Sustentar e Escalar. As aulas vão ser gravadas a partir do conteúdo da aula ao vivo de 25/10. Cadastre-se e cada uma chega no seu e-mail e WhatsApp assim que for publicada.
- **Formulário:** título "Cadastro gratuito"; legenda "Receba a aula 1 quando ela sair"; botão "Quero receber a aula 1"; conclusão "Cadastro feito. A aula 1 chega no seu e-mail assim que for publicada." + botão "Enquanto isso, garanta sua vaga na aula ao vivo de 25/10" → `https://www.fullxmarketing.com/`.
- **Problema (h2):** "Toda agência vaza em pelo menos um cano." 4 cards: O mês depende de indicação / Lead chega sem verba / Só você vende / O boleto atrasa. Fecho: "Seu problema não é conhecimento. É instalação."
- **Ementa (h2):** "As 5 aulas." + lead "Um cano por aula, na ordem em que o dinheiro passa." Itens: Atrair (anúncio para a própria agência e os 4 funis de captação), Filtrar (formulário que pontua e nota de corte), Fechar (roteiro de call e CRM com tarefas de SDR e WhatsApp), Sustentar (régua de cobrança por WhatsApp e o 3º mês), Escalar (IA na operação, o que estamos construindo).
- **Como chega + quem fala:** passos "Você se cadastra / A aula 1 é publicada / As outras 4 seguem na ordem"; bio publicada do Julio; linha de prova PROOF.
- **Para quem:** É para você se tem agência ou carteira de clientes própria, já anuncia e o mês ainda fecha na indicação, quer ver como as etapas se ligam. Não é para você se ainda não tem cliente, procura fórmula sem implementar, quer só aula de configuração de anúncio.
- **Ponte aula ao vivo:** "Não quer esperar? A aula ao vivo é domingo, 25/10." Domingo, 25/10, às 14h (Brasília), no Google Meet. 100 lugares. Gratuita, com perguntas no final. Botão "Garantir minha vaga na aula ao vivo".
- **FAQ (local `FAQ_07`):** Quando sai a aula 1? / Quanto custa? / É a mesma coisa da aula ao vivo? / Serve para o meu nicho? / Vão tentar me vender alguma coisa?
- **CTA final:** "Daqui a 90 dias, sua agência vai depender de quem?" / "Cadastre-se agora e a aula 1 chega no seu e-mail e WhatsApp assim que sair." / botão "Quero receber a aula 1".

## Fase 6 · Implementação
- `paginas/p07_playbook_curso.py` reescrito: hero reposicionado; formulário 1 passo mantido (`playbook-curso`, `CompleteRegistration`, campos `nome/email/whatsapp`, `fid=form` inalterados); `done7` = "Cadastro feito. A aula 1 chega no seu e-mail assim que for publicada." + link direto (sem `data-dl`) para `https://www.fullxmarketing.com/`; `mods` sem durações; `stats` "90 min no total" removida; novas seções: vazamentos (4 cards), quem dá as aulas (bio publicada + `PROOF`), para quem (compare), ponte para a aula ao vivo, FAQ local `FAQ_07`, CTA final.
- `CURSO_URL` removido do CONFIG (o botão `data-dl` saiu; se a chave fosse configurada, sobrescreveria o link da aula ao vivo). `TRAILER_URL` mantido vazio: o sistema esconde o player; a dobra funciona sem ele (H1 + sub + formulário).
- `python3 _gerar.py` → `12 páginas em .../dist` (rc=0); `grep -c 'class="todo"' dist/curso/index.html` → `0`.

## Fase 7 · Ajuste visual
- `07-v1`: compare ("Não é para você se") em seção escura ficou com texto de baixo contraste; frase "Seu problema não é conhecimento. É instalação." desalinhada à esquerda. Corrigido: seções reordenadas (escuro/claro alternando: hero → vazamentos claro → aulas escuro → para quem claro → quem dá as aulas escuro → aula ao vivo claro → FAQ → CTA) e frase centralizada.
- `07-v2` / `07-v3`: 390 e 1440 conferidos (cards iguais, sem texto cortado, botões com folga). Observação: com o sistema atual o placeholder do player ("Vídeo de vendas. Configure TRAILER_URL") ainda aparece no build local; a ocultação com URL vazia é tarefa do sistema compartilhado.

## Fase 8 · Engenharia
- 1 `h1`; `h2` por seção; `h3` em cards, aulas e compare. Links externos: só `https://www.fullxmarketing.com/` (com `target=_blank rel=noopener`); interno `/institucional/` (logo). Canônico `https://www.fullxmarketing.com/curso/`; title "Full10X · Aulas gratuitas: o sistema em 5 aulas curtas".
- CTAs `#form` com `data-go` (barra do celular e painel final). Busca no `dist/curso/index.html` por "90 min", "18 min", "login", "CURSO_URL", "IA comercial", "toda semana": 0 ocorrências.

## Fase 9 · Revisão editorial
- Leitura na ordem do visitante; trocado "Cada aula abre uma delas" (eram 4 dores para 5 aulas) por "As 4 primeiras aulas abrem um cano cada". Sem clichês da lista, sem "não é X, é Y" além da frase publicada do Julio, sem número fora dos permitidos (+R$10 milhões, +2.300, R$2.500–5.000, 25/10 14h, 100 lugares).

## Fase 10 · Resumo
- **Estratégia:** isca honesta em consciência de problema: vende a ementa (4 canos + Escalar) e o aviso de publicação; usa a aula ao vivo (existe hoje) como próximo degrau imediato.
- **Antes → depois:** H1 "O sistema de uma agência que vende toda semana, em 5 aulas curtas." → "O sistema Full10X em 5 aulas curtas, na ordem em que o dinheiro passa." · Conclusão "Acesso liberado. Enviamos o login…" → "Cadastro feito. A aula 1 chega no seu e-mail assim que for publicada." · Botão "Liberar meu acesso" → "Quero receber a aula 1" · CTA final "Comece a aula 1 hoje." → "Daqui a 90 dias, sua agência vai depender de quem?" · Escalar "IA no comercial e na operação · 20 min" → "IA na operação: … que estamos construindo".
- **Testes (saída real):** `python3 _gerar.py` → `12 páginas em /Users/juliomyself/projetos/fullx-funis/dist` rc=0 · `node qa/screens.mjs 07-v3 curso` → `curso overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:1450ms` rc=0.

## Bloqueios
Nenhum para publicar a página. O envio real das aulas depende de `WEBHOOK_URL` + automação (pendência comum).

## Pendências para o Julio
1. Confirmar que as 5 aulas vão ser gravadas a partir do conteúdo da aula de 25/10 (a página afirma isso como plano, sem data). Se não for acontecer, trocar a página para a saída (b).
2. Definir como o cadastro recebe a aula (lista de e-mail e/ou disparo no WhatsApp) e ligar o webhook deste funil.
3. Conflito de oferta: a home diz "A gravação, só para quem se inscreveu". Se as 5 aulas forem cortes da gravação, isso tira a exclusividade da aula ao vivo; manter as aulas como regravação curta ou mudar a frase da home.
4. Depois de 25/10, a ponte "Não quer esperar? A aula ao vivo é domingo, 25/10" e o botão da conclusão ficam vencidos: trocar pela próxima data ou pela página da mentoria.
5. Trailer (`TRAILER_URL`) opcional quando houver vídeo.

## Sugestões para arquivos compartilhados
- `_comum.py` `VSL`: quando a chave estiver vazia, não renderizar o texto "Configure X no topo do arquivo" no ar (ou esconder `.vsl-wrap`).

## Status final: CONCLUÍDA

## Checklist (seção 19) — só o verificado
**COPY**
- [x] Headline diz o que é, para quem serve o formato e o mecanismo, sem promessa sem prova
- [x] Nenhum número fora dos permitidos; nenhum produto inexistente vendido como disponível
- [x] Objeções reais na FAQ (quando sai, custo, diferença da aula ao vivo, nicho, venda)
- [x] CTAs com verbo e consequência; conclusão do formulário verdadeira
- [x] Zero clichê da lista do brief
**ENGENHARIA**
- [x] `todo:0 placeholders:0 overflow:0 console:0 links-quebrados:0` (07-v3)
- [x] 1 h1, hierarquia h2>h3
- [x] Contrato do formulário preservado (`name`, `data-funil`, `data-evento`, `fid`)
- [x] Prints 390 e 1440 conferidos
