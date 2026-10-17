# ═══════════════════ 01 · INSTITUCIONAL ═══════════════════
from _comum import *

body = f'''{topbar('t1', ('Falar com o time', '05-aplicacao.html'), nav=True)}
<main>
<section class="sec hero glow center">
  <div class="wrap">
    <span class="eyebrow"><i aria-hidden="true"></i>Softwares e educação para agências</span>
    <!-- ✏️ PROMESSA DA MARCA -->
    <h1>Venda, cobrança e operação da sua agência no mesmo sistema.</h1>
    <p class="lead">CRM, gateway de pagamento e duas IAs feitos para agência, mais o conteúdo para você implantar sozinho. Tudo testado primeiro na nossa operação.</p>
    <div class="cta-row" data-hero-cta>
      <a class="btn btn-primary btn-m" href="#softwares" data-go="#softwares" data-pos="hero">Conhecer os softwares</a>
      <a class="btn btn-ghost btn-m" href="01b-blog.html">Ver conteúdos gratuitos</a>
    </div>
    {PROOF.replace('class="proof-line"','class="proof-line" style="justify-content:center"',1)}
    <!-- 🖼️ MÍDIA: interface desenhada em código. Para usar print real, troque <div class="app">…</div> por <img class="app" src="..." alt="Painel Full10X"> -->
    <div class="shot">{app_mock('hm')}</div>
  </div>
  <div class="wrap">{strip()}</div>
</section>

<section class="sec light">
  <div class="wrap split">
    <div class="reveal"><h2>Agência não trava por falta de técnica. Trava por falta de sistema.</h2></div>
    <div class="reveal"><p class="lead">Lead chega sem filtro, venda depende do dono, boleto atrasa e o time aprende tudo de boca. A Full10X junta as quatro peças que resolvem isso em um só lugar.</p>
      <div class="stats" style="margin-top:36px"><div><b><span class="todo">[XXX]</span></b><span>agências atendidas</span></div><div><b>+R$10MM</b><span>em tráfego gerenciado</span></div><div><b><span class="todo">[X anos]</span></b><span>de operação</span></div></div></div>
  </div>
</section>

<section class="sec glow" id="softwares">
  <div class="wrap">
    <div class="head center reveal"><span class="eyebrow"><i aria-hidden="true"></i>Plataforma Full10X</span><h2 style="margin-top:20px">Quatro softwares. Uma operação.</h2><p class="lead">Use um só ou os quatro integrados. Também disponíveis com a sua marca, em white label.</p></div>
    {soft_cards}
  </div>
</section>

<section class="sec light mist">
  <div class="wrap">
    <div class="head center reveal"><h2>Conteúdo gratuito para implantar sozinho.</h2><p class="lead">Aulas, playbooks e artigos publicados toda semana.</p></div>
    <div class="grid g3">{post_cards(3, 'i')}</div>
    <div class="cta-row reveal" style="justify-content:center"><a class="btn btn-primary btn-m" href="01b-blog.html">Ver todos os conteúdos</a></div>
  </div>
</section>

<section class="sec light">
  <div class="wrap split">
    <div class="reveal"><h2>Prefere implantar com a gente do lado?</h2><p class="lead" style="margin-top:18px">A mentoria Full10X instala o sistema completo na sua agência: aquisição, comercial, cobrança e operação.</p>
      <div class="cta-row"><a class="btn btn-primary btn-m" href="05-aplicacao.html">Aplicar para a mentoria</a></div></div>
    <ol class="steps reveal">
      <li><span class="n">1</span><div><h3>Diagnóstico</h3><p>Onde sua agência vaza: atrair, filtrar, fechar ou sustentar.</p></div></li>
      <li><span class="n">2</span><div><h3>Instalação</h3><p>Funis, CRM, cobrança e IA configurados para a sua operação.</p></div></li>
      <li><span class="n">3</span><div><h3>Acompanhamento</h3><p>Calls semanais até o sistema rodar sem você.</p></div></li>
    </ol>
  </div>
</section>

<!-- ✏️ DEPOIMENTOS: troque pelos reais e apague a palavra data-draft da tag <section> para publicar. Sem depoimento real, este bloco fica oculto no ar. -->
<section class="sec light mist" data-draft>
  <div class="wrap">
    <div class="head center reveal"><h2>Quem já instalou o sistema.</h2></div>
    <div class="quotes">
      <figure class="quote reveal"><p>“<span class="todo">[DEPOIMENTO REAL EM 2 FRASES, COM UM NÚMERO]</span>”</p><footer><span class="av b">AA</span><div><b><span class="todo">[NOME]</span></b><span><span class="todo">[AGÊNCIA · CIDADE]</span></span></div></footer></figure>
      <figure class="quote reveal"><p>“<span class="todo">[DEPOIMENTO REAL EM 2 FRASES, COM UM NÚMERO]</span>”</p><footer><span class="av c">BB</span><div><b><span class="todo">[NOME]</span></b><span><span class="todo">[AGÊNCIA · CIDADE]</span></span></div></footer></figure>
      <figure class="quote reveal"><p>“<span class="todo">[DEPOIMENTO REAL EM 2 FRASES, COM UM NÚMERO]</span>”</p><footer><span class="av d">CC</span><div><b><span class="todo">[NOME]</span></b><span><span class="todo">[AGÊNCIA · CIDADE]</span></span></div></footer></figure>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">{cta_panel('fc', 'Comece pelo que mais dói na sua agência hoje.', 'Diagnóstico com o time ou playbook gratuito: escolha o próximo passo.', [('Falar com o time', '05-aplicacao.html', 'btn-primary'), ('Baixar o playbook grátis', '06-playbook-ebook.html', 'btn-ghost')])}</div>
</section>
</main>
{footer('f1')}
{mbar('Falar com o time', '05-aplicacao.html').replace(' data-go="05-aplicacao.html"','')}'''
pages['01-institucional.html'] = page('Full10X · Softwares e educação para agências', 'CRM, gateway de pagamento, IA operacional e IA comercial para agências, com conteúdo gratuito para implantar.', 'https://grupofull10x.com/', 'institucional', body)
