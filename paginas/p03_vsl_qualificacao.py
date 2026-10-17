# ═══════════════════ 03 · VSL + QUALIFICAÇÃO ═══════════════════
from _comum import *

f3 = (step(1, 'Seu contato', 'Para o time falar com você.', CONTATO())
      + step(2, 'Hoje, você é…', '', radios('perfil', PERFIL))
      + step(3, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses.', radios('faturamento', FATUR))
      + step(4, 'Qual ponto mais pesa hoje?', 'Usamos isso para preparar a conversa.', radios('gargalo', GARG))
      + step(5, 'Se fizer sentido, qual sua situação para investir?', 'O investimento da mentoria fica entre <span class="todo">[R$X e R$Y]</span>.', radios('momento', MOMENTO)))
done3 = OK('Aplicação recebida.', 'Um especialista vai falar com você pelo WhatsApp em até 24 horas úteis.', '<a class="btn btn-primary on-light" data-wa href="#" target="_blank" rel="noopener">' + ic('whats') + 'Adiantar pelo WhatsApp</a>')
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
