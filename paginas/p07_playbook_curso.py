# ═══════════════════ 07 · PLAYBOOK CURSO ═══════════════════
from _comum import *

f7 = step(1, 'Crie seu acesso gratuito', '', CONTATO())
done7 = OK('Acesso liberado.', 'Enviamos o login para o seu e-mail. Você já pode começar a primeira aula.', f'<a class="btn btn-primary on-light" href="#" data-dl="CURSO_URL" target="_blank" rel="noopener">Começar a aula 1</a>')
mods = [('Atrair', 'Os 4 funis de captação', '18 min'), ('Filtrar', 'Formulário com pontuação', '14 min'), ('Fechar', 'Roteiro de call e CRM', '22 min'), ('Sustentar', 'Cobrança e retenção', '16 min'), ('Escalar', 'IA no comercial e na operação', '20 min')]
mod_html = ''.join(f'<li><span class="n">{i+1}</span><div><h3>{t}</h3><p>{d} · {m}</p></div></li>' for i, (t, d, m) in enumerate(mods))
body = f'''{topbar('t9')}
<main>
<section class="sec hero glow center">
  <div class="wrap">
    <span class="eyebrow"><i aria-hidden="true"></i>Curso gratuito · 5 aulas</span>
    <h1 style="max-width:20ch">O sistema de uma agência que vende toda semana, em 5 aulas curtas.</h1>
    <p class="lead">Do primeiro anúncio à cobrança. Assista no seu ritmo, de graça.</p>
    <div class="vsl-wrap">{VSL('TRAILER_URL')}</div>
    <div style="max-width:480px;margin:36px auto 0;text-align:left" data-hero-cta>{form_card('playbook-curso', 'Acesso gratuito', f7, 'Liberar meu acesso', done7, evento='CompleteRegistration')}</div>
  </div>
</section>
<section class="sec light">
  <div class="wrap split" style="align-items:start">
    <div class="reveal"><h2>As 5 aulas.</h2><p class="lead" style="margin-top:16px">Cada aula termina com uma tarefa para aplicar na mesma semana.</p>
      <div class="stats" style="margin-top:28px"><div><b>5</b><span>aulas</span></div><div><b>90 min</b><span>no total</span></div><div><b>R$0</b><span>para sempre</span></div></div></div>
    <ol class="steps reveal">{mod_html}</ol>
  </div>
</section>
<section class="sec"><div class="wrap">{cta_panel('c7', 'Comece a aula 1 hoje.', '5 aulas curtas, uma tarefa por semana. Grátis.', [('Liberar meu acesso', '#form', 'btn-primary')]).replace('href="#form"', 'href="#form" data-go="#form" data-pos="final"')}</div></section>
</main>
{footer('f9', full=False)}
{mbar('Liberar acesso grátis')}'''
pages['07-playbook-curso.html'] = page('Full10X · Curso gratuito em 5 aulas', 'Curso gratuito: o sistema de uma agência que vende toda semana, em 5 aulas.', 'https://grupofull10x.com/curso', 'playbook-curso', body,
  ",\n  TRAILER_URL:'' /* 🔗 embed do vídeo de apresentação */,\n  CURSO_URL:''   /* 🔗 link da área de membros (Hubla, Kiwify, etc.) */")
