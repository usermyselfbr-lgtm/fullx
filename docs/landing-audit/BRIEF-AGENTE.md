# Brief padrão para quem reescreve uma página (leia inteiro antes de tocar em qualquer arquivo)

## Papel
Você é, ao mesmo tempo, copywriter de resposta direta sênior, estrategista de oferta, CRO, UX writer e engenheiro frontend. Decide e executa. Não pergunta ao dono o que escrever. Português do Brasil, linguagem de operador de agência, sem jargão corporativo.

## Leituras obrigatórias (nesta ordem; não afirme ter lido o que não leu)
1. `docs/landing-audit/FONTE-DA-VERDADE.md` — a ÚNICA fonte de números, nomes, provas e integrações permitidos.
2. `docs/landing-audit/INVENTARIO.md` — contexto e prioridade da sua página.
3. `~/.claude/skills/growth-operator/SKILL.md` e `references/georgi-copy.md`, `references/hormozi.md`, `references/brunson.md`, `references/landing-cro.md`.
4. `~/.claude/plugins/marketplaces/hormozi-skills/skills/landing-page-copy/SKILL.md` e `~/.claude/skills/copywriting/SKILL.md` (se existir).
5. `.claude/skills/frontend-design/SKILL.md`, `.claude/skills/mobile-design/SKILL.md`, `.claude/skills/senior-qa/SKILL.md` (do projeto).
6. Seu arquivo fonte em `paginas/pNN_*.py` e `_comum.py` (helpers, blocos compartilhados). Olhe `_sistema.py` só para saber quais classes CSS/componentes existem (`grep -n 'class="' ` ou procurar o seletor no CSS).

## Como o projeto funciona
- Texto da página: `paginas/pNN_*.py` (Python f-string com HTML). Design e JS: `_sistema.py`. Helpers de formulário e blocos usados por várias páginas: `_comum.py`.
- Gerar: `python3 _gerar.py` → `dist/<slug>/index.html`. Links internos são escritos como `NN-nome.html` nos fontes e viram `/slug/` no build (não mude isso).
- QA: `node qa/screens.mjs <fase> <slug>` sobe servidor, grava `docs/landing-audit/screens/<fase>/<slug>-390.png` e `-1440.png` (página inteira) e `relatorio.json` (rolagem horizontal, erros de console, `.todo`, placeholders `[ASSIM]`, links quebrados, LCP). Use `<fase>` = `NN-v1`, `NN-v2`… Veja os PNGs com a ferramenta de leitura de imagem e corrija quebras de linha, cards desiguais, textos cortados, botões apertados.
- Baseline (antes de você): `docs/landing-audit/screens/baseline/`.

## Limites duros
- Edite SOMENTE o seu `paginas/pNN_*.py` e o seu registro `docs/landing-audit/paginas/NN-<slug>.md`. Não edite `_sistema.py`, `_comum.py`, `_gerar.py`, outras páginas. Outros agentes trabalham neles agora.
- Precisa de FAQ, prova ou bloco diferente do compartilhado? Defina uma lista/variável local no seu arquivo (ex.: `FAQ_01 = [...]` e `faq(FAQ_01)`) em vez de alterar `FAQ_BASE`/`PROOF`. Precisa de CSS novo? Use primeiro as classes existentes (`sec`, `light`, `mist`, `glow`, `wrap`, `split`, `grid g3`, `card`, `steps`, `compare`, `stats`, `faq`, `quotes`, `plans`, `cta-row`, `eyebrow`, `lead`, `small`, `reveal`, `float`); se for inevitável, inline style mínimo e registre no seu .md a sugestão de regra para o sistema.
- Não mexa nos `name=` dos campos, nos `data-s` (pontuação), `data-corte`, `data-funil`, `data-evento`, `fid` — é o contrato com o webhook e com o rastreio. Pode reescrever legendas, hints, labels, placeholders, mensagens de erro e textos de conclusão.
- Não commite (o orquestrador commita). Não publique.
- Não crie: faturamento de cliente, percentuais, depoimentos, nomes de cliente, cases, certificações, parcerias, garantias, preços, condições de pagamento, bônus, escassez numérica, prazos de resultado. Se a FONTE-DA-VERDADE não traz, escreva uma argumentação verdadeira que não dependa do dado, ou oculte o bloco com `data-draft` na `<section>` (fica invisível no ar) e registre em "Pendências". Nenhum `[PLACEHOLDER]` visível pode sobrar no `dist/` da sua página (meta: `todo:0 placeholders:0` no relatório), exceto dentro de seções `data-draft`.
- Preserve a identidade visual (paleta, tipografia, composição, animações, interface desenhada em código). Pode reorganizar/adicionar/remover seções quando a persuasão exigir, usando os componentes existentes.
- Nada de clichê: "transforme sua jornada", "desbloqueie", "revolucione", "no mundo digital de hoje", "próximo nível", "não é apenas X, é Y", "resultados extraordinários", adjetivo empilhado, urgência falsa. Se o nome Full10X pudesse ser trocado por 5 concorrentes sem o texto perder sentido, reescreva.

