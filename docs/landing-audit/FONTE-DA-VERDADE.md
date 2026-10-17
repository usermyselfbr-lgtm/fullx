# Fonte da verdade — Full10X / FULLX (levantamento de 17/10/2026)

Documento para copywriters reescreverem as 12 landing pages de `~/projetos/fullx-funis/paginas/*.py` sem inventar nada. Só entra aqui o que tem fonte (arquivo:linha ou trecho literal). Onde duas fontes conflitam, as duas aparecem. Tudo que nenhuma fonte preenche está na seção 9.

Legenda da coluna "pode usar": **sim** = já está publicado pelo Julio ou vem de dado operacional; **com ressalva** = publicado, mas conflita com outra fonte ou é número redondo sem base verificável; **não** = só existe em documento interno/hipótese.

Caminhos usados (abreviações): `AULA-A` = `~/projetos/fullx-aula/index.html` (home de fullxmarketing.com, variante A); `AULA-B` = `~/projetos/fullx-aula/100k/index.html` (fullxmarketing.com/100k, variante B); `RMBC` = `~/Downloads/FULLX/RMBC FULLX — Pesquisa Condensada.pdf` (13/10/2026, texto extraído com pdftotext); `ANUNCIOS` = `~/Downloads/FULLX/FULLX-anuncios/textos-dos-anuncios.md`; `MEM/<nome>` = `~/.claude/projects/-Users-juliomyself/memory/<nome>.md`.

## 1. Marca e quem fala

| Item | Fato | Fonte |
|---|---|---|
| Nome da marca nas páginas publicadas | **FULLX** (grafia em caixa alta; o rodapé diz "FULLX. Educação e sistemas para donos de agência. Resultados variam de acordo com a aplicação.") | AULA-A texto visível, rodapé; AULA-A:512 `aria-label="Full10X"` no logo |
| Nome da marca nos modelos de funil | **Full10X** (ex.: "Plataforma Full10X", "Por que a Full10X?", "mentoria Full10X") | `paginas/p01_institucional.py:33,48`; `_comum.py:58` |
| Origem da marca | "FULLX (antes Eikon Insider) é a mentoria de implementação do Julio para gestores de tráfego e donos de agência pequena" | RMBC p.1 (linha 11 do texto extraído) |
| Quem fala | "Julio, founder da FULLX" | AULA-A:551; AULA-B (texto visível "Julio, founder da FULLX") |
| Nome completo | "Julio Henrique" (capa do material de estudo) | `~/Downloads/FULLX/fullx-aulao-meta-ads-2026.pdf` p.1: "Julio Henrique · Material de estudo FULLX" |
| Bio publicada (literal) | "Sou o Julio, founder da FULLX. Opero agência com tráfego, comercial e cobrança próprios. O CRM, o formulário que pontua o lead e o sistema de cobrança que você vai ver foram construídos para a minha operação. Você vê a tela, não a teoria." | AULA-A:653 e texto visível |
| Bio variante B (literal) | "Sou o Julio, founder da FULLX. Opero agência com tráfego, comercial e cobrança próprios. Tudo o que você vai ver foi construído para a minha operação. Eu mostro o que roda, não o que li." | AULA-B texto visível |
| Idade | "Julio tem 22 anos" aparece como OBJEÇÃO a responder (não como dado de página) | RMBC linha 351 e 829 |
| Empresa operacional (a "agência própria") | **Eikon** — "A Eikon é uma agência que só atende tatuadores, no Brasil e na Europa." Rosto comercial da Eikon = João Flávio (sócio); "Julio aparece como fundador/estrategista só se quiser" | `~/projetos/kortix-agentes/skills/*` (grep "A Eikon é uma ag"); MEM/eikon-analise-escala-anuncios ("João Flavio (sócio)") |
| Nome da agência no RMBC | "a Inout, agência de tatuagem do Julio desde 2017" | RMBC linha 14 |
| Time da operação | Alexandre = SDR, Paulo Neto = closer (único), João Flávio = gestor | MEM/crm-eikon-marketing-campanhas ("Julio definiu: Alexandre = SDR, Paulo Neto = CLOSER (único), João Flávio = GESTOR") |
| Cidade | **informação ausente** (nenhuma fonte local cita cidade/sede) | — |
| Foto do Julio | única foto usada: link externo postimg (avatar e og:image), `alt="Julio, founder da FULLX"` | AULA-A:55,550,650; AULA-B:52 |
| Instagram | link genérico `https://instagram.com/` (sem handle) nas duas páginas | AULA-A:804; AULA-B:916 |
| Logos | `~/Downloads/FULLX/16:10:2026/LOGO E POST/full10x-horizontal-*.png`, `full10x-simbolo-*.png`; `~/Downloads/FULLX/FULLX-logo-perfil/fullx-logo.svg`, `fullx-simbolo.svg` | listagem das pastas |

Conflito a registrar: as páginas publicadas chamam a marca de FULLX e os modelos de funil de Full10X; os PNGs de logo usam "full10x" no nome e o SVG "fullx". Não há decisão escrita sobre a grafia oficial.

## 2. Números e provas verificadas

### 2a. Números de autoridade (quatro versões em circulação — registrar todas)

