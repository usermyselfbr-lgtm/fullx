# ═══════════════════ 05 · APLICAÇÃO ═══════════════════
from _comum import *

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
