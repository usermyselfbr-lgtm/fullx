# ═══════════════════ 02 · FORM + CALENDLY ═══════════════════
from _comum import *

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
