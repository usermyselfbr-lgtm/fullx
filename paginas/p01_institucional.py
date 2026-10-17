# ═══════════════════ 01 · INSTITUCIONAL ═══════════════════
from _comum import *

# Cartões locais: só CRM e cobrança aparecem como em uso; IA operacional em construção; IA comercial no roadmap.
# Sugestão registrada em docs/landing-audit/paginas/01-institucional.md para levar ao SOFT de _comum.py.
SOFT_01 = [('crm', 'CRM', 'Em uso na nossa agência. Pipeline com etapas, tarefas e histórico de cada lead, do primeiro contato ao contrato.', ['Funil visual por etapa', 'Formulário que pontua o lead', 'WhatsApp dentro do CRM']),
           ('pay', 'Sistema de cobrança', 'Em uso na nossa agência. Régua de cobrança por WhatsApp para o boleto não depender de você lembrar.', ['Régua por WhatsApp', 'Integração com o Asaas']),
           ('ops', 'IA operacional', 'O que estamos construindo. Uma base com os processos da agência que responde as dúvidas do time de entrega.', ['Base de processos', 'Respostas para o time', 'Protótipo em teste']),
           ('chat', 'IA comercial', 'No roadmap, ainda não disponível. Hoje o filtro é o formulário que pontua e o lead cai no WhatsApp do comercial.', ['No roadmap'])]

CANOS = [('Atrair', 'O mês depende de indicação. Você anuncia para cliente e não para a própria agência.', 'Anúncio e funil de captação da agência'),
         ('Filtrar', 'Lead chega sem verba. A semana vai embora em call com curioso.', 'Formulário que pontua o lead e nota de corte antes da call'),
         ('Fechar', 'Só você vende. Sem roteiro e sem CRM, cada call é um chute.', 'CRM com etapas, tarefas do SDR e roteiro de venda'),
         ('Sustentar', 'Cliente cancela em 3 meses. Boleto atrasa.', 'Régua de cobrança por WhatsApp e entrega com processo escrito')]
canos = ''.join(f'<article class="card reveal float"><span class="k">Cano {n}</span><h3>{t}</h3><p>{s}</p><ul><li>{i}</li></ul></article>' for n, (t, s, i) in enumerate(CANOS, 1))

PASSOS = [('users', 'Mentoria individual', 'Você fatura de R$10 mil a R$80 mil por mês e quer os quatro canos instalados com acompanhamento.', 'Aplicar para a mentoria', '05-aplicacao.html'),
          ('search', 'Diagnóstico', 'Você quer saber em qual cano a agência vaza antes de decidir qualquer investimento.', 'Agendar o diagnóstico', '02-form-calendly.html'),
          ('file', 'Playbook gratuito', 'Você quer começar sozinho, hoje, sem investir nada.', 'Baixar o playbook', '06-playbook-ebook.html'),
          ('layers', 'White label', 'Você quer oferecer o CRM com a sua marca. Ainda não está aberto: a lista de espera recebe a novidade primeiro.', 'Entrar na lista de espera', '09-software-whitelabel.html')]
passos = ''.join(f'<a class="card reveal" href="{h}"><span class="ico">{ic(i)}</span><h3>{t}</h3><p>{d}</p><span class="more">{c} {ic("arrow")}</span></a>' for i, t, d, c, h in PASSOS)

FAQ_01 = [('A Full10X vende software ou mentoria?', 'Hoje, mentoria individual. O CRM e o sistema de cobrança são os que rodam na nossa agência e entram na implantação. A versão com a sua marca (white label) ainda não está aberta.'),
          ('Isso é curso?', 'Não. É a operação aberta: anúncio, formulário que pontua o lead, CRM, roteiro de venda e cobrança, ligados entre si. Você vê a tela, não a teoria.'),
          ('Quanto custa a mentoria?', 'O investimento fica entre R$2.500 e R$5.000. O valor exato sai depois da aplicação, quando a gente sabe em qual cano a sua agência vaza.'),
          ('Ainda não tenho verba para investir. Por onde começo?', 'Pelo playbook gratuito. Ele cobre o cano Filtrar: perguntas, pontuação e nota de corte para parar de gastar call com curioso.'),
          ('Meu nicho é diferente. Serve para mim?', 'O sistema é de captação, comercial e cobrança de agência. Serve para quem vende serviço recorrente, seja qual for o nicho do cliente.'),
          ('Quanto tempo leva para responderem a aplicação?', 'Respondemos todas as aplicações em até 48 horas úteis.')]

