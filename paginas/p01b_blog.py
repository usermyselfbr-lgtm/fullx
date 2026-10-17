# ═══════════════════ 01b · BLOG ═══════════════════
from _comum import *

body = f'''{topbar('t2', ('Baixar playbook', '06-playbook-ebook.html'), nav=True)}
<main>
<section class="sec hero glow center" style="padding-bottom:clamp(56px,7vw,88px)">
  <div class="wrap"><span class="eyebrow"><i aria-hidden="true"></i>Conteúdo gratuito toda semana</span>
    <h1 style="max-width:18ch">Aulas, playbooks e artigos para agência.</h1>
    <p class="lead">Tudo o que usamos para captar, vender, cobrar e operar. Sem cadastro para ler.</p></div>
</section>
<section class="sec light mist tight">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filtrar conteúdos">
      <button class="chip" type="button" data-f="todos" aria-pressed="true">Todos</button>
      <button class="chip" type="button" data-f="aulas" aria-pressed="false">Aulas gratuitas</button>
      <button class="chip" type="button" data-f="playbooks" aria-pressed="false">Playbooks</button>
      <button class="chip" type="button" data-f="artigos" aria-pressed="false">Artigos</button>
    </div>
    <!-- ✏️ CONTEÚDOS: duplique um bloco <a class="post"> para cada novo conteúdo. data-cat = aulas | playbooks | artigos -->
    <div class="grid g3">{post_cards(6, 'b')}</div>
  </div>
</section>
<section class="sec glow center">
  <div class="wrap"><h2 class="reveal" style="max-width:22ch;margin:0 auto">Receba o próximo conteúdo no WhatsApp.</h2>
    <div class="reveal" style="max-width:460px;margin:28px auto 0;text-align:left">
    {form_card('blog-newsletter', 'Avisos de novos conteúdos', step(1, 'Para onde mandamos?', '', inp('nome','Seu nome',auto='given-name',err='Escreva seu nome.')+inp('whatsapp','WhatsApp com DDD','tel','(11) 91234-5678',auto='tel-national',err='Confira o WhatsApp.')), 'Quero receber', OK('Pronto.', 'Você vai receber o aviso a cada novo conteúdo publicado.'), fid='news')}
    </div></div>
</section>
</main>
{footer('f2')}'''
pages['01b-blog.html'] = page('Full10X · Conteúdos gratuitos', 'Aulas gratuitas, playbooks e artigos para donos de agência e gestores de tráfego.', 'https://grupofull10x.com/conteudos', 'blog', body)
