# Inventário real das landing pages — Full10X (17/10/2026)

**Repositório:** `~/projetos/fullx-funis` (cópia versionada de `~/Downloads/FULLX/16:10:2026/full10x-funis-v3`, commit inicial `c364c55`).
**Stack:** HTML estático de arquivo único (CSS e JS embutidos) gerado por Python 3: `_sistema.py` (design, componentes, rastreio, JS de formulário), `_comum.py` (helpers e blocos compartilhados), `paginas/pNN_*.py` (texto de cada página), `_gerar.py` (monta `dist/<slug>/index.html`).
**Publicação alvo:** `https://www.fullxmarketing.com/<slug>/` (projeto Vercel `fullx-aula`, pasta `~/projetos/fullx-aula`, `deploy.sh`). A home do domínio continua sendo a landing da aula ao vivo (não faz parte deste inventário).
**Mercado comum:** donos de agência de marketing e gestores de tráfego com clientes próprios (R$10 mil a R$80 mil/mês), Brasil. Produto: softwares Full10X (CRM, gateway de pagamento/cobrança, IA operacional, IA comercial, white label), mentoria Full10X, conteúdos gratuitos.
**Rastreio comum:** Pixel Meta 1127997753074983 (o mesmo da landing da aula), eventos no `dataLayer`, UTMs por 90 dias, webhook JSON (`WEBHOOK_URL`).
**Baseline visual:** `docs/landing-audit/screens/baseline/` (390 e 1440 px, 12 páginas) + `relatorio.json` (0 rolagem horizontal, 0 erro de console em todas).

| # | Página / slug | Arquivo fonte | Produto | ICP | Conversão principal | CTA principal | Oferta atual | Estado da copy | Estado técnico (baseline) | Problemas | Prioridade |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | `/institucional` | `paginas/p01_institucional.py` | Marca + 4 softwares + mentoria + conteúdos | Dono de agência (frio/orgânico/bio) | Clique p/ aplicação (05) ou playbook (06) | "Falar com o time" | Difusa: softwares, conteúdo e mentoria no mesmo peso | Média: headline descritiva, 13 placeholders (stats, depoimentos), sem mecanismo nem prova | OK; depoimentos `data-draft` ocultos | Prova `[XXX]`, sem caso, CTA "Falar com o time" vago | 1 (porta de entrada da marca) |
| 09 | `/white-label` | `p09_software_whitelabel.py` | Software white label | Dono de agência/consultoria que quer revender SaaS | Agendar demonstração (form 3 passos + Calendly) | "Agendar demonstração" | Planos com `[R$X]`, prazo `[PRAZO]`, FAQ com placeholder | Média: boa estrutura, 8 placeholders, benefícios genéricos de SaaS | OK | Preços e prazos ausentes; FAQ de segurança vazia | 2 (receita B2B) |
| 05 | `/aplicacao` | `p05_aplicacao.py` | Mentoria (aplicação 8 perguntas) | Dono de agência R$10–80 mil | SubmitApplication | "Enviar aplicação" | Mentoria; vagas `[XX]`, investimento `[R$X e R$Y]` | Média: pouco argumento antes do formulário; escassez sem número | OK | Placeholders de vagas/investimento | 3 |
| 04 | `/mentoria` | `p04_vsl_form_calendly.py` | Mentoria (VSL + aplicação + agenda) | Idem, tráfego pago | SubmitApplication + Schedule | "Ver horários" | Mentoria; vídeo não configurado | Fraca: headline genérica ("sistema que fecha cliente toda semana"), sem mecanismo nem prova além da linha PROOF | Vídeo sem URL (placeholder visível) | VIDEO_URL e CALENDLY_URL vazios | 3 |
| 03 | `/assista` | `p03_vsl_qualificacao.py` | Mentoria (VSL + qualificação) | Idem, tráfego pago | SubmitApplication | "Enviar aplicação" | Mentoria; 3 "pontos do vídeo" em placeholder | Fraca: seção "o que você vai ver" vazia | Vídeo sem URL | VIDEO_URL vazio; investimento `[R$X e R$Y]` | 4 |
| 02 | `/diagnostico` | `p02_form_calendly.py` | Call de diagnóstico 30 min | Dono de agência | Lead + Schedule | "Agendar minha call" | Diagnóstico gratuito | Média: promessa clara, FAQ genérica com placeholder | OK | CALENDLY_URL vazio; FAQ `[DESCREVA A ENTREGA]` | 4 |
| 06 | `/playbook` | `p06_playbook_ebook.py` | Isca: playbook PDF (formulário que qualifica) | Topo de funil | Lead + download | "Quero o playbook" | PDF `[TÍTULO]`, `[XX]` páginas | Boa headline; capa em placeholder | DOWNLOAD_URL vazio | PDF real não existe/confirmado | 5 |
| 07 | `/curso` | `p07_playbook_curso.py` | Isca: curso gratuito 5 aulas | Topo/meio | CompleteRegistration | "Liberar meu acesso" | Curso; área de membros sem URL | Boa estrutura; promessa "vende toda semana" sem sustentação | TRAILER_URL e CURSO_URL vazios | Curso real não confirmado | 5 |
| 01b | `/conteudos` | `p01b_blog.py` | Blog (lista) | SEO/conteúdo | Lead (aviso WhatsApp) | "Quero receber" | 6 posts fictícios que apontam todos para o mesmo artigo | Média | OK | Conteúdos são modelo, não reais | 6 |
| 01c | `/conteudos/4-funis-agenda-comercial` | `p01c_blog_artigo.py` | Artigo/aula (modelo) | SEO/remarketing | Clique p/ playbook | "Baixar o playbook grátis" | Artigo com 10 placeholders de texto | Vazia (esqueleto) | OK | Precisa do artigo inteiro, autor e data | 6 |
| 08 | `/espera` | `p08_backredirect.py` | Backredirect (oferta de saída) | Quem aperta voltar | Lead + download | "Quero o playbook" | Playbook | Boa e curta | DOWNLOAD_URL vazio; `noindex` | — | 7 |
| 00 | `/modelos` | `p00_modelos.py` | Índice interno dos modelos | Uso interno do Julio | Navegação | — | — | Funcional | `noindex` | Não é página de venda | 8 (só revisar texto) |

## Classificação
1. **Importância comercial:** 01, 09, 05/04/03 (mentoria), 02, iscas (06/07), conteúdo (01b/01c), utilitárias (08/00).
2. **Fragilidade da copy:** 01c (vazio) > 03/04 (headline genérica, pontos vazios) > 01 (sem prova) > 09 (planos vazios) > 05 > 02 > 06/07 > 08 > 00.
3. **Problemas críticos de conversão:** todos os formulários estão em modo demonstração (`WEBHOOK_URL` vazio), WhatsApp `5500000000000`, Calendly/vídeo/PDF sem URL. Sem isso a página não converte de verdade.
4. **Falhas técnicas:** nenhuma de renderização no baseline; ver auditoria do sistema compartilhado em `SISTEMA.md`.
5. **Impacto potencial:** 01 e 09 (tráfego de marca e receita de software), depois o trio da mentoria.

## Ordem de execução
01 → 09 → 05 → 04 → 03 → 02 → 06 → 07 → 01b → 01c → 08 → 00 (páginas independentes rodam em paralelo quando não compartilham arquivo).
