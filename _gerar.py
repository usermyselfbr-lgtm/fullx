import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _sistema import *
OUT = pathlib.Path(__file__).parent

# ───────────── helpers de formulário ─────────────
def inp(name, label, typ='text', ph='', req=True, auto='', err='', mn=None, opt=False):
    lab = f'{label}{" <span class=\"muted\">(opcional)</span>" if opt else ""}'
    extra = (' required' if req and not opt else '') + (f' autocomplete="{auto}"' if auto else '') + (f' data-err="{err}"' if err else '') + (f' data-min="{mn}"' if mn else '')
    if typ == 'tel': extra += ' inputmode="tel"'
    if typ == 'textarea':
        return f'<div class="fld"><label for="f-{name}">{lab}</label><textarea id="f-{name}" name="{name}" rows="4" placeholder="{ph}"{extra}></textarea></div>'
    return f'<div class="fld"><label for="f-{name}">{lab}</label><input id="f-{name}" name="{name}" type="{typ}" placeholder="{ph}"{extra}></div>'

def radios(name, opts):
    return '<div class="opts">' + ''.join(f'<label class="opt"><input type="radio" name="{name}" value="{v}" data-s="{s}" required>{t}</label>' for v, t, s in opts) + '</div>'

def step(n, legend, hint, inner):
    hid = '' if n == 1 else ' hidden'
    h = f'<p class="hint">{hint}</p>' if hint else ''
    return f'<fieldset data-step="{n}"{hid}><legend>{legend}</legend>{h}{inner}<p class="err" role="alert"></p></fieldset>'

CONTATO = lambda: inp('nome', 'Seu nome', auto='given-name', err='Escreva seu nome.') + inp('email', 'E-mail', 'email', 'voce@agencia.com', auto='email', err='Confira o e-mail.') + inp('whatsapp', 'WhatsApp com DDD', 'tel', '(11) 91234-5678', auto='tel-national', err='Confira o WhatsApp: DDD + número.')

PERFIL = [('dono', 'Dono ou sócio de agência', 3), ('gestor', 'Gestor de tráfego com clientes próprios', 2), ('func', 'Trabalho em uma agência (não decido)', 0), ('comecando', 'Ainda não tenho cliente', 0)]
FATUR = [('ate-6k', 'Até R$6 mil', 0), ('6-10k', 'R$6 mil a R$10 mil', 2), ('10-30k', 'R$10 mil a R$30 mil', 4), ('30-80k', 'R$30 mil a R$80 mil', 3), ('80k+', 'Acima de R$80 mil', 2)]
GARG = [('atrair', 'Atrair: dependo de indicação', 0), ('filtrar', 'Filtrar: lead chega sem verba', 0), ('fechar', 'Fechar: só eu vendo ou a call não fecha', 0), ('sustentar', 'Sustentar: cliente atrasa ou cancela', 0)]
MOMENTO = [('agora', 'Consigo investir agora', 4), ('60-dias', 'Consigo em até 60 dias', 2), ('sem-verba', 'Hoje não consigo investir', 0)]

def form_card(funil, title, steps_html, final, done_ok, done_nok='', corte=None, evento='Lead', fid='form'):
    c = f' data-corte="{corte}"' if corte is not None else ''
    n = steps_html.count('<fieldset')
    prog = '<div class="prog" aria-hidden="true"><i></i></div><span class="prog-t" aria-live="polite"></span>' if n > 1 else ''
    nok = done_nok or ''
    return f'''<div class="form-card" id="{fid}">
  <div class="fh"><b>{title}</b><span>{ic("lock")}Seguro · 1 min</span></div>{prog}
  <form class="fx-form" novalidate data-funil="{funil}" data-final="{final}" data-evento="{evento}"{c}>
    {hp()}
    {steps_html}
    <div class="nav-f"><button type="button" class="back" data-back hidden>Voltar</button><button type="button" class="btn btn-primary on-light" data-next style="margin-left:auto">Continuar</button></div>
    {privacy()}
    <div class="done" data-done="ok" hidden>{done_ok}</div>
    {nok}
    <div class="done" data-done="fail" hidden><h3>Não conseguimos registrar.</h3><p>A conexão falhou. Fale com o time pelo WhatsApp.</p><a class="btn btn-primary on-light" data-wa href="#" target="_blank" rel="noopener">{ic("whats")}Falar pelo WhatsApp</a></div>
  </form>
</div>'''

