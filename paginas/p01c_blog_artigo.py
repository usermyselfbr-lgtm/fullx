# ═══════════════════ 01c · ARTIGO ═══════════════════
from _comum import *

body = f'''{topbar('t3', ('Baixar playbook', '06-playbook-ebook.html'), nav=True)}
<main>
<section class="sec glow" style="padding-bottom:clamp(40px,5vw,64px)">
  <div class="wrap article">
    <a class="crumb" href="01b-blog.html">{ic("left")}Conteúdos</a>
    <!-- ✏️ TÍTULO DO ARTIGO -->
    <h1 style="margin-top:18px">Os 4 funis que enchem a agenda comercial de uma agência</h1>
    <p class="meta">Aula gratuita · <span class="todo">[DD/MM/AAAA]</span> · Por <span class="todo">[AUTOR]</span></p>
  </div>
</section>
<section class="sec light" style="padding-top:clamp(40px,5vw,64px)">
  <div class="wrap article prose">
    <!-- 🖼️ MÍDIA: capa do artigo ou vídeo da aula (16:9). Troque a div .cover por <img> ou <iframe> -->
    <div class="cover">{mark('ac', size=120)}</div>
    <p><strong>Resumo:</strong> <span class="todo">[1 PARÁGRAFO COM A IDEIA CENTRAL DO CONTEÚDO]</span></p>
    <h2>1. Atrair: o funil que não depende de indicação</h2>
    <p><span class="todo">[TEXTO]</span> Escreva frases curtas. Uma ideia por parágrafo. Mostre print sempre que citar um número.</p>
    <blockquote>Coloque aqui a frase mais forte do conteúdo, a que a pessoa vai querer compartilhar.</blockquote>
    <h2>2. Filtrar: lead com verba antes da call</h2>
    <ul><li><span class="todo">[PONTO 1]</span></li><li><span class="todo">[PONTO 2]</span></li><li><span class="todo">[PONTO 3]</span></li></ul>
    <div class="inline-cta"><h3>Quer o modelo pronto?</h3><p>Baixe o playbook com as perguntas, a pontuação e a nota de corte.</p><a class="btn btn-primary" href="06-playbook-ebook.html">Baixar o playbook grátis</a></div>
    <h2>3. Fechar: o roteiro que outra pessoa executa</h2>
    <p><span class="todo">[TEXTO]</span></p>
    <h2>4. Sustentar: cobrança e retenção</h2>
    <p><span class="todo">[TEXTO]</span></p>
    <h3>Próximo passo</h3>
    <p>Se quiser implantar com a gente do lado, <a href="05-aplicacao.html">aplique para a mentoria</a>.</p>
  </div>
</section>
<section class="sec light mist tight">
  <div class="wrap"><div class="head reveal"><h2>Continue lendo</h2></div><div class="grid g3">{post_cards(3, 'r')}</div></div>
</section>
</main>
{footer('f3')}'''
pages['01c-blog-artigo.html'] = page('Os 4 funis que enchem a agenda comercial de uma agência · Full10X', 'Aula gratuita: como atrair, filtrar e fechar clientes sem depender de indicação.', 'https://grupofull10x.com/conteudos/4-funis', 'blog-artigo', body)
