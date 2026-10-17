# Helpers, dados e componentes compartilhados entre as páginas (texto de cada página em paginas/)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _sistema import *
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
    <div class="done" data-done="fail" hidden><h3>Não conseguimos registrar.</h3><p>A conexão falhou. Suas respostas continuam aqui: tente de novo em alguns segundos.</p><button type="button" class="btn btn-primary on-light" data-retry>Tentar de novo</button><a class="btn btn-ghost" style="width:100%;margin-top:10px" data-wa href="#" target="_blank" rel="noopener noreferrer" hidden>{ic("whats")}Ou fale pelo WhatsApp</a></div>
  </form>
</div>'''

OK = lambda t, p, extra='': f'<div class="ok">{ic("check")}</div><h3>{t}</h3><p>{p}</p>{extra}'
NOK = lambda: f'<div class="done" data-done="nok" hidden><div class="ok">{ic("check")}</div><h3>Recebemos sua aplicação.</h3><p>Pelo seu momento, o melhor próximo passo é o conteúdo gratuito. Separamos o playbook para você começar hoje.</p><a class="btn btn-primary on-light" href="06-playbook-ebook.html">Baixar o playbook grátis</a></div>'

PROOF = f'<div class="proof-line"><span>{ic("check")}+R$10 milhões em tráfego gerenciado</span><span>{ic("check")}+2.300 clientes de serviço gerados</span><span>{ic("check")}CRM e cobrança próprios, rodando na nossa agência</span></div>'

def mbar(label, go='#form'):
    return f'<div class="mbar"><a class="btn btn-primary" href="{go}" data-go="{go}" data-pos="barra-celular">{label}</a></div>'

FAQ_BASE = [('Para quem é?', 'Para donos de agência e gestores de tráfego que já têm clientes pagando e querem parar de recomeçar o mês do zero.'),
            ('Isso é curso?', 'Não. É o sistema que roda na nossa própria agência: anúncio, formulário que pontua o lead, CRM, roteiro de venda e cobrança, ligados entre si. Você vê a tela, não a teoria.'),
            ('E se o meu nicho for diferente?', 'O sistema é de captação, comercial e operação de agência. Serve para quem vende serviço recorrente, seja qual for o nicho do cliente.'),
            ('Por que a Full10X?', 'Porque tudo o que mostramos roda primeiro na nossa operação, com +R$10 milhões gerenciados em tráfego e CRM e cobrança construídos para ela.'),
            ('Como eu começo?', 'Preencha o formulário desta página. O próximo passo aparece na hora, de acordo com as suas respostas.')]

pages = {}

# ───────────── blocos usados por mais de uma página ─────────────
SOFT = [('crm', 'CRM', 'Pipeline comercial de agência, com etapas, tarefas e histórico de cada lead.', ['Funil visual por etapa', 'Formulário que pontua o lead', 'Tarefas e follow-up do SDR']),
        ('pay', 'Gateway de pagamento', 'Cobrança recorrente com régua automática para o boleto não atrasar.', ['Pix, boleto e cartão recorrente', 'Régua de cobrança por WhatsApp', 'Painel de inadimplência']),
        ('ops', 'IA operacional', 'Treina e orienta o time de entrega com os processos da sua agência.', ['Responde dúvidas do time 24h', 'Base de processos e checklists', 'Onboarding de novo colaborador']),
        ('chat', 'IA comercial', 'Qualifica, responde e agenda leads no WhatsApp enquanto o time dorme.', ['Primeiro contato em segundos', 'Qualificação por perguntas', 'Agendamento direto na agenda'])]
soft_cards = bento(SOFT)

# (categoria, selo, título, descrição, meta, link). Só conteúdo que existe. O artigo fica por último: a página dele mostra os 3 primeiros em "Continue lendo".
POSTS = [('aulas', 'Aula ao vivo', 'Os 4 canos da agência, abertos na tela', 'Anúncio, formulário que pontua, CRM, roteiro e cobrança, na operação real. Gratuita, no Google Meet.', '25/10 · 14h', 'https://www.fullxmarketing.com/'),
         ('playbooks', 'Playbook', 'Playbook Full10X: mais clientes e receita', 'Da oferta ao cliente que renova, com plano de 6 semanas para implantar.', 'PDF · 147 páginas', '06-playbook-ebook.html'),
         ('aulas', 'Aulas gratuitas', 'O sistema Full10X em 5 aulas curtas', 'Em gravação. Cadastre-se e receba cada aula quando ela sair.', 'Cadastro gratuito', '07-playbook-curso.html'),
         ('artigos', 'Artigo', 'Os 4 funis que enchem a agenda comercial de uma agência', 'Atrair, filtrar, fechar e sustentar, com a tabela de pontuação do formulário.', '7 min de leitura', '01c-blog-artigo.html')]
TH_ART = {'aulas': lambda: f'<span class="th-play">{ic("play")}</span>',
          'playbooks': lambda: '<span class="th-doc"><i></i><i></i><i></i><i></i><i></i><i></i></span>',
          'artigos': lambda: '<span class="th-lines"><i></i><i></i><i></i><i></i></span>'}
TH_IC = {'aulas': 'video', 'playbooks': 'file', 'artigos': 'clock'}
def post_cards(n=6, uid='p'):
    # 🖼️ MÍDIA: para usar capa real, troque o conteúdo de <div class="th"> por <img src="..." alt="" width="640" height="360">
    return ''.join(f'''<a class="post reveal" href="{href}" data-cat="{c}"><div class="th"><span class="t">{tag}</span>{TH_ART[c]()}{mark(f"{uid}{i}", size=26)}</div>
<div class="bd"><h3>{t}</h3><p>{d}</p><span class="meta"><span>{ic(TH_IC[c])}{m}</span><span class="go">{ic("arrow")}</span></span></div></a>''' for i, (c, tag, t, d, m, href) in enumerate(POSTS[:n]))
VSL = lambda key='VIDEO_URL': f'''<div class="video" data-embed-key="{key}"><div class="ph"><span class="play">{ic("play")}</span><span>🖼️ Vídeo de vendas. Configure {key} no topo do arquivo.</span></div></div>'''