| Afirmação | Fonte | Pode usar nas páginas? |
|---|---|---|
| "+2.300 clientes de serviço gerados" | AULA-A título e texto visível; AULA-B idem (publicados em fullxmarketing.com em 16/10/2026, MEM/fullx-aula-landing) | **com ressalva**: é o número que o Julio publicou por último, mas conflita com +420 (anúncios/home anterior), +150 (RMBC) e 152 clientes no CRM |
| "+R$10 milhões em tráfego Ads" / "+R$10MM em tráfego gerenciado" | AULA-A e AULA-B; `_comum.py:50` (PROOF); RMBC linha 15 ("+R$10 milhões gerenciados em tráfego"); aulão PDF p.1 ("+R$ 10 mi gerenciados em tráfego") | **sim** — único número presente em todas as fontes |
| "+R$10 milhões em receita gerada" | AULA-A e AULA-B texto visível | **com ressalva**: só aparece nas landings de 16/10; não consta no RMBC nem nos anúncios |
| "A primeira agência passou de R$100 mil em 90 dias" / linha do tempo "2024 — Primeira agência aberta → 90 dias depois — R$100 mil de faturamento" | AULA-A e AULA-B; ANUNCIOS anúncio 02 ("Criei minha primeira agência em 2024 e faturei +R$100 mil em 90 dias") | **com ressalva**: conflita com RMBC ("Inout, agência de tatuagem do Julio desde 2017") |
| "+420 clientes" | ANUNCIOS anúncios 01 e 02 (14/10); home anterior de fullxmarketing.com (título "4 funis… +420 clientes", MEM/fullx-aula-landing) | **não** — substituído por 2.300 em 16/10 |
| "Inout desde 2017, +150 clientes, +30 países, R$150 mil/mês, +R$10 milhões em tráfego, +R$1 milhão em direct response" | RMBC linhas 14–15 e 756 ("Credibilidade e provas (FATO)"); aulão PDF p.1 ("2017 operando desde · +150 clientes · +30 países") | **com ressalva**: é a versão "oficial" do RMBC de 13/10, mas as páginas de 16/10 não a usam; MEM/eikon-insider-growth avisa: "150 ativos × ticket R$1.5–2k não bate com R$150k/mês — pendente de confirmação no CRM" |
| 152 clientes no CRM, ticket R$ 1,8 mil, 0 recompra registrada | MEM/eikon-analise-escala-anuncios (leitura do Neon de produção em 14/10/2026) | **não publicar como está** — é dado interno, mas é o único número de clientes verificado em sistema |
| Receita 2026 da Eikon por mês (CRM): jan–jun média R$ 25,7 mil; jul R$ 54 mil; ago R$ 43 mil; set R$ 39,6 mil; out (até 14) R$ 15,6 mil | MEM/eikon-analise-escala-anuncios | **não** — interno; mostra que "R$150 mil/mês" não é o faturamento atual do CRM |
| "A gente analisou os formulários de mais de 4 mil tatuadores" | kortix-agentes (marcado "[CONFIRMAR se pode citar]") | **não** até o Julio confirmar |
| "[XXX] agências atendidas · +R$10MM em tráfego gerenciado · [X anos] de operação" | `paginas/p01_institucional.py:27` | placeholder — ver seção 9 |
| "[+XXX clientes atendidos]" | `_comum.py:50` | placeholder — ver seção 9 |

### 2b. Provas visuais publicadas (pasta `prova/`, 9 cartões, legendas literais da página)

| Arquivo | Legenda na página | aria-label (descrição do print) | Fonte |
|---|---|---|---|
| `img-1-57-mi.jpg` | "R$ 1,57 milhão investidos em Meta Ads" | — | AULA-A texto visível |
| `img-placas.jpg` | "R$ 1 milhão em saques + placa de R$ 100 mil na Kiwify" | — | idem |
| `img-20-mil-dia.jpg` | "R$ 20 mil por dia em anúncios rodando" | — | idem |
| `v6-kiwify-425k.mp4` | "R$ 425 mil a caminho do R$ 1 milhão na Kiwify" | "Painel da Kiwify com R$ 425 mil de R$ 1 milhão" | AULA-A:684 |
| `v5-vsl-154k.mp4` | "154.736 views em uma única VSL" | "Analytics da VSL com 154.736 visualizações" | AULA-A:685 |
| `v9-344-mil.mp4` | "R$ 344 mil de verba em uma só conta" | "Gerenciador de anúncios com R$ 344.835,35 de total usado" | AULA-A:686 |
| `v1-172-anuncios.mp4` | "172 anúncios publicados de uma vez" | "Meta Ads publicando 4 campanhas, 84 conjuntos e 84 anúncios" (conflito 172 × 84) | AULA-A:687 |
| `v2-verba-compras.mp4` | "Verba, compras e plays na mesma conta, ao vivo" | "Gerenciador de anúncios com R$ 1,57 milhão usado, compras e plays" | AULA-A:688 |
| `v8-placas.mp4` | "500 mil e 1 milhão em saques, nas placas" | "Placas de 500 mil e 1 milhão em saques" | AULA-A:689 |

Observações: (1) os clipes foram "recortados dos vídeos/fotos de resultado do Julio com ffmpeg" (MEM/fullx-aula-landing-b); (2) os selos "✓ Print real / ✓ Vídeo real" foram removidos em 16/10 a pedido do Julio "pareciam fake" (MEM/fullx-aula-landing); (3) as placas e o painel Kiwify são de infoproduto, não da agência — nenhuma fonte diz qual produto gerou esses saques; (4) a legenda "172 anúncios" não bate com o aria-label "84 anúncios" do mesmo vídeo.

