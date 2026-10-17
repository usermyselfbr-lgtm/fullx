# ═══════════════════ 02 · CALL DE DIAGNÓSTICO (form 3 passos + agenda opcional) ═══════════════════
from _comum import *

f2 = (step(1, 'Para onde mandamos a confirmação?', 'É por este WhatsApp que o time combina o horário.', CONTATO())
      + step(2, 'Hoje, você é…', 'Para a gente preparar a call certa.', radios('perfil', PERFIL))
      + step(3, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses. Fica só entre você e o time.', radios('faturamento', FATUR)))
# Funciona sem agenda (CALENDLY_URL vazio) e com agenda: a frase .cal-only e o widget só aparecem quando o Calendly carrega (classe .cal).
done2 = OK('Recebemos.', 'O time confirma o horário com você pelo WhatsApp em até 24 horas úteis. Enquanto isso, pense em qual dos 4 canos você acha que vaza. Na call, a gente confere.',
           '<p class="cal-only">Se preferir, escolha agora um horário na agenda abaixo.</p><div data-calendly></div>')
CAL_CSS = '<style>#form .cal-ph,#form .cal-only{display:none}#form .done:has(.cal) .cal-only{display:block;margin-top:14px}</style>'

CANOS = [('layers', 'Atrair', 'O mês depende de indicação. Você anuncia para cliente e não para a própria agência.'),
         ('shield', 'Filtrar', 'Lead chega, mas sem verba. A semana vai embora em call com curioso.'),
         ('chat', 'Fechar', 'Só você vende. Sem roteiro e sem CRM, cada call é um chute.'),
         ('pay', 'Sustentar', 'Cliente cancela em 3 meses. Boleto atrasa e você cobra no braço.')]
canos = ''.join(f'<article class="card reveal"><span class="ico">{ic(i)}</span><h3>{t}</h3><p>{p}</p></article>' for i, t, p in CANOS)

FAQ_02 = [('A call é venda disfarçada?', 'A call é um diagnóstico da sua agência. No final, se o seu caso pedir acompanhamento, apresentamos a mentoria individual Full10X, com investimento entre R$2.500 e R$5.000. Fica quem quiser. Quem não quiser sai com o gargalo nomeado e a ação do mesmo jeito.'),
          ('Quanto custa?', 'Nada. A call é gratuita e sem compromisso.'),
          ('Quem atende?', 'O time da Full10X, que roda a própria agência com o CRM e o sistema de cobrança que construímos para ela. A conversa parte do que funciona aqui, na tela.'),
          ('Preciso ter números em mãos?', 'Planilha não. Ajuda saber de cabeça quanto a agência fatura, quantos clientes ativos tem e de onde veio o último cliente. O resto levantamos na conversa.'),
          ('E se eu não me encaixar?', 'O próximo passo aparece assim que você envia. Se a call ainda não fizer sentido para o seu momento, indicamos o playbook gratuito para você começar hoje.'),
          ('Como eu marco o horário?', 'Depois de enviar, o time confirma o horário com você pelo WhatsApp em até 24 horas úteis.'),
          ('Meu nicho é diferente. Serve?', 'O diagnóstico olha captação, comercial e operação de agência. Serve para quem vende serviço recorrente, seja qual for o nicho do cliente.')]

body = f'''{topbar('t4')}
<main>
<section class="sec hero glow">
  <div class="wrap split">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Call de diagnóstico · 30 minutos · gratuita</span>
      <h1>Descubra em 30 minutos onde sua agência perde venda.</h1>
      <p class="lead">No anúncio, no filtro, na call ou no boleto. Numa call gratuita com o time da Full10X, olhamos a sua operação pelos 4 canos que rodam na nossa agência e você sai com o gargalo nomeado e uma ação para a semana.</p>
      <ul class="steps" style="margin-top:32px">
        <li><span class="n">1</span><div><h3>Responda 3 perguntas</h3><p>Para a call começar pelo seu caso, não pelo básico.</p></div></li>
        <li><span class="n">2</span><div><h3>Marque o horário</h3><p>O time confirma com você pelo WhatsApp em até 24 horas úteis.</p></div></li>
        <li><span class="n">3</span><div><h3>Faça a call</h3><p>30 minutos com o time, cano por cano.</p></div></li>
      </ul>
      {PROOF}
    </div>
    <div data-hero-cta>{CAL_CSS}{form_card('form-calendly', 'Peça sua call', f2, 'Pedir minha call', done2, NOK().replace('Recebemos sua aplicação.', 'Recebemos seu pedido.'), corte=3, evento='Lead')}</div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Toda agência vaza em pelo menos um cano.</h2><p class="lead">Quatro canos, na ordem em que o dinheiro passa. Na call, descobrimos qual deles trava o seu faturamento primeiro.</p></div>
    <div class="grid g4">{canos}</div>
  </div>
</section>
<section class="sec glow">
  <div class="wrap split">
    <div class="head reveal"><h2>Como são os 30 minutos.</h2><p class="lead">Se o seu caso pedir acompanhamento, no final apresentamos a mentoria individual Full10X. Fica quem quiser. Quem não quiser sai com o diagnóstico do mesmo jeito.</p></div>
    <ul class="steps reveal">
      <li><span class="n">1</span><div><h3>Suas respostas, lidas antes</h3><p>A call começa no seu faturamento e no seu perfil, não em apresentação.</p></div></li>
      <li><span class="n">2</span><div><h3>Os 4 canos, um por um</h3><p>De onde vem o lead, como ele é filtrado, quem vende e como o cliente paga. Comparando com o que roda na nossa operação.</p></div></li>
      <li><span class="n">3</span><div><h3>O gargalo com nome</h3><p>Qual cano vaza primeiro e por que mexer nos outros agora não resolve.</p></div></li>
      <li><span class="n">4</span><div><h3>Uma ação para a semana</h3><p>Algo que você aplica em dias, com ou sem a Full10X.</p></div></li>
    </ul>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>O que você leva da call.</h2></div>
    <div class="grid g3">
      <article class="card reveal"><span class="ico">{ic("layers")}</span><h3>Mapa do gargalo</h3><p>Em qual dos 4 canos a sua agência vaza: Atrair, Filtrar, Fechar ou Sustentar.</p></article>
      <article class="card reveal"><span class="ico">{ic("crm")}</span><h3>O que medir</h3><p>Os números para acompanhar no cano que vaza. São os que acompanhamos na nossa operação, do lead que entra à venda fechada.</p></article>
      <article class="card reveal"><span class="ico">{ic("check")}</span><h3>Próximo passo</h3><p>Uma ação para aplicar na mesma semana, com ou sem a Full10X.</p></article>
    </div>
    <div class="head center reveal" style="margin-top:clamp(64px,8vw,112px)"><h2>Para quem é a call.</h2></div>
    <div class="compare" style="max-width:900px;margin:0 auto">
      <div class="no reveal"><h3>Ainda não é para você se</h3><ul><li>Ainda não tem nenhum cliente. Comece pelo playbook gratuito.</li><li>Procura fórmula pronta sem mexer na operação.</li><li>Trabalha em uma agência e não decide.</li></ul></div>
      <div class="yes reveal"><h3>É para você se</h3><ul><li>Tem agência ou carteira própria de clientes como gestor de tráfego.</li><li>Fatura entre R$10 mil e R$80 mil por mês.</li><li>Quer saber onde agir antes de gastar mais em tráfego ou em curso.</li></ul></div>
    </div>
  </div>
</section>
<section class="sec glow"><div class="wrap"><div class="head center reveal"><h2>Perguntas frequentes</h2></div><div class="faq reveal">{faq(FAQ_02)}</div></div></section>
<section class="sec"><div class="wrap">{cta_panel('c2', 'Descubra qual cano vaza primeiro.', 'Três perguntas, 30 minutos de call, sem custo. Você sai com o gargalo nomeado e uma ação para a semana.', [('Marcar minha call', '#form', 'btn-primary')]).replace('href="#form"', 'href="#form" data-go="#form" data-pos="final"')}</div></section>
</main>
{footer('f4', full=False)}
{mbar('Marcar minha call')}'''
pages['02-form-calendly.html'] = page('Full10X · Call de diagnóstico gratuita para agências', 'Call gratuita de 30 minutos com o time da Full10X: descubra em qual dos 4 canos (Atrair, Filtrar, Fechar, Sustentar) sua agência perde venda.', 'https://grupofull10x.com/diagnostico', 'form-calendly', body,
  ",\n  CALENDLY_URL:''         /* 🔗 link do seu evento: https://calendly.com/seu-usuario/diagnostico (vazio = o time confirma pelo WhatsApp) */,\n  POS_AGENDAMENTO_URL:''   /* opcional: página de obrigado depois de agendar */")
