# ═══════════════════ 04 · VSL + FORM + CALENDLY ═══════════════════
from _comum import *

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