OK = lambda t, p, extra='': f'<div class="ok">{ic("check")}</div><h3>{t}</h3><p>{p}</p>{extra}'
NOK = lambda: f'<div class="done" data-done="nok" hidden><div class="ok">{ic("check")}</div><h3>Recebemos sua aplicação.</h3><p>Pelo seu momento, o melhor próximo passo é o conteúdo gratuito. Separamos o playbook para você começar hoje.</p><a class="btn btn-primary on-light" href="06-playbook-ebook.html">Baixar o playbook grátis</a></div>'

PROOF = f'<div class="proof-line"><span>{ic("check")}+R$10 milhões em tráfego gerenciado</span><span>{ic("check")}<span class="todo">[+XXX clientes atendidos]</span></span><span>{ic("check")}Sistemas próprios de CRM e cobrança</span></div>'

def mbar(label, go='#form'):
    return f'<div class="mbar"><a class="btn btn-primary" href="{go}" data-go="{go}" data-pos="barra-celular">{label}</a></div>'

FAQ_BASE = [('Para quem é?', 'Para donos de agência e gestores de tráfego que já têm clientes e querem previsibilidade de venda e operação.'),
            ('O que eu recebo exatamente?', '<span class="todo">[DESCREVA A ENTREGA DESTE FUNIL EM 2 FRASES]</span>'),
            ('E se o meu caso for diferente?', 'O sistema é de captação, comercial e operação de agência. Funciona para qualquer nicho que vende serviço recorrente.'),
            ('Por que a Full10X?', 'Porque tudo o que ensinamos e vendemos roda primeiro na nossa operação: tráfego, CRM, cobrança e IA.'),
            ('Como eu começo?', 'Preencha o formulário desta página. O próximo passo aparece na hora.')]

pages = {}

# ═══════════════════ 01 · INSTITUCIONAL ═══════════════════
SOFT = [('crm', 'CRM', 'Pipeline comercial de agência, com etapas, tarefas e histórico de cada lead.', ['Funil visual por etapa', 'Formulário que pontua o lead', 'Tarefas e follow-up do SDR']),
        ('pay', 'Gateway de pagamento', 'Cobrança recorrente com régua automática para o boleto não atrasar.', ['Pix, boleto e cartão recorrente', 'Régua de cobrança por WhatsApp', 'Painel de inadimplência']),
        ('ops', 'IA operacional', 'Treina e orienta o time de entrega com os processos da sua agência.', ['Responde dúvidas do time 24h', 'Base de processos e checklists', 'Onboarding de novo colaborador']),
        ('chat', 'IA comercial', 'Qualifica, responde e agenda leads no WhatsApp enquanto o time dorme.', ['Primeiro contato em segundos', 'Qualificação por perguntas', 'Agendamento direto na agenda'])]
soft_cards = bento(SOFT)

POSTS = [('aulas', 'Aula gratuita', 'Os 4 funis que enchem a agenda comercial de uma agência', 'Como atrair, filtrar e fechar sem depender de indicação.', '42 min'),
         ('playbooks', 'Playbook', 'Playbook: formulário que qualifica lead antes da call', 'Perguntas, pontuação e nota de corte prontas para copiar.', 'PDF · 18 páginas'),
         ('artigos', 'Artigo', 'Por que sua agência perde cliente no terceiro mês', 'Os 3 pontos da entrega que derrubam a retenção.', '7 min de leitura'),
         ('aulas', 'Aula gratuita', 'Roteiro de call: como outra pessoa fecha no seu lugar', 'A estrutura da call que o SDR e o closer seguem.', '35 min'),
         ('playbooks', 'Playbook', 'Régua de cobrança para agência: modelo pronto', 'Mensagens, prazos e o que fazer no atraso.', 'PDF · 12 páginas'),
         ('artigos', 'Artigo', 'CPL baixo não paga boleto: as métricas que importam', 'Da campanha à venda: o que acompanhar toda semana.', '6 min de leitura')]
TH_ART = {'aulas': lambda: f'<span class="th-play">{ic("play")}</span>',
          'playbooks': lambda: '<span class="th-doc"><i></i><i></i><i></i><i></i><i></i><i></i></span>',
          'artigos': lambda: '<span class="th-lines"><i></i><i></i><i></i><i></i></span>'}
