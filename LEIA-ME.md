# Full10X · Modelos de funil

Abra `00-modelos.html` para navegar por todos. Cada página é um HTML único: suba o arquivo e ela funciona.

## O que configurar em cada página (bloco CONFIG no topo do arquivo)
| Campo | Para que serve |
|---|---|
| WEBHOOK_URL | Recebe os leads em JSON (Apps Script, n8n, Make ou CRM). Vazio = modo demonstração |
| WHATSAPP | Número do time (55 + DDD + número) |
| CALENDLY_URL | Páginas 02, 04 e 09: link do evento no Calendly |
| VIDEO_URL / TRAILER_URL | Páginas 03, 04 e 07: link de embed do vídeo |
| DOWNLOAD_URL | Páginas 06 e 08: link do PDF |
| CURSO_URL | Página 07: área de membros |
| BACK_URL | Backredirect: coloque o endereço da página 08 nas outras páginas |

## O que cada lead envia
nome, email, whatsapp, respostas, pontuacao, qualificado, status (parcial | completo), lead_id, funil, pagina, utm_*, fbclid, fbp, fbc.
O envio "parcial" sai assim que a pessoa preenche o contato; o "completo", no final. Junte os dois pelo lead_id.

## Roteamento por qualificação
02, 03, 04 e 05 têm nota de corte (data-corte no <form>). Qualificado vê a agenda ou a confirmação; não qualificado é levado para o playbook gratuito.

## Para editar o design de todas as páginas de uma vez
Edite `_sistema.py` (cores, botões, componentes) e rode `python3 _gerar.py`.
O texto de cada página está em `_gerar.py`.

## Visual v2 (out/2026)
- Interface do produto desenhada em código no topo do site (01) e do white label (09). Para usar print real, troque o bloco `<div class="app">` pelo `<img>` (comentário 🖼️ no arquivo).
- Módulos em grade "bento", cada um com uma mini tela do produto (pipeline, régua de cobrança, chat da IA, base de processos).
- Bloco de depoimentos na página 01 fica oculto no ar até você trocar pelos reais e apagar `data-draft`.
- Tokens de cor, tipografia, raio e sombra no topo do CSS em `_sistema.py`. Edite lá e rode `python3 _gerar.py`.

## Rastreio (todas as 14 páginas)
- **Pixel da Meta** (1127997753074983) em todas, inclusive o índice `00-modelos.html`. Eventos: PageView, AbriuFormulario, InicioCadastro, EtapaFormulario, Lead / SubmitApplication / CompleteRegistration, LeadQualificado, Schedule, CliqueCTA. Também vão para o `dataLayer` (GTM).
- **UTMs**: `utm_source, utm_medium, utm_campaign, utm_content, utm_term, utm_id` + `fbclid, gclid, ttclid` ficam guardados por 90 dias. Quem volta sem UTM no link continua atribuído à campanha que trouxe (último toque) e o primeiro toque vai junto (`ft_utm_*`).
- O `fbclid` vira o cookie `_fbc` da Meta automaticamente.
- Links internos entre as páginas levam as UTMs junto.
- Cada lead chega no webhook com: utm_*, ft_utm_*, fbclid, gclid, fbc, fbp, pagina_entrada e referrer.

## Movimento v3
Títulos entram palavra por palavra com onda de brilho, aurora nas seções escuras, bordas de luz girando (selo, botão no hover, plano em destaque, oferta, vídeo), holofote 3D nos cartões (só com mouse), cabeçalho que encolhe, barra de leitura no topo e formulário que treme no erro e desenha o check no final. Tudo em CSS e JavaScript nativo, sem biblioteca. Quem ativa "reduzir movimento" no sistema vê tudo parado.
Títulos em Inter Tight 500, texto em Geist.