### 2c. Números de mercado utilizáveis (RMBC marca como FATO, com fonte externa)
- "65% das agências têm até 10 funcionários, 79% atendem no máximo 10 clientes, 67% cobram menos de R$5 mil/mês por cliente. 78,3% das agências brasileiras são microempresas. Só 47% das agências usam CRM." (RMBC linha 89–92, RD Station 2025/2026)
- "44% das agências fecham até 5 clientes recorrentes por ano e 14% não fecharam nenhum"; churn: "cliente não percebe valor (16%)", "expectativas desalinhadas (12%)"; indicação é o principal canal (28%) (RMBC Pesquisa FullX.pdf, TL;DR)
- "Preço é 8% do critério de escolha; atendimento 28%" (RMBC linha 192 e 412)

## 3. Produtos e softwares

### 3a. O que as páginas prometem (modelos de funil)
`_comum.py:64–67` define os 4 "softwares" exibidos no bento: **CRM** ("Pipeline comercial de agência, com etapas, tarefas e histórico de cada lead" — Funil visual por etapa / Formulário que pontua o lead / Tarefas e follow-up do SDR), **Gateway de pagamento** ("Cobrança recorrente com régua automática para o boleto não atrasar" — Pix, boleto e cartão recorrente / Régua de cobrança por WhatsApp / Painel de inadimplência), **IA operacional** ("Treina e orienta o time de entrega com os processos da sua agência" — Responde dúvidas do time 24h / Base de processos e checklists / Onboarding de novo colaborador), **IA comercial** ("Qualifica, responde e agenda leads no WhatsApp enquanto o time dorme" — Primeiro contato em segundos / Qualificação por perguntas / Agendamento direto na agenda). `p01_institucional.py:33`: "Quatro softwares. Uma operação. Use um só ou os quatro integrados. Também disponíveis com a sua marca, em white label."

### 3b. O que existe de fato (verificado em código/memória de projeto)

