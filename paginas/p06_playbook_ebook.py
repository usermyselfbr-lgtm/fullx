# ═══════════════════ 06 · PLAYBOOK EBOOK ═══════════════════
# Isca real: ~/Downloads/FULLX/Playbook-Full10X.pdf (147 páginas, 11 partes), servida em /playbook/Playbook-Full10X.pdf
from _comum import *

f6 = step(1, 'Libere o seu PDF', '', CONTATO() + '<div class="fld"><label for="f-perfil2">Você é</label><select id="f-perfil2" name="perfil" required data-err="Escolha uma opção." data-min="1"><option value="">Selecione</option><option value="dono">Dono ou sócio de agência</option><option value="gestor">Gestor de tráfego</option><option value="outro">Outro</option></select></div>')
done6 = OK('O playbook é seu.', 'PDF de 25 MB: no 4G, salve para ler depois. Comece pela Parte 11, que diz por onde ir.', f'<a class="btn btn-primary on-light" href="#" data-dl="DOWNLOAD_URL" target="_blank" rel="noopener">{ic("down")}Baixar o playbook (PDF)</a>')
# capa desenhada em código com o título e o nº de páginas reais do PDF
cover = f'''<div class="book-wrap reveal" aria-hidden="true">
  <div class="book"><div class="cv">
    {mark('cv', size=52)}
    <div><p class="k">PLAYBOOK FULL10X · EDIÇÃO 2026</p><p class="tt">Mais clientes &amp; receita</p><p class="pp">147 páginas · PDF</p></div>
  </div></div></div>'''
PARTES = [('Partes 01 a 04', 'Antes de anunciar', 'Em que fase a agência está, as 5 métricas de base (CAC, LTV, retorno, ticket e conversão), a conta que diz se dá para escalar, ICP, escada de valor e os 8 elementos de uma oferta.'),
          ('Partes 05 a 07', 'Atrair, filtrar e fechar', 'Ângulos e hooks, funil de diagnóstico com vídeo e aplicação, social selling, os 4 tipos de SDR, a call de decisão do closer, quantas pessoas o comercial precisa e o pipeline do CRM etapa por etapa.'),
          ('Partes 08 a 11', 'Sustentar e escalar', 'Pós-venda em 5 etapas, fluxos por WhatsApp e e-mail, KPIs e rotinas de gestão, IA no comercial e o plano de 6 semanas com checklist mestre.')]
MODOS = [('45 minutos', 'Leitura rápida', 'A Parte 02 inteira e, de cada módulo, só o objetivo e as armadilhas.'),
         ('6 semanas', 'Implementação', 'Semana a semana, com a métrica que precisa mexer em cada etapa.'),
         ('Quando travar', 'Consulta', 'A tabela "onde está o meu problema" leva direto ao módulo certo.')]
cards = lambda xs: ''.join(f'<article class="card reveal"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p></article>' for k, t, d in xs)
body = f'''{topbar('t8')}
<main>
<section class="sec hero glow">
  <div class="wrap split">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Playbook gratuito · PDF · 147 páginas</span>
      <h1>O playbook da agência inteira, grátis.</h1>
      <p class="lead">Atrair, filtrar, fechar e sustentar, na ordem em que o dinheiro passa: oferta, criativo, funil, pré-vendas, closer, CRM e retenção. No fim, um plano de 6 semanas para implantar um módulo por vez.</p>
      <div style="margin-top:30px;max-width:480px" data-hero-cta>{form_card('playbook-ebook', 'Grátis · download na hora', f6, 'Liberar meu playbook', done6, evento='Lead', fid='form')}</div>
      {PROOF}
    </div>
    {cover}
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>O que tem dentro das 147 páginas.</h2></div>
    <div class="grid g3">{cards(PARTES)}</div>
  </div>
</section>
<section class="sec mist">
  <div class="wrap">
    <div class="head center reveal"><h2>147 páginas não são para ler de uma vez.</h2><p class="lead">Ler não muda nada. Implementar muda. Escolha o modo que cabe no seu momento.</p></div>
    <div class="grid g3">{cards(MODOS)}</div>
    <div class="cta-row reveal" style="justify-content:center"><a class="btn btn-primary btn-m" href="#form" data-go="#form" data-pos="conteudo">Baixar o playbook grátis</a></div>
  </div>
</section>
</main>
{footer('f8', full=False)}
{mbar('Baixar o playbook grátis')}'''
pages['06-playbook-ebook.html'] = page('Full10X · Playbook gratuito: mais clientes e receita para agência', 'Baixe grátis o Playbook Full10X: 147 páginas de oferta, funil, comercial e retenção para donos de agência, com plano de 6 semanas.', 'https://grupofull10x.com/playbook', 'playbook-ebook', body,
  ",\n  DOWNLOAD_URL:'/playbook/Playbook-Full10X.pdf' /* PDF real em static/playbook/ (147 páginas) */")
