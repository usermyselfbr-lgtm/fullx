# ═══════════════════ 01b · CONTEÚDOS ═══════════════════
from _comum import *

body = f'''{topbar('t2', ('Baixar playbook', '06-playbook-ebook.html'), nav=True)}
<main>
<section class="sec hero glow center" style="padding-bottom:clamp(56px,7vw,88px)">
  <div class="wrap"><span class="eyebrow"><i aria-hidden="true"></i>Conteúdo gratuito</span>
    <h1 style="max-width:20ch">O sistema da nossa agência, aberto de graça.</h1>
    <p class="lead">Uma aula ao vivo, um playbook de 147 páginas, aulas curtas em gravação e um artigo. Todos sobre os mesmos 4 canos: atrair, filtrar, fechar e sustentar.</p></div>
</section>
<section class="sec light mist tight">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filtrar conteúdos">
      <button class="chip" type="button" data-f="todos" aria-pressed="true">Todos</button>
      <button class="chip" type="button" data-f="aulas" aria-pressed="false">Aulas</button>
      <button class="chip" type="button" data-f="playbooks" aria-pressed="false">Playbook</button>
      <button class="chip" type="button" data-f="artigos" aria-pressed="false">Artigo</button>
    </div>
    <!-- ✏️ CONTEÚDOS: a lista vem de POSTS em _comum.py (categoria, selo, título, descrição, meta, link). data-cat = aulas | playbooks | artigos -->
    <div class="grid g2">{post_cards(len(POSTS), 'b')}</div>
  </div>
</section>
<section class="sec glow center">
  <div class="wrap"><h2 class="reveal" style="max-width:22ch;margin:0 auto">Saiu conteúdo novo, você fica sabendo.</h2>
    <p class="lead reveal" style="max-width:52ch;margin:16px auto 0">Quando a próxima aula ou o próximo material ficar pronto, mandamos o link no seu WhatsApp. Só isso: um aviso por conteúdo.</p>
    <div class="reveal" style="max-width:460px;margin:28px auto 0;text-align:left">
    {form_card('blog-newsletter', 'Aviso de conteúdo novo', step(1, 'Para onde mandamos o aviso?', '', inp('nome','Seu nome',auto='given-name',err='Escreva seu nome.')+inp('whatsapp','WhatsApp com DDD','tel','(11) 91234-5678',auto='tel-national',err='Confira o WhatsApp: DDD + número.')), 'Quero o aviso', OK('Pronto, você está na lista.', 'Quando sair conteúdo novo, o link chega no seu WhatsApp. Enquanto isso, o artigo dos 4 funis já está no ar.', '<a class="btn btn-primary on-light" href="01c-blog-artigo.html">Ler o artigo</a>'), fid='news')}
    </div></div>
</section>
</main>
{footer('f2')}'''
pages['01b-blog.html'] = page('Full10X · Conteúdos gratuitos para agência', 'Aula ao vivo, Playbook Full10X de 147 páginas, aulas curtas e artigo sobre os 4 canos de uma agência: atrair, filtrar, fechar e sustentar.', 'https://grupofull10x.com/conteudos', 'blog', body)