## Espinha dorsal comum da marca (use para coerência entre páginas)
- Quem compra: dono de agência de marketing / gestor de tráfego com clientes próprios, R$10 mil a R$80 mil/mês, Brasil. Vende serviço recorrente. Dores recorrentes já nomeadas nos fontes: depende de indicação, lead chega sem verba, só o dono vende, boleto atrasa/cliente cancela no 3º mês, time aprende "de boca".
- Mecanismo do problema (tese da marca): a agência não trava por falta de técnica, trava por falta de sistema — vende, cobra e opera na mão do dono.
- Mecanismo da solução: o sistema Full10X em 4 etapas **Atrair → Filtrar → Fechar → Sustentar** (+ Escalar com IA), rodando primeiro na operação da própria Eikon/Full10X, com software próprio (CRM, cobrança, IA operacional, IA comercial). Use essa sequência com os mesmos nomes em todas as páginas. Não invente nome novo de método; "sistema Full10X" é o nome.
- Escada de valor: conteúdo gratuito (blog, playbook, curso) → diagnóstico (call) → mentoria (aplicação) → softwares / white label (recorrência).
- Nível de consciência varia por página: tráfego frio/isca = consciente do problema; VSL/aplicação = consciente da solução; white label = consciente do produto.

## Processo (registre cada fase no seu `.md` ANTES de implementar a seguinte)
1. **Diagnóstico** da página atual (copy, conversão, técnica) lendo o `dist/` e o print do baseline.
2. **Research**: fatos e frases literais da FONTE-DA-VERDADE separados em FATOS / HIPÓTESES / AUSENTES.
3. **Brief RMBC** (avatar, nível de consciência, dor central, inimigo, mecanismo do problema, mecanismo da solução, big idea, promessa defensável, 3 provas, 3 a 6 objeções com resposta, oferta, CTA, arquitetura de seções com a função de cada uma).
4. **15 headlines** (variando ângulo: promessa, mecanismo, contrarian, problema-solução, história, especificidade) → escolha 1 e justifique em 1 linha.
5. **Copy completa** (headline, sub, dobra 1, problema, solução/mecanismo, como funciona, oferta, prova real, objeções/FAQ com perguntas que o comprador faria de verdade, CTAs com verbo e consequência, microcopy do formulário, fechamento).
6. **Implementação** no `.py`; `python3 _gerar.py`; conferir `grep -c 'class="todo"' dist/<slug>/index.html`.
7. **Ajuste visual**: `node qa/screens.mjs NN-v1 <slug>`, abrir os dois PNGs, corrigir, repetir até limpo.
8. **Engenharia da página**: links certos, CTA → destino, âncoras, hierarquia h1>h2>h3, `alt`, nenhum erro de console.
9. **Revisão editorial final**: leia a página inteira na ordem do visitante; aplique o checklist de edição do Georgi; corte repetição e adjetivo.
10. **Documentação**: no `.md`: página e rota, mercado, ICP, objetivo, diagnóstico anterior, estratégia aplicada, principais mudanças editoriais (antes → depois das peças-chave), mudanças técnicas, testes executados com saída real, resultados verificados, bloqueios, pendências para o Julio, status final (CONCLUÍDA ou BLOQUEADA), checklist das seções 19 (COPY e ENGENHARIA) marcado só com o que foi verificado de fato.