body = f'''{topbar('t1', ('Aplicar para a mentoria', '05-aplicacao.html'), nav=True)}
<main>
<section class="sec hero glow center">
  <div class="wrap">
    <span class="eyebrow"><i aria-hidden="true"></i>Sistema Full10X para donos de agência</span>
    <h1>O sistema que atrai, filtra, fecha e cobra cliente na sua agência.</h1>
    <p class="lead">Para dono de agência e gestor de tráfego com clientes, de R$10 mil a R$80 mil por mês, que cansou de recomeçar o mês do zero. Tudo o que instalamos roda primeiro na nossa operação.</p>
    <div class="cta-row" data-hero-cta>
      <a class="btn btn-primary btn-m" href="05-aplicacao.html" data-pos="hero">Aplicar para a mentoria</a>
      <a class="btn btn-ghost btn-m" href="#passo" data-go="#passo" data-pos="hero">Ver qual é o meu próximo passo</a>
    </div>
    {PROOF.replace('class="proof-line"','class="proof-line" style="justify-content:center"',1)}
    <!-- 🖼️ MÍDIA: interface desenhada em código. Para usar print real, troque <div class="app">…</div> por <img class="app" src="..." alt="Painel Full10X"> -->
    <div class="shot">{app_mock('hm')}</div>
  </div>
  <div class="wrap">{strip()}</div>
</section>

<section class="sec light" id="canos">
  <div class="wrap">
    <div class="head reveal"><h2>Toda agência vaza em pelo menos um cano.</h2><p class="lead">São quatro, na ordem em que o dinheiro passa: Atrair, Filtrar, Fechar e Sustentar. Estudar mais tráfego não fecha vazamento. Seu problema não é conhecimento. É instalação.</p></div>
    <div class="grid g4">{canos}</div>
    <p class="small reveal" style="margin-top:28px">Escalar com IA vem depois, quando os quatro canos já seguram o dinheiro.</p>
  </div>
</section>

<section class="sec light mist" id="passo">
  <div class="wrap">
    <div class="head center reveal"><h2>Escolha o próximo passo pelo seu momento.</h2><p class="lead">Nenhuma das quatro pede cartão.</p></div>
    <div class="grid g2">{passos}</div>
  </div>
</section>

<section class="sec glow" id="softwares">
  <div class="wrap">
    <div class="head center reveal"><span class="eyebrow"><i aria-hidden="true"></i>Software próprio</span><h2 style="margin-top:20px">O sistema roda em software que a gente usa.</h2><p class="lead">CRM e cobrança estão em uso na nossa agência hoje. A IA operacional é o que estamos construindo. A IA comercial está no roadmap.</p></div>
    {bento(SOFT_01, 'White label: lista de espera', '09-software-whitelabel.html')}
  </div>
</section>

<section class="sec light">
  <div class="wrap">
    <div class="split">
      <div class="reveal"><h2>Eu mostro o que roda, não o que li.</h2></div>
      <div class="reveal"><p class="lead">Sou o Julio, founder da Full10X. Opero agência com tráfego, comercial e cobrança próprios. O CRM, o formulário que pontua o lead e o sistema de cobrança foram construídos para a minha operação. Na mentoria e nos conteúdos, você vê a tela, não a teoria.</p></div>
    </div>
    <div class="stats reveal" style="margin-top:48px"><div><b>+R$10 mi</b><span>em tráfego gerenciado</span></div><div><b>+2.300</b><span>clientes de serviço gerados</span></div><div><b>R$100 mil</b><span>em 90 dias: a primeira agência passou disso</span></div></div>
  </div>
</section>

<section class="sec light mist">
  <div class="wrap split">
    <div class="reveal"><h2>Prefere instalar com alguém do lado?</h2><p class="lead" style="margin-top:18px">A mentoria Full10X é individual. A gente instala os quatro canos na sua agência, começando pelo que mais vaza.</p>
      <p class="small" style="margin-top:14px">Investimento entre R$2.500 e R$5.000. Respondemos todas as aplicações em até 48 horas úteis.</p>
      <div class="cta-row"><a class="btn btn-primary btn-m" href="05-aplicacao.html">Aplicar para a mentoria</a></div></div>
    <ol class="steps reveal">
      <li><span class="n">1</span><div><h3>Diagnóstico</h3><p>Em qual cano sua agência vaza: atrair, filtrar, fechar ou sustentar.</p></div></li>
      <li><span class="n">2</span><div><h3>Instalação</h3><p>Funil, formulário que pontua, CRM e régua de cobrança configurados para a sua operação.</p></div></li>
      <li><span class="n">3</span><div><h3>Acompanhamento</h3><p>Implantação acompanhada até o sistema entrar na rotina do time.</p></div></li>
    </ol>
  </div>
</section>

<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Comece pelo conteúdo gratuito.</h2><p class="lead">Material gratuito para aplicar sozinho, na ordem dos canos.</p></div>
    <div class="grid g3">{post_cards(3, 'i')}</div>
    <div class="cta-row reveal" style="justify-content:center"><a class="btn btn-primary btn-m" href="01b-blog.html">Ver os conteúdos</a></div>
  </div>
</section>

<section class="sec light mist">
  <div class="wrap">
    <div class="head center reveal"><h2>Perguntas de quem chega pela primeira vez.</h2></div>
    <div class="faq reveal" style="max-width:820px;margin:0 auto">{faq(FAQ_01)}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">{cta_panel('fc', 'Daqui a 90 dias, sua agência vai depender de quem?', 'Se você já tem cliente pagando, aplique para a mentoria. Se quer começar sozinho, baixe o playbook.', [('Aplicar para a mentoria', '05-aplicacao.html', 'btn-primary'), ('Baixar o playbook grátis', '06-playbook-ebook.html', 'btn-ghost')])}</div>
</section>
</main>
{footer('f1')}
{mbar('Escolher meu próximo passo', '#passo')}'''
pages['01-institucional.html'] = page('Full10X · Sistema para donos de agência', 'O sistema que atrai, filtra, fecha e cobra cliente na sua agência: mentoria individual, CRM e cobrança próprios, diagnóstico e playbook gratuito.', 'https://grupofull10x.com/', 'institucional', body)