| Produto | Estado real | O que faz hoje | Fonte |
|---|---|---|---|
| **CRM** ("Eikon CRM & Formulário", ex-"Órbita") | **Existe e roda em produção** (eikonappinterno.online, Vercel + Neon) | Pipeline/kanban, formulários multi-etapa com pontuação e filtro MQL/SQL (PR #4, 30/09), aba Marketing › Campanhas com coleta horária do Meta Ads, CAPI, origem da venda (PRs #14–#24), WhatsApp dentro do CRM via Evolution API — inbox, kanban, resposta com texto/foto/áudio, cadência (PRs #9–#13), cargos SDR/Closer/Gestor (PRs #26/#28). Instagram Direct no PR #23 aguardando merge. 1 org, 10 usuários em 16/10. | MEM/crm-eikon-servidores; MEM/crm-eikon-filtro-mql-resultados; MEM/crm-eikon-marketing-campanhas; MEM/crm-eikon-whatsapp-inbox; MEM/crm-eikon-dados-producao |
| **Gateway de pagamento / cobrança** ("Eikon Cobranças", Sistema de Pagamento) | **Existe, em produção no Railway** (eikonfinanceirointerno.online), Node vanilla + SQLite | Régua de cobrança com disparos por WhatsApp via n8n (fluxos 1–5), dívida D+30, integração/divergência com Asaas; **a régua está pronta e parada**: "0 de 133 parceiros têm disparo ativo, com 0 pagamentos lançados" (02/10); "nenhuma melhoria pode ligar o disparo… quem liga é o FINANCEIRO" | MEM/eikon-cobrancas-processo; MEM/localizacao-sistemas-eikon |
| **Gateway próprio (Pix/boleto/cartão)** | **Não é gateway próprio**: a cobrança usa Asaas por baixo ("régua de cobrança via Asaas", RMBC linha 13; "multa/juros Asaas, divergência com Asaas" em MEM/eikon-cobrancas-processo) | — | idem |
| **IA operacional** ("IA que treina o time") | **Existe como protótipo**: Open WebUI no Railway com 11 "mentores" + 84 skills/132 .md importados em 12/10; cérebro em `~/projetos/kortix-agentes` (11 mentores, biblioteca destilada). Conta Kortix sem modelo ligado; Open WebUI usa Anthropic. Não há registro de uso pelo time da Eikon. | MEM/eikon-mentores-openwebui; MEM/kortix-agentes |
| **IA comercial** (qualifica/responde/agenda no WhatsApp sozinha) | **Não encontrado em nenhuma fonte.** O que existe é: formulário que pontua (CRM), fluxo n8n que manda lead novo para o grupo Comercial no WhatsApp (MEM/sdr-leads-whatsapp), cadência manual no CRM. | — |
| **White label** (software com a marca do aluno) | **Só plano/oferta**: RMBC propõe "Licença do software com a marca do aluno após os 90 dias, R$197–497/mês" como HIPÓTESE (linha 727); CRM tem isolamento multi-tenant testado (MEM/crm-eikon-ci-e-multitenant: "teste de orgId") mas 1 org em produção. Não há cliente white label. | RMBC; MEM/crm-eikon-ci-e-multitenant |
| **"Builder Forms"** | Nome usado no RMBC para o formulário com pontuação do CRM ("Builder Forms multi-etapas com pontuação, UTMs e métrica de abandono", RMBC linha 596); nas landings aparece só como "o formulário que pontua o lead" | RMBC; AULA-A |
| Outros sistemas internos citados em memória (não são produto) | Eikon Links (encurtador), Eikon AdSpy, Eikon Leads/Firecrawl, OS Time, Spy Myself | MEM/* |

Resumo para o copy: pode-se afirmar que CRM e cobrança são **sistemas próprios, construídos para a operação da Eikon e rodando** (as páginas já dizem isso: "Sistemas próprios de CRM e cobrança", `_comum.py:50`). Não se pode afirmar: gateway próprio de pagamento, IA comercial funcionando, white label disponível, "painel de inadimplência" em uso (a régua está desligada por decisão do financeiro).

## 4. Mentoria / aula

### 4a. Aula ao vivo (publicada em fullxmarketing.com e /100k)
| Item | Fato | Fonte |
|---|---|---|
| Data/hora | "Domingo, 25/10, às 14h (Brasília), no Google Meet. O link chega pelo WhatsApp." / `data-alvo="2026-10-25T14:00:00-03:00"` | AULA-A texto; AULA-B:614 |
| Duração prevista | Evento de agenda: 17:00Z–18:30Z (= 14h–15h30 Brasília) | AULA-A:910 (link calendar.google.com) |
| Público declarado | "Para gestores de tráfego a partir de R$6 mil/mês e donos de agência de R$10 mil a R$30 mil/mês" | AULA-A hero |
| Promessa A (variante A, ângulo mecanismo) | "Você já estudou tráfego, funil e venda. Agora veja o sistema rodando." / "Eu abro, na tela, a operação que já gerou +2.300 clientes de serviço: o anúncio, o formulário que pontua o lead, o CRM, o roteiro de venda e a cobrança." | AULA-A |
| Promessa B (variante B, ângulo resultado) | "Feche cliente todo mês sem depender de indicação. Na aula ao vivo eu mostro os 4 funis que levaram minha primeira agência a R$100 mil em 90 dias" | AULA-B |
| Estrutura do conteúdo | 4 "canos": Atrair / Filtrar / Fechar / Sustentar, "na ordem em que o dinheiro passa" | AULA-A e AULA-B |
| Formato de inscrição | formulário de 7 perguntas em `<dialog>`; nota de corte 8 (`NOTA_CORTE:8`); pontuação exibida na "ficha do lead" | AULA-A:932; AULA-A texto "corte em 8" |
| Pontuação das respostas | Perfil: dono/sócio +3, gestor com clientes +2; Faturamento: 10–30k +4, 30–80k +3, 6–10k +2, 80k+ +2; Formação: curso online +1; Momento: investir agora +4, até 60 dias +2 | `_comum.py:24–27` (mesma tabela das landings) |
| Vagas | "100 lugares. É o limite da sala do Google Meet. Quando lotar, a inscrição fecha." | AULA-A |
| O que recebe | "A aula ao vivo no Google Meet, com perguntas no final. A gravação, só para quem se inscreveu. O grupo da aula no WhatsApp, com link e lembrete. Suas respostas lidas antes, para eu cobrir o seu gargalo ao vivo." | AULA-A |
| Pitch no final | "No final eu apresento a mentoria FULLX. Fica quem quiser." / "Sem cartão e sem plataforma." | AULA-A e AULA-B |
| Preço âncora | "O conteúdo da mentoria, em uma aula aberta. Mentoria individual FULLX: a partir de R$2.500 → R$0" | AULA-A; AULA-B ("R$0 / R$2.500") |
| Faixa de investimento dita no formulário | "O investimento da mentoria fica entre R$2.500 e R$5.000. Responda com sinceridade: isso não muda sua vaga na aula." | AULA-A, pergunta 7 |

### 4b. Mentoria FULLX (o produto vendido depois da aula)
| Item | Fato | Fonte |
|---|---|---|
| Formato publicado | "Mentoria individual FULLX" | AULA-A |
| Formato nos modelos de funil | "Cada turma tem [XX] vagas porque as calls são em grupo pequeno" (conflita com "individual") | `p05_aplicacao.py:21` |
| Preço | Publicado: "a partir de R$2.500"; faixa "R$2.500 e R$5.000". Histórico (RMBC, FATO): "mentoria de 30 dias a R$2.000, depois R$2.500–5.000". Recomendação RMBC (HIPÓTESE): "R$4.997–7.997 por 90 dias" + licença R$197–497/mês. RMBC lista 4 versões de preço em documentos e pede decisão. | AULA-A; RMBC linhas 709–745, 1140 |
| Duração | "90 dias" nos modelos ("Está pronto para implantar em 90 dias", `p05_aplicacao.py:32`); RMBC recomenda "instalados em 30 dias" + 90 dias de programa. Nenhuma duração publicada nas landings da aula. | p05; RMBC |
| Entrega (RMBC, "Entregáveis — master list (FATO)") | "4 sistemas (CRM, Builder Forms com pontuação, régua de cobrança via Asaas e IA que treina o time) mais o Sistema de Demanda Qualificada" | RMBC linhas 11–14, 667 |
| Público da aplicação | "Tem agência entre R$10 mil e R$80 mil por mês. Quer previsibilidade de venda. Está pronto para implantar em 90 dias." / Não é para: "Ainda não tem nenhum cliente. Procura fórmula sem implementar. Não tem como investir nos próximos 60 dias." | `p05_aplicacao.py:31–32` |
| Prazo de resposta da aplicação | "Respondemos todas as aplicações em até 48 horas úteis." | `p05_aplicacao.py:17` |
| Garantia | **Nenhuma garantia publicada.** RMBC recomenda garantia de instalação ("Se em 30 dias os 4 sistemas não estiverem rodando na sua agência, trabalhamos de graça até estarem…") + 7 dias CDC — HIPÓTESE, não decidida. | RMBC linha 745–754 |
| Cases de mentorados | RMBC cita "Um mentorado evitou 3 churns e fechou 4 clientes na primeira semana" e nomes "Eluan e Brayan" como cases a documentar ("Sem 3 cases documentados, usar linguagem de processo"). Nenhum case com nome/print publicado. | RMBC linhas 757, 763, 1163 |
| Mecanismo oficial | UMP "funil sem encanamento"; UMS "Sistema de Demanda Qualificada, instalado, não ensinado"; assinatura "Não estude. Instale." (RMBC avisa que está perto do slogan da Agência de Valor) | RMBC linha 565–569, 642–649 |

## 5. Conteúdos gratuitos existentes

| Conteúdo prometido nas páginas | Existe? | Fonte |
|---|---|---|
| "Playbook: formulário que qualifica lead antes da call — PDF · 18 páginas" (`_comum.py:70`), "PLAYBOOK FULL10X [TÍTULO DO EBOOK] [XX] páginas · PDF" (`p06`) | **Não há PDF pronto desse título.** O que existe: `~/Downloads/FULLX/Playbook-Full10X.pdf` + `Playbook-Full10X-editavel.pptx` (pdftotext retorna 0 linhas = PDF só imagem; conteúdo não verificado) e a página `~/Downloads/FULLX/playbook.html` com título "Playbook 0 a 100K — os 4 canos da agência de R$150 mil/mês \| FULLX" | listagem `~/Downloads/FULLX`; grep `<title>` |
| "Régua de cobrança para agência: modelo pronto — PDF · 12 páginas" (`_comum.py:74`) | Não encontrado | — |
| "Cadastro para curso gratuito em 5 aulas" (`p00_modelos.py:12`, `p07`) | Não encontrado nenhum curso em 5 aulas. Existe material de estudo pago/interno: `fullx-curso-meta-ads-2026.pdf` e `fullx-aulao-meta-ads-2026.pdf` ("Meta Ads 2026: do sistema à escala", 10 módulos, 8 aulas de referência) | listagem; aulão PDF p.1 |
| "Aula gratuita: Os 4 funis que enchem a agenda comercial de uma agência — 42 min" (`_comum.py:70`) | É a aula ao vivo de 25/10; ainda não aconteceu, não há gravação | AULA-A |
| "Aula gratuita: Roteiro de call: como outra pessoa fecha no seu lugar — 35 min" | Não encontrado | — |
| Artigos "Por que sua agência perde cliente no terceiro mês", "CPL baixo não paga boleto" | Não encontrados (só títulos nos modelos) | `_comum.py:72,75` |
| "Aulas, playbooks e artigos publicados toda semana" (`p01_institucional.py:40`) | Não há blog publicado; `01b-blog` e `01c-blog-artigo` são modelos com `[AUTOR]`, `[DD/MM/AAAA]` | p01b, p01c |
| Carrosséis prontos (Instagram) | PNGs em `~/Downloads/FULLX/16:10:2026/LOGO E POST/carrosseis-full10x*` : 01-quem-somos, 02-estudo-payback, 03-estudo-funil, 04-estudo-03-funis, 05-estudo-04-matematica-10x, 06-estudo-05-ltv-cac, 07-estudo-06-engenharia-reversa, 08-estudo-07-oferta-isca, 09-estudo-08-angulos-hooks, 10-estudo-09-retencao, 11-estudo-10-pre-vendas-closer (só imagens, texto não lido) | listagem |
| Anúncios prontos | 3 estáticos (feed + stories) em `~/Downloads/FULLX/FULLX-anuncios/` com textos em `textos-dos-anuncios.md` (ainda com "+420 clientes" e "8 vagas restantes") | ANUNCIOS |
| Páginas HTML soltas já escritas (não publicadas) | `~/Downloads/FULLX/`: `vsl.html` ("Não estude. Instale. \| Os 4 sistemas que rodam uma agência de R$150 mil/mês"), `aplicacao.html` ("Aplicação para o Raio-X da sua agência"), `diagnostico.html` ("Diagnóstico do Encanamento da sua agência"), `aula.html` ("Aula ao vivo: o encanamento da agência de R$150 mil/mês"), pasta `PÁGINAS WEB/` (fullxcurta, fullxplaybook) | grep `<title>` |
| Templates herdados do Eikon Insider (PDF) | `~/Downloads/FULLX/PDF AULAS INSIDER/`: Template SDR, Closer, Sales Ops, Social Selling, Checklist de Pesquisa, Aula 01 Aquisição Qualificada, Caderno de Implementação, Outline de VSL, Playbook Estruturação Comercial, "Insider Criar Oferta" | listagem |
| Material do operacional Eikon (transcrições de 16 aulas + PDF de 40 slides) | Pasta `~/Downloads/OPERACIONAL EIKON ATUAL` **não existe mais**; cópia no Google Drive (`…/TUDO MAC/CINZA/EIKON/OPERACIONAL EIKON ATUAL`) só tem a pasta `BREIF GERAL` e `_TRANSCRICOES` vazia (arquivos não baixados). **Fonte indisponível nesta máquina.** | mdfind/ls |

Links de download/curso configurados nas páginas: `DOWNLOAD_URL`, `CURSO_URL`, `VIDEO_URL`, `CALENDLY_URL` **vazios** em todos os modelos (`LEIA-ME.md`, `_sistema.py:1079–1082`).

## 6. Integrações e configurações reais

| Item | Valor | Fonte |
|---|---|---|
| Domínio no ar | `fullxmarketing.com` (+www) ligado ao projeto Vercel `fullx-aula` (team `sistemacrmbuilderforms`, projectId `prj_D4hiUMFFHyklZZvZuSKNFP4TtHye`); home = variante A, `/100k` = variante B; também responde em `fullx-aula.vercel.app` | MEM/fullx-aula-landing; `.vercel/project.json` |
| Domínio nos canônicos das landings | `https://fullx.com.br/aula` e `https://fullx.com.br/aula-b` (og:url e canonical) — **não há evidência de que fullx.com.br esteja configurado**; conflita com o domínio real | AULA-A:56,60; AULA-B:53,57 |
| Domínio nos modelos de funil | `_gerar.py:12 DOMINIO = 'https://www.fullxmarketing.com'`; substitui `grupofull10x.com` dos textos; mock de URL `app.grupofull10x.com/pipeline` (`_sistema.py:776`) | _gerar.py; _sistema.py |
| Slugs previstos | /institucional, /conteudos, /conteudos/4-funis-agenda-comercial, /diagnostico, /assista, /mentoria, /aplicacao, /playbook, /curso, /espera, /white-label, /modelos | `_gerar.py:13–17` |
| Pixel da Meta | `1127997753074983` (landings A e B e todos os modelos) | AULA-A:44; AULA-B:41; `_sistema.py:1079`; LEIA-ME |
| Eventos do pixel | PageView, AbriuFormulario, InicioCadastro, EtapaFormulario, Lead / SubmitApplication / CompleteRegistration, LeadQualificado, Schedule, CliqueCTA; também `dataLayer` (GTM id vazio: `gtm.js?id=`) | LEIA-ME; AULA-A:34 |
| Webhook de leads da aula | Apps Script `https://script.google.com/macros/s/AKfycbwVAbcJL5BcocQ5-FYh7yqGZz22purH7bnaBhqhEWzSq9PZoW0TxZaLPlmfJjFsOgCG/exec` (script do Julio, responde `{"status":"success","message":"Lead registrado com sucesso!"}`; não é o `apps-script/Code.gs` da pasta) | AULA-A:929; AULA-B:1052; MEM/fullx-aula-landing; `README-planilha.md` |
| Grupo do WhatsApp da aula | `https://chat.whatsapp.com/LDHW591lcXr0JPnz6tbHxC?mode=gi_t` | AULA-A:931 |
| WhatsApp do time | **placeholder** `5500000000000` nas landings A/B e nos modelos ("TROQUE pelo número real") | AULA-A:930; `_sistema.py:1081` |
| Número real conhecido (interno) | SDR da Eikon pareado na Evolution `evolution-sdr`: JID `556294570553@s.whatsapp.net` (fluxo n8n 8 enviava 1:1 para ele) — número da operação Eikon/tatuagem, não da FULLX; **não usar sem o Julio decidir** | MEM/crm-eikon-whatsapp-inbox; MEM/sdr-leads-whatsapp |
| Calendly | nenhuma URL em nenhuma fonte (`CALENDLY_URL` vazio) | LEIA-ME |
| Webhook dos modelos de funil | `WEBHOOK_URL:''` (modo demonstração) e `EVENTOS_URL` vazio | `_sistema.py:1080` |
| Google Agenda da aula | link TEMPLATE "Aula ao vivo FULLX", 25/10 17:00Z–18:30Z, "O link do Google Meet chega no grupo do WhatsApp" | AULA-A:910 |
| Publicação | `deploy.sh` = `vercel deploy --prod --yes --scope sistemacrmbuilderforms`; conector Vercel do claude.ai dá 403 nesse time | `deploy.sh`; MEM/vercel-setup-agente |
| Sistemas da Eikon (domínios internos) | CRM `eikonappinterno.online`; cobranças `eikonfinanceirointerno.online`; links `eikonmarketingatendimento.online`; site cliente tatuagem `eikonmarketingtattoo.com` | MEM/* |

## 7. Linguagem do Julio

Ressalva: as transcrições das aulas do operacional (voz falada) não estão acessíveis nesta máquina (seção 5). As frases abaixo são o texto que o Julio publicou ou aprovou nas landings de 16/10 e nos anúncios de 14/10 — é a voz escrita da marca hoje. Fonte entre parênteses.

1. "Você já estudou tráfego, funil e venda. Agora veja o sistema rodando." (AULA-A, H1)
2. "Seu problema não é conhecimento. É instalação." (AULA-A e AULA-B)
3. "Curso ensina a peça. Quase ninguém mostra como as peças se ligam dentro de uma agência com cliente pagando boleto todo mês." (AULA-A)
4. "Eu não ensino o que li. Mostro o que roda." (AULA-A) / "Eu mostro o que roda, não o que li." (AULA-B)
5. "Isso não é teoria. É a operação, gravada." (AULA-A, seção de provas)
6. "Quatro canos, na ordem em que o dinheiro passa. Toda agência vaza em pelo menos um. Eu abro cada um na minha operação." (AULA-A)
7. "O mês depende de indicação. Você anuncia para cliente e não para a própria agência." (AULA-A)
8. "Lead chega, mas sem verba. A semana vai embora em call com curioso." (AULA-A)
9. "Só você vende. Sem roteiro e sem CRM, cada call é um chute." (AULA-A)
10. "Cliente cancela em 3 meses. Boleto atrasa. Time demora para produzir." (AULA-A)
11. "É o critério que separa quem tem verba de quem é curioso, antes de gastar uma call." (AULA-A, ficha do lead)
12. "Se você domina a primeira lista e o faturamento ainda oscila, o gargalo está na segunda." (AULA-A)
13. "Para quem já tem cliente e cansou de recomeçar o mês do zero." (AULA-A)
14. "Não é aula de tráfego. É a operação aberta: anúncio, formulário com pontuação, CRM, roteiro e cobrança, ligados entre si. A parte que curso costuma pular." (AULA-A, FAQ)
15. "Em 20 minutos você anota uma ação para aplicar na sua agência. Se não anotar, pode sair." (AULA-A)
16. "No final eu apresento a mentoria FULLX. Fica quem quiser." (AULA-A e AULA-B)
17. "Daqui a 90 dias, sua agência vai depender de quem?" (AULA-A) / "Daqui a 30 dias, de onde vem o seu próximo cliente?" (AULA-B)
18. "A promessa vem de uma linha do tempo, não de uma teoria." (AULA-B)
19. "Sua agência anuncia todo dia e o mês ainda fecha na indicação? Então o problema não é mais lead. É o que acontece depois que ele chega." (ANUNCIOS 01)
20. "Não foi curso. Foi processo: geração de demanda, 4 funis de captação, estrutura comercial e operação." (ANUNCIOS 02)

Padrões observáveis: frases curtas, verbo no presente, 2ª pessoa ("você"), vocabulário de encanamento (cano, vaza, instalar, roda), oposição recorrente teoria × tela/operação, "curioso" × "verba", "boleto" como símbolo de cliente pagante. Palavras que ele evita nas páginas: "garantido", "fórmula", "segredo", "método" como substantivo isolado. Expressão que o RMBC atribui a ele como história de fundo (HIPÓTESE de narrativa, não citação): "Eu não criei esses sistemas para vender. Criei porque a minha agência estava quebrando por dentro… e eu não tinha dinheiro para pagar dev. Então construí com IA." (RMBC linha 625–630)

## 8. Hipóteses estratégicas (não são fatos; marcadas como HIPÓTESE)

- HIPÓTESE 1 — Unificar o número de autoridade. Há quatro versões (+2.300 / +420 / +150 ativos / 152 no CRM). A mais defensável em tela é a que puder ser mostrada no CRM ou em print; "+R$10 milhões em tráfego" é a única constante e deve ser o número-âncora até o Julio decidir.
- HIPÓTESE 2 — A "primeira agência em 2024 → R$100 mil em 90 dias" e a "Inout desde 2017" podem ser duas empresas diferentes (Eikon/tatuagem desde 2017 e uma segunda operação em 2024) ou duas versões da mesma história. Precisa de resposta do Julio antes de qualquer copy de linha do tempo.
- HIPÓTESE 3 — A prova mais forte e mais barata é a que o RMBC já pede: vídeo de tela do CRM, do formulário com pontuação e da régua de cobrança com números reais (RMBC "Provas a produzir, prioridade 1"). As placas da Kiwify provam infoproduto, não agência, e podem confundir o ICP.
- HIPÓTESE 4 — Enquanto IA comercial e white label não existirem rodando, as páginas 09 (white label) e os cartões "IA comercial" devem ser escritos como lista de espera/demonstração do roadmap, não como produto disponível (coerente com a regra do RMBC: garantia e promessa só sobre o que a FULLX controla).
- HIPÓTESE 5 — O preço publicado (R$2.500–5.000, individual) e o formato dos modelos (turma, grupo pequeno, 90 dias) descrevem produtos diferentes; copy das páginas 04/05 deve esperar a decisão de produto que o próprio RMBC lista como pendência nº 1.
- HIPÓTESE 6 — A assinatura "Não estude. Instale." está nas páginas soltas (vsl.html) mas não nas landings publicadas; o RMBC alerta proximidade com "Não é curso. É método aplicado." (Agência de Valor). Usar o mecanismo "encanamento/canos", que já está nas landings, como linguagem principal.
- HIPÓTESE 7 — O WhatsApp do time para as páginas provavelmente será um número FULLX novo, não o do SDR da Eikon (número de outra marca/nicho).

## 9. Informações ausentes (nenhuma fonte preenche)

Placeholders literais encontrados em `paginas/*.py` e `_comum.py` (grep `\[[A-Z+R$][^]]+\]`), mais lacunas das landings publicadas:

| # | Placeholder / lacuna | Onde | O que falta |
|---|---|---|---|
| 1 | `[+XXX clientes atendidos]` | `_comum.py:50` (PROOF, aparece em várias páginas) | número oficial de clientes (ver conflito 2.300/420/150/152) |
| 2 | `[DESCREVA A ENTREGA DESTE FUNIL EM 2 FRASES]` | `_comum.py:56` (FAQ "O que eu recebo exatamente?") | entregável por funil |
| 3 | `[XXX] agências atendidas` e `[X anos] de operação` | `p01_institucional.py:27` | nº de agências atendidas pela mentoria; anos de operação (2017? 2024?) |
| 4 | `[DEPOIMENTO REAL EM 2 FRASES, COM UM NÚMERO]`, `[NOME]`, `[AGÊNCIA · CIDADE]` ×3 | `p01_institucional.py:63–65` (bloco oculto por `data-draft`) | depoimentos nomeados; RMBC só cita "Eluan e Brayan" e "mentorado dos 3 churns" sem dados |
| 5 | `[AUTOR]`, `[DD/MM/AAAA]`, `[PONTO 1..3]`, `[TEXTO]` | `p01c_blog_artigo.py:11` e corpo | autor e data do artigo; conteúdo |
| 6 | `[PONTO DO VÍDEO]` | `p03_vsl_qualificacao.py` | minutagem da VSL (não existe VSL gravada) |
| 7 | `[R$X e R$Y]` (faixa de investimento) | `p03`, `p04`, `p05` | faixa oficial de preço da mentoria (publicado só na aula: R$2.500–5.000) |
| 8 | `[XX] vagas` por turma | `p05_aplicacao.py:21` | vagas por turma; sequer está decidido se é turma ou individual |
| 9 | `[TÍTULO DO EBOOK]`, `[XX] páginas` | `p06_playbook_ebook.py` | playbook PDF não existe pronto |
| 10 | `[R$X]/mês` (planos Start e "Mais escolhido"), `[Sob consulta]` (Scale), `[10]`/`[50]` clientes por plano | `p09_software_whitelabel.py:43–45` | preços e limites do white label |
| 11 | `[PRAZO] após a assinatura` | `p09_software_whitelabel.py` FAQ | prazo de implantação do white label |
| 12 | `[DESCREVA HOSPEDAGEM, BACKUP E LGPD]` | `p09_software_whitelabel.py` FAQ | infraestrutura/LGPD (CRM roda em Vercel+Neon; cobranças em Railway — ninguém redigiu isso) |
| 13 | Curso gratuito em 5 aulas (títulos das aulas, `CURSO_URL`) | `p07_playbook_curso.py` | curso não existe |
| 14 | `CALENDLY_URL`, `DOWNLOAD_URL`, `VIDEO_URL`, `TRAILER_URL`, `WEBHOOK_URL`, `EVENTOS_URL`, `BACK_URL` | CONFIG de todos os modelos | nenhum link real |
| 15 | WhatsApp do time (`5500000000000`) | landings A/B e modelos | número oficial da FULLX |
| 16 | Handle do Instagram (`instagram.com/`) | landings A/B | perfil oficial |
| 17 | GTM id (`gtm.js?id=`) | landings A/B | container GTM |
| 18 | Domínio canônico (fullx.com.br × fullxmarketing.com × grupofull10x.com) | canônicos e _gerar.py | decisão de domínio |
| 19 | Cidade/sede da FULLX e da Eikon | — | não aparece em nenhuma fonte |
| 20 | Garantia da mentoria | — | só hipótese no RMBC |
| 21 | Duração e formato oficiais da mentoria (30 dias? 90 dias? individual? grupo?) | AULA-A × p05 × RMBC | decisão de produto (pendência nº 1 do RMBC) |
| 22 | Nome do formulário de qualificação ("Builder Forms"?) e nomes comerciais dos 4 softwares | RMBC × `_comum.py` | naming oficial |
| 23 | O que gerou as placas/saques da Kiwify (qual produto, qual período) | `prova/` | contexto das provas |
| 24 | Fonte do "+R$10 milhões em receita gerada" e do "+2.300 clientes de serviço" | AULA-A/B | base de cálculo |
| 25 | Voz falada do Julio (transcrições do operacional) | pasta inacessível | reler quando os arquivos do Drive forem baixados |

### Contagem
- Fatos verificados com fonte (linhas das tabelas das seções 1–6, números de mercado e frases da seção 7): **116**
- Informações ausentes: **25** itens acima (36 placeholders literais distintos nos `.py`, agrupados)

### Regras de ouro para quem reescrever
1. Só três números são seguros sem perguntar: **+R$10 milhões em tráfego Ads**, **pixel 1127997753074983**, **aula 25/10/2026 14h, Google Meet, 100 lugares**.
2. Qualquer número de clientes, faturamento, "primeira agência", anos de operação e preço precisa de decisão do Julio (conflitos documentados na seção 2a e 4b).
3. Não afirmar que existem: IA comercial, white label, gateway próprio, playbook PDF, curso em 5 aulas, blog, depoimentos.
4. CRM e cobrança próprios existem e rodam: pode descrever o que fazem (seção 3b), sem citar "painel de inadimplência em uso".