TH_IC = {'aulas': 'video', 'playbooks': 'file', 'artigos': 'clock'}
def post_cards(n=6, uid='p'):
    # 🖼️ MÍDIA: para usar capa real, troque o conteúdo de <div class="th"> por <img src="..." alt="" width="640" height="360">
    return ''.join(f'''<a class="post reveal" href="01c-blog-artigo.html" data-cat="{c}"><div class="th"><span class="t">{tag}</span>{TH_ART[c]()}{mark(f"{uid}{i}", size=26)}</div>
<div class="bd"><h3>{t}</h3><p>{d}</p><span class="meta"><span>{ic(TH_IC[c])}{m}</span><span class="go">{ic("arrow")}</span></span></div></a>''' for i, (c, tag, t, d, m) in enumerate(POSTS[:n]))

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

# ═══════════════════ 01b · BLOG ═══════════════════
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

# ═══════════════════ 01c · ARTIGO ═══════════════════
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

# ═══════════════════ 02 · FORM + CALENDLY ═══════════════════
f2 = (step(1, 'Vamos começar pelo seu contato.', 'Leva menos de 1 minuto.', CONTATO())
      + step(2, 'Hoje, você é…', '', radios('perfil', PERFIL))
      + step(3, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses.', radios('faturamento', FATUR)))
done2 = OK('Escolha o melhor horário.', 'Seus dados já estão preenchidos na agenda.', '<div data-calendly></div>')
body = f'''{topbar('t4')}
<main>
<section class="sec hero glow">
  <div class="wrap split">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Call de diagnóstico · 30 minutos</span>
      <!-- ✏️ PROMESSA DA CALL -->
      <h1>Descubra em 30 minutos onde sua agência perde venda.</h1>
      <p class="lead">Uma call com um especialista para mapear captação, comercial e cobrança. Você sai com o gargalo nomeado e o próximo passo.</p>
      <ul class="steps" style="margin-top:32px">
        <li><span class="n">1</span><div><h3>Preencha 3 perguntas</h3><p>Para a call ser sobre o seu caso.</p></div></li>
        <li><span class="n">2</span><div><h3>Escolha o horário</h3><p>A agenda abre logo depois.</p></div></li>
        <li><span class="n">3</span><div><h3>Receba o diagnóstico</h3><p>Ao vivo, com o plano de ação.</p></div></li>
      </ul>
    </div>
    <div data-hero-cta>{form_card('form-calendly', 'Agende sua call', f2, 'Ver horários', done2, NOK(), corte=3, evento='Lead')}</div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>O que você leva da call.</h2></div>
    <div class="grid g3">
      <article class="card reveal float"><span class="ico">{ic("layers")}</span><h3>Mapa do gargalo</h3><p>Em qual dos 4 pontos sua agência vaza: atrair, filtrar, fechar ou sustentar.</p></article>
      <article class="card reveal float"><span class="ico">{ic("crm")}</span><h3>Números de referência</h3><p>Custo por lead qualificado, taxa de fechamento e churn esperados para o seu tamanho.</p></article>
      <article class="card reveal float"><span class="ico">{ic("check")}</span><h3>Próximo passo</h3><p>Uma ação para aplicar na mesma semana, com ou sem a Full10X.</p></article>
    </div>
  </div>
</section>
<section class="sec glow center"><div class="wrap"><div class="head center reveal"><h2>Perguntas frequentes</h2></div><div class="faq reveal">{faq(FAQ_BASE)}</div></div></section>
</main>
{footer('f4', full=False)}
{mbar('Agendar minha call')}'''
pages['02-form-calendly.html'] = page('Full10X · Agende sua call de diagnóstico', 'Call de 30 minutos para descobrir onde sua agência perde venda.', 'https://grupofull10x.com/diagnostico', 'form-calendly', body,
  ",\n  CALENDLY_URL:''         /* 🔗 link do seu evento: https://calendly.com/seu-usuario/diagnostico */,\n  POS_AGENDAMENTO_URL:''   /* opcional: página de obrigado depois de agendar */")

# ═══════════════════ 03 · VSL + QUALIFICAÇÃO ═══════════════════
f3 = (step(1, 'Seu contato', 'Para o time falar com você.', CONTATO())
      + step(2, 'Hoje, você é…', '', radios('perfil', PERFIL))
      + step(3, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses.', radios('faturamento', FATUR))
      + step(4, 'Qual ponto mais pesa hoje?', 'Usamos isso para preparar a conversa.', radios('gargalo', GARG))
      + step(5, 'Se fizer sentido, qual sua situação para investir?', 'O investimento da mentoria fica entre <span class="todo">[R$X e R$Y]</span>.', radios('momento', MOMENTO)))
done3 = OK('Aplicação recebida.', 'Um especialista vai falar com você pelo WhatsApp em até 24 horas úteis.', '<a class="btn btn-primary on-light" data-wa href="#" target="_blank" rel="noopener">' + ic('whats') + 'Adiantar pelo WhatsApp</a>')
VSL = lambda key='VIDEO_URL': f'''<div class="video" data-embed-key="{key}"><div class="ph"><span class="play">{ic("play")}</span><span>🖼️ Vídeo de vendas. Configure {key} no topo do arquivo.</span></div></div>'''
body = f'''{topbar('t5')}
<main>
<section class="sec hero glow center">
  <div class="wrap">
    <span class="eyebrow"><i aria-hidden="true"></i>Assista antes de aplicar</span>
    <!-- ✏️ HEADLINE = mesmo hook do anúncio -->
    <h1 style="max-width:20ch">Como agências de R$10 mil a R$30 mil passam a fechar cliente toda semana.</h1>
    <div class="vsl-wrap">{VSL()}<p class="vsl-note">Ative o som. O formulário aparece durante o vídeo.</p></div>
    <!-- ⚙️ data-delay = segundos até liberar o formulário (use o momento da oferta no vídeo) -->
    <div class="delayed wait" data-delay="90" data-hero-cta style="max-width:560px;margin:40px auto 0;text-align:left">
      {form_card('vsl-qualificacao', 'Aplicação para a mentoria', f3, 'Enviar aplicação', done3, NOK(), corte=8, evento='SubmitApplication')}
    </div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>O que você vai ver no vídeo.</h2></div>
    <ol class="steps reveal" style="max-width:780px;margin:0 auto">
      <li><span class="n">1</span><div><h3>O motivo real de a agência oscilar</h3><p><span class="todo">[PONTO DO VÍDEO]</span></p></div></li>
      <li><span class="n">2</span><div><h3>O sistema que resolve</h3><p><span class="todo">[PONTO DO VÍDEO]</span></p></div></li>
      <li><span class="n">3</span><div><h3>Como aplicar na sua agência</h3><p><span class="todo">[PONTO DO VÍDEO]</span></p></div></li>
    </ol>
  </div>
</section>
<section class="sec glow center"><div class="wrap"><div class="head center reveal"><h2>Perguntas frequentes</h2></div><div class="faq reveal">{faq(FAQ_BASE)}</div></div></section>
</main>
{footer('f5', full=False)}'''
pages['03-vsl-qualificacao.html'] = page('Full10X · Assista e aplique', 'Vídeo e aplicação para a mentoria Full10X.', 'https://grupofull10x.com/vsl', 'vsl-qualificacao', body,
  ",\n  VIDEO_URL:''   /* 🔗 URL de embed do vídeo: YouTube (https://www.youtube.com/embed/ID), Vimeo, Panda ou Vturb */")

# ═══════════════════ 04 · VSL + FORM + CALENDLY ═══════════════════
f4 = (step(1, 'Seu contato', '', CONTATO())
      + step(2, 'Hoje, você é…', '', radios('perfil', PERFIL))
      + step(3, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses.', radios('faturamento', FATUR))
      + step(4, 'Se fizer sentido, qual sua situação para investir?', 'O investimento da mentoria fica entre <span class="todo">[R$X e R$Y]</span>.', radios('momento', MOMENTO)))
done4 = OK('Você foi aprovado para a call.', 'Escolha o horário. Seus dados já estão preenchidos.', '<div data-calendly></div>')
body = f'''{topbar('t6')}
<main>
<section class="sec hero glow">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Mentoria Full10X</span>
      <!-- ✏️ HEADLINE = mesmo hook do anúncio -->
      <h1>Instale na sua agência o sistema que fecha cliente toda semana.</h1>
      <div style="margin-top:30px">{VSL()}</div>
      {PROOF}
    </div>
    <div class="delayed wait" data-delay="60" data-hero-cta style="position:sticky;top:90px">
      {form_card('vsl-form-calendly', 'Aplique e agende sua call', f4, 'Ver horários', done4, NOK(), corte=8, evento='SubmitApplication')}
    </div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Como funciona.</h2></div>
    <div class="grid g3">
      <article class="card reveal float"><span class="ico">{ic("video")}</span><h3>1. Assista</h3><p>O vídeo mostra o sistema e para quem ele é.</p></article>
      <article class="card reveal float"><span class="ico">{ic("check")}</span><h3>2. Aplique</h3><p>4 perguntas para confirmar se faz sentido para você.</p></article>
      <article class="card reveal float"><span class="ico">{ic("cal")}</span><h3>3. Agende</h3><p>Se aprovado, a agenda abre na hora.</p></article>
    </div>
  </div>
</section>
<section class="sec glow center"><div class="wrap"><div class="head center reveal"><h2>Perguntas frequentes</h2></div><div class="faq reveal">{faq(FAQ_BASE)}</div></div></section>
</main>
{footer('f6', full=False)}'''
pages['04-vsl-form-calendly.html'] = page('Full10X · Mentoria: assista, aplique e agende', 'Vídeo da mentoria Full10X com aplicação e agendamento.', 'https://grupofull10x.com/mentoria', 'vsl-form-calendly', body,
  ",\n  VIDEO_URL:''   /* 🔗 embed do vídeo */,\n  CALENDLY_URL:'' /* 🔗 link do evento no Calendly */,\n  POS_AGENDAMENTO_URL:''")

# ═══════════════════ 05 · APLICAÇÃO ═══════════════════
f5 = (step(1, 'Como você se chama?', 'Comece pelo fácil.', inp('nome', 'Seu nome', auto='given-name', err='Escreva seu nome.'))
      + step(2, 'Para onde mandamos a resposta?', '', inp('email', 'E-mail', 'email', 'voce@agencia.com', auto='email', err='Confira o e-mail.') + inp('whatsapp', 'WhatsApp com DDD', 'tel', '(11) 91234-5678', auto='tel-national', err='Confira o WhatsApp.') + inp('instagram', 'Instagram da agência', ph='@suaagencia', opt=True))
      + step(3, 'Hoje, você é…', '', radios('perfil', PERFIL))
      + step(4, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses.', radios('faturamento', FATUR))
      + step(5, 'Quantas pessoas trabalham com você?', '', radios('time', [('solo', 'Só eu', 0), ('2-3', '2 a 3 pessoas', 1), ('4-8', '4 a 8 pessoas', 2), ('9+', '9 ou mais', 2)]))
      + step(6, 'Qual ponto mais pesa hoje?', '', radios('gargalo', GARG))
      + step(7, 'Se for aprovado, qual sua situação para investir?', 'Investimento entre <span class="todo">[R$X e R$Y]</span>.', radios('momento', MOMENTO))
      + step(8, 'Por que agora?', 'Em 2 linhas: onde você está e onde quer chegar em 90 dias.', inp('motivo', 'Sua resposta', 'textarea', 'Ex.: tenho 8 clientes, fecho por indicação e quero chegar a R$30 mil/mês.', err='Conte um pouco do seu momento.', mn=10)))
body = f'''{topbar('t7')}
<main>
<section class="sec hero glow">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Vagas limitadas por turma</span>
      <h1>Aplicação para a mentoria Full10X.</h1>
      <p class="lead">Respondemos todas as aplicações em até 48 horas úteis. Aprovamos só quem conseguimos ajudar de verdade.</p>
      <!-- ✏️ ESCASSEZ REAL: explique o motivo do limite -->
      <div class="card" style="margin-top:30px"><h3>Por que existe aplicação</h3><p>Cada turma tem <span class="todo">[XX]</span> vagas porque as calls são em grupo pequeno. Aplicação garante que a turma tenha o mesmo momento.</p></div>
      {PROOF}
    </div>
    <div data-hero-cta>{form_card('aplicacao', 'Aplicação · 8 perguntas', f5, 'Enviar aplicação', OK('Aplicação enviada.', 'Você recebe a resposta no WhatsApp em até 48 horas úteis.'), NOK(), corte=9, evento='SubmitApplication')}</div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Quem é aprovado</h2></div>
    <div class="compare" style="max-width:900px;margin:0 auto">
      <div class="no reveal"><h3>Não é para você se</h3><ul><li>Ainda não tem nenhum cliente.</li><li>Procura fórmula sem implementar.</li><li>Não tem como investir nos próximos 60 dias.</li></ul></div>
      <div class="yes reveal"><h3>É para você se</h3><ul><li>Tem agência entre R$10 mil e R$80 mil por mês.</li><li>Quer previsibilidade de venda.</li><li>Está pronto para implantar em 90 dias.</li></ul></div>
    </div>
  </div>
</section>
</main>
{footer('f7', full=False)}
{mbar('Enviar minha aplicação')}'''
pages['05-aplicacao.html'] = page('Full10X · Aplicação para a mentoria', 'Aplique para a mentoria Full10X. Respondemos em até 48 horas úteis.', 'https://grupofull10x.com/aplicacao', 'aplicacao', body)

# ═══════════════════ 06 · PLAYBOOK EBOOK ═══════════════════
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

# ═══════════════════ 07 · PLAYBOOK CURSO ═══════════════════
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

# ═══════════════════ 08 · BACKREDIRECT ═══════════════════
f8 = step(1, 'Para onde mandamos?', '', inp('nome', 'Seu nome', auto='given-name', err='Escreva seu nome.') + inp('email', 'E-mail', 'email', 'voce@agencia.com', auto='email', err='Confira o e-mail.'))
body = f'''<main>
<section class="sec hero glow center" style="min-height:100svh;display:grid;align-content:center">
  <div class="wrap">
    <div style="display:grid;place-items:center">{mark('bk', size=56)}</div>
    <span class="eyebrow" style="margin-top:26px"><i aria-hidden="true"></i>Antes de sair</span>
    <!-- ✏️ OFERTA DE SAÍDA: algo menor e mais fácil do que a oferta da página anterior -->
    <h1 style="max-width:18ch">Leve pelo menos o playbook. É grátis.</h1>
    <p class="lead">Não quis seguir agora? Tudo bem. Leve o modelo de formulário que qualifica lead e aplique sozinho.</p>
    <div style="max-width:460px;margin:34px auto 0;text-align:left" data-hero-cta>
      {form_card('backredirect', 'Receba no e-mail', f8, 'Quero o playbook', OK('Enviado.', 'Confira seu e-mail. O link também está aqui:', f'<a class="btn btn-primary on-light" href="#" data-dl="DOWNLOAD_URL" target="_blank" rel="noopener">{ic("down")}Baixar agora</a>'), evento='Lead')}
    </div>
    <p class="small" style="margin-top:22px"><a href="01-institucional.html">Não, obrigado. Ir para o site.</a></p>
  </div>
</section>
</main>'''
pages['08-backredirect.html'] = page('Full10X · Antes de sair', 'Leve o playbook gratuito da Full10X.', 'https://grupofull10x.com/espera', 'backredirect', body,
  ",\n  DOWNLOAD_URL:''\n  /* COMO USAR: nas outras páginas, coloque em BACK_URL o endereço desta página (ex.: 'https://grupofull10x.com/espera').\n     Quem apertar \"voltar\" no navegador cai aqui. Esta página não tem backredirect para não prender a pessoa. */")

# ═══════════════════ 09 · SOFTWARE WHITE LABEL ═══════════════════
f9 = (step(1, 'Seu contato', '', CONTATO() + inp('empresa', 'Nome da agência ou empresa', err='Escreva o nome da empresa.'))
      + step(2, 'Quantos clientes você atende hoje?', 'Define o plano ideal.', radios('clientes', [('ate-10', 'Até 10', 1), ('11-30', '11 a 30', 2), ('31-100', '31 a 100', 3), ('100+', 'Mais de 100', 3)]))
      + step(3, 'Quais módulos interessam?', 'Pode escolher o principal agora.', radios('modulo', [('crm', 'CRM', 1), ('pagamento', 'Gateway de pagamento', 1), ('ia-op', 'IA operacional', 1), ('ia-com', 'IA comercial', 1), ('todos', 'Todos integrados', 2)])))
done9 = OK('Vamos montar sua demonstração.', 'Escolha o horário. Mostramos o painel com a sua marca.', '<div data-calendly></div>')
body = f'''{topbar('t10', ('Agendar demonstração', '#form', 'data-go="#form" data-pos="topo"'))}
<main>
<section class="sec hero glow">
  <div class="wrap split">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>White label para agências e consultorias</span>
      <h1>Seu próprio software de CRM, cobrança e IA. Com a sua marca.</h1>
      <p class="lead">Revenda para os seus clientes um sistema completo, com seu logo, suas cores e seu domínio. Nós cuidamos da tecnologia.</p>
      <div class="cta-row" data-hero-cta><a class="btn btn-primary btn-m" href="#form" data-go="#form" data-pos="hero">Agendar demonstração</a><a class="btn btn-ghost btn-m" href="#planos" data-go="#planos">Ver planos</a></div>
    </div>
    <!-- 🖼️ MÍDIA: interface desenhada em código, já com "Sua Agência" no lugar da marca. Troque por print real quando tiver -->
    <div class="side-shot reveal">{app_mock('wl', white_label=True)}</div>
  </div>
  <div class="wrap">{strip()}</div>
</section>
<section class="sec glow">
  <div class="wrap">
    <div class="head center reveal"><h2>Quatro módulos, uma marca: a sua.</h2><p class="lead">Seu logo, suas cores e seu domínio em cada tela que o seu cliente vê.</p></div>
    {soft_cards.replace('Ver demonstração', 'Incluído no white label').replace('09-software-whitelabel.html', '#form')}
  </div>
</section>
<section class="sec light">
  <div class="wrap split">
    <div class="reveal"><h2>Como o white label funciona.</h2></div>
    <ol class="steps reveal">
      <li><span class="n">1</span><div><h3>Sua marca</h3><p>Logo, cores, domínio próprio e e-mails com seu nome.</p></div></li>
      <li><span class="n">2</span><div><h3>Seus clientes</h3><p>Você cadastra, define o preço e fica com a margem.</p></div></li>
      <li><span class="n">3</span><div><h3>Nossa tecnologia</h3><p>Servidor, atualização, segurança e suporte de nível 2 com a Full10X.</p></div></li>
    </ol>
  </div>
</section>
<section class="sec light mist" id="planos">
  <div class="wrap">
    <div class="head center reveal"><h2>Planos</h2><p class="lead">Valores de referência. Fechamos a proposta na demonstração.</p></div>
    <div class="plans">
      <div class="plan reveal"><span class="tag">Start</span><p class="price"><span class="todo">[R$X]</span><small>/mês</small></p><p>Até <span class="todo">[10]</span> clientes.</p><ul><li>{ic("check")}CRM com sua marca</li><li>{ic("check")}Domínio próprio</li><li>{ic("check")}Suporte por e-mail</li></ul><a class="btn btn-primary" href="#form" data-go="#form" data-pos="plano-start">Falar com vendas</a></div>
      <div class="plan hot reveal"><span class="tag">Mais escolhido</span><p class="price"><span class="todo">[R$X]</span><small>/mês</small></p><p>Até <span class="todo">[50]</span> clientes.</p><ul><li>{ic("check")}CRM + gateway de pagamento</li><li>{ic("check")}IA comercial</li><li>{ic("check")}Suporte prioritário</li></ul><a class="btn btn-primary" href="#form" data-go="#form" data-pos="plano-pro">Falar com vendas</a></div>
      <div class="plan reveal"><span class="tag">Scale</span><p class="price"><span class="todo">[Sob consulta]</span></p><p>Clientes ilimitados.</p><ul><li>{ic("check")}Os 4 módulos</li><li>{ic("check")}IA operacional treinada</li><li>{ic("check")}Gerente de conta</li></ul><a class="btn btn-primary" href="#form" data-go="#form" data-pos="plano-scale">Falar com vendas</a></div>
    </div>
  </div>
</section>
<section class="sec glow">
  <div class="wrap split" style="align-items:start">
    <div class="reveal"><h2>Veja o painel com a sua marca.</h2><p class="lead" style="margin-top:16px">Na demonstração de 30 minutos montamos uma prévia com o seu logo e mostramos os módulos funcionando.</p>
      <div class="faq" style="margin-top:28px">{faq([("Preciso saber programar?","Não. A configuração é feita pela Full10X."),("Quanto tempo para ficar pronto?","<span class=\"todo\">[PRAZO]</span> após a assinatura."),("Posso cobrar o que eu quiser?","Sim. Você define o preço para o seu cliente e fica com a margem."),("Meus dados ficam seguros?","<span class=\"todo\">[DESCREVA HOSPEDAGEM, BACKUP E LGPD]</span>")])}</div></div>
    {form_card('software-whitelabel', 'Agende sua demonstração', f9, 'Ver horários', done9, evento='Lead', fid='form')}
  </div>
</section>
</main>
{footer('f10')}
{mbar('Agendar demonstração')}'''
pages['09-software-whitelabel.html'] = page('Full10X · Software white label para agências', 'CRM, gateway de pagamento e IA com a sua marca para revender aos seus clientes.', 'https://grupofull10x.com/white-label', 'software-whitelabel', body,
  ",\n  CALENDLY_URL:'' /* 🔗 evento de demonstração */,\n  POS_AGENDAMENTO_URL:''")

# ═══════════════════ 00 · HUB DE MODELOS ═══════════════════
HUB = [('01-institucional.html', 'LP institucional', 'Site da marca com softwares, conteúdos e mentoria.', 'Tráfego frio e orgânico, busca, bio'),
       ('01b-blog.html', 'Blog', 'Lista de aulas, playbooks e artigos com filtro.', 'SEO e conteúdo'),
       ('01c-blog-artigo.html', 'Artigo do blog', 'Modelo de post com CTA para o playbook.', 'SEO e remarketing'),
       ('02-form-calendly.html', 'Formulário + Calendly', 'Qualifica em 3 perguntas e abre a agenda.', 'Call de diagnóstico'),
       ('03-vsl-qualificacao.html', 'VSL + qualificação', 'Vídeo; formulário aparece no momento da oferta.', 'Mentoria high ticket'),
       ('04-vsl-form-calendly.html', 'VSL + formulário + Calendly', 'Vídeo, aplicação e agenda só para aprovados.', 'Mentoria com call'),
       ('05-aplicacao.html', 'Formulário de aplicação', '8 perguntas com nota de corte e escassez explicada.', 'Turmas e high ticket'),
       ('06-playbook-ebook.html', 'Playbook ebook (isca)', 'Captura curta e download na hora.', 'Topo de funil'),
       ('07-playbook-curso.html', 'Playbook curso (isca)', 'Cadastro para curso gratuito em 5 aulas.', 'Topo e meio de funil'),
       ('08-backredirect.html', 'Backredirect', 'Oferta de saída para quem aperta voltar.', 'Recuperar visita perdida'),
       ('09-software-whitelabel.html', 'Software white label', 'Módulos, planos e demonstração com agenda.', 'Venda B2B do software')]
cards = ''.join(f'<a class="card reveal" href="{f}"><span class="k">{f.split("-")[0]}</span><h3>{t}</h3><p>{d}</p><p class="small" style="margin-top:10px">Uso: {u}</p><span class="more">Abrir modelo {ic("arrow")}</span></a>' for f, t, d, u in HUB)
body = f'''<main>
<section class="sec hero glow center" style="padding-bottom:40px"><div class="wrap">{logo('hb', h=40)}<h1 style="margin:28px auto 0;max-width:18ch">Modelos de funil Full10X</h1><p class="lead">{len(HUB)} páginas no mesmo sistema visual. Clique para abrir.</p></div></section>
<section class="sec tight" style="padding-bottom:96px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
</main>'''
pages['00-modelos.html'] = page('Full10X · Modelos de funil', 'Índice dos modelos de página.', 'https://grupofull10x.com/modelos', 'hub', body)

import re as _re
def _setas(html):
    # seta animada nos CTAs principais (só links grandes, sem ícone próprio)
    return _re.sub(r'(<a class="btn btn-primary btn-m"[^>]*>)([^<]+)</a>', lambda m: m.group(1) + m.group(2) + go_ic() + '</a>', html)
for name, html in pages.items():
    (OUT / name).write_text(_setas(html), encoding='utf-8')
print(len(pages), 'páginas')
