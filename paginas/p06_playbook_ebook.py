# ═══════════════════ 06 · PLAYBOOK EBOOK ═══════════════════
from _comum import *

f6 = step(1, 'Receba o playbook agora', '', CONTATO() + '<div class="fld"><label for="f-perfil2">Você é</label><select id="f-perfil2" name="perfil" required data-err="Escolha uma opção." data-min="1"><option value="">Selecione</option><option value="dono">Dono ou sócio de agência</option><option value="gestor">Gestor de tráfego</option><option value="outro">Outro</option></select></div>')
done6 = OK('O playbook é seu.', 'Também enviamos o link para o seu e-mail.', f'<a class="btn btn-primary on-light" href="#" data-dl="DOWNLOAD_URL" target="_blank" rel="noopener">{ic("down")}Baixar o playbook (PDF)</a>')
cover = f'''<div class="book-wrap reveal" aria-hidden="true">
  <!-- 🖼️ MÍDIA: troque o conteúdo de <div class="cv"> por <img> da capa real do ebook (proporção 3:4) -->
  <div class="book"><div class="cv">
    {mark('cv', size=52)}
    <div><p class="k">PLAYBOOK FULL10X</p><p class="tt"><span class="todo">[TÍTULO DO EBOOK]</span></p><p class="pp"><span class="todo">[XX]</span> páginas · PDF</p></div>
  </div></div></div>'''
body = f'''{topbar('t8')}
<main>
<section class="sec hero glow">
  <div class="wrap split">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Playbook gratuito · PDF</span>
      <!-- ✏️ PROMESSA DA ISCA (específica) -->
      <h1>O formulário que separa lead com verba de curioso.</h1>
      <p class="lead">As perguntas, a pontuação e a nota de corte que usamos para só chegar na call quem pode contratar. Pronto para copiar.</p>
      <div style="margin-top:30px;max-width:480px" data-hero-cta>{form_card('playbook-ebook', 'Baixe grátis', f6, 'Quero o playbook', done6, evento='Lead', fid='form')}</div>
    </div>
    {cover}
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>O que tem dentro.</h2></div>
    <div class="grid g3">
      <article class="card reveal float"><span class="k">Capítulo 1</span><h3>As 7 perguntas</h3><p>Ordem, texto e por que cada uma existe.</p></article>
      <article class="card reveal float"><span class="k">Capítulo 2</span><h3>A pontuação</h3><p>Quanto vale cada resposta e como definir o corte.</p></article>
      <article class="card reveal float"><span class="k">Capítulo 3</span><h3>O roteamento</h3><p>O que fazer com lead quente, morno e frio.</p></article>
    </div>
    <div class="cta-row reveal" style="justify-content:center"><a class="btn btn-primary btn-m" href="#form" data-go="#form" data-pos="conteudo">Baixar o playbook grátis</a></div>
  </div>
</section>
</main>
{footer('f8', full=False)}
{mbar('Baixar o playbook')}'''
pages['06-playbook-ebook.html'] = page('Full10X · Playbook gratuito: formulário que qualifica', 'Baixe grátis o playbook com perguntas, pontuação e nota de corte para qualificar leads.', 'https://grupofull10x.com/playbook', 'playbook-ebook', body,
  ",\n  DOWNLOAD_URL:'' /* 🔗 link do PDF (Google Drive, Dropbox ou seu servidor) */")