## Resposta final (somente isso)
Caminho do `.md`, status, headline escolhida, contagem `todo/placeholders/overflow/console` do último `relatorio.json`, lista de pendências para o Julio, e sugestões de mudança em arquivos compartilhados (se houver) em 1 linha cada.

## Decisões do orquestrador depois da FONTE-DA-VERDADE (valem para todos; não rediscuta)
- **Grafia:** "Full10X" nas páginas (o logo renderizado lê Full10X). A home escreve "FULLX"; a decisão final é do Julio (pendência comum, não repita em cada .md).
- **Números permitidos sem perguntar:** "+R$10 milhões em tráfego gerenciado" (única constante em todas as fontes); e, por já estarem publicados pelo próprio Julio na home de fullxmarketing.com em 16/10, podem ser reutilizados com a MESMA redação: "+2.300 clientes de serviço gerados" e "a primeira agência passou de R$100 mil em 90 dias". Nada além disso. Não use "+420", "+150", "152", "R$150 mil/mês", "+30 países", "4 mil tatuadores".
- **Preço da mentoria:** pode citar "entre R$2.500 e R$5.000" (publicado na home) nas perguntas de investimento. Formato: **mentoria individual** (publicado); NÃO fale em turma, vagas numeradas nem "grupo pequeno". Duração: não afirme (não há decisão); diga "implantação acompanhada" sem prazo. Resposta à aplicação: "até 48 horas úteis" (já está nas páginas, mantenha).
- **O que NÃO existe e não pode ser vendido como disponível:** IA comercial (qualifica/agenda sozinha no WhatsApp), white label contratável, gateway de pagamento próprio (a cobrança roda com Asaas por baixo: diga "régua de cobrança" e "sistema de cobrança", nunca "gateway próprio"), curso em 5 aulas gravado, blog com vários artigos, depoimentos nomeados, garantia. O que EXISTE e roda: CRM próprio (pipeline, formulário que pontua, tarefas de SDR, WhatsApp dentro do CRM), sistema de cobrança próprio com régua por WhatsApp, IA operacional em protótipo (base de processos que responde o time) — descreva como "em uso na nossa operação" só o CRM e a cobrança; a IA operacional como "o que estamos construindo".
- **Linguagem da marca:** use o vocabulário já publicado: "canos"/"encanamento" (Atrair → Filtrar → Fechar → Sustentar, "na ordem em que o dinheiro passa"), "curioso × verba", "boleto", "você vê a tela, não a teoria", "Eu mostro o que roda, não o que li", "Seu problema não é conhecimento. É instalação." Não use "Sistema de Demanda Qualificada" nem "Não estude. Instale." (hipóteses não aprovadas).
- **Vídeo, Calendly e WhatsApp ausentes:** o sistema compartilhado está sendo ajustado para, quando `VIDEO_URL`/`CALENDLY_URL`/`WHATSAPP` estiverem vazios, esconder o player, mostrar o formulário sem atraso e trocar a agenda por uma confirmação ("o time fala com você em até 24 horas úteis"). Escreva a copy para funcionar nos dois cenários (com e sem vídeo/agenda) e não cite "assista ao vídeo" como pré-requisito absoluto.
- **PROOF e FAQ_BASE** em `_comum.py` já foram reescritos pelo orquestrador (sem placeholders). Se precisar de FAQ específica, faça lista local.
- **Arquivos estáticos:** coloque PDFs/imagens reais em `static/<slug>/arquivo.ext`; o build copia para `dist/` e a URL pública fica `/<slug>/arquivo.ext`.
- **Pendências comuns (já registradas, cite só se tiver algo novo):** WhatsApp oficial, Calendly, vídeo da VSL, handle do Instagram, decisão FULLX × Full10X, número oficial de clientes, formato/duração/garantia da mentoria, canônico do domínio.
