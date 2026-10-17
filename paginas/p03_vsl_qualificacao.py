# ═══════════════════ 03 · ASSISTA (VÍDEO + QUALIFICAÇÃO) ═══════════════════
# Brief RMBC da mentoria: docs/landing-audit/paginas/05-aplicacao.md · diferenças de ângulo: 03-assista.md
from _comum import *

f3 = (step(1, 'Seu contato', 'Para o time falar com você.', CONTATO())
      + step(2, 'Hoje, você é…', '', radios('perfil', PERFIL))
      + step(3, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses.', radios('faturamento', FATUR))
      + step(4, 'Onde sua agência mais vaza hoje?', 'Usamos isso para preparar a conversa.', radios('gargalo', GARG))
      + step(5, 'Se fizer sentido, qual sua situação para investir?', 'O investimento da mentoria fica entre R$2.500 e R$5.000.', radios('momento', MOMENTO)))
done3 = OK('Aplicação recebida.', 'O time fala com você pelo WhatsApp em até 24 horas úteis, já com o cano que você marcou como ponto de partida.')

PONTOS_03 = [('Um filtro antes da call', 'Formulário que pontua cada resposta, com nota de corte. Quem tem verba chega na call; o curioso para antes dela e deixa de comer a sua semana.'),
             ('Um comercial que não depende só de você', 'CRM com etapas, tarefas do SDR, WhatsApp dentro do CRM e roteiro de call. Cada lead tem histórico e próximo passo, e outra pessoa consegue vender.'),
             ('Uma cobrança que não depende de lembrar', 'Régua de cobrança por WhatsApp, com o lembrete antes do vencimento e a cobrança depois dele. O boleto deixa de ser assunto seu.')]
pontos3 = ''.join(f'<li><span class="n">{i}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(PONTOS_03, 1))

FAQ_03 = [('Quanto custa a mentoria?', 'O investimento fica entre R$2.500 e R$5.000. O valor da sua implantação é apresentado na conversa, depois da aprovação.'),
          ('Já fiz curso de tráfego e de vendas. O que muda aqui?', 'Curso ensina a peça. Na mentoria você vê as peças ligadas na tela da nossa operação e monta a mesma ligação na sua agência. Seu problema não é conhecimento. É instalação.'),
          ('Meu nicho é diferente. Funciona?', 'O sistema é de captação, venda e cobrança da agência, não do cliente final. Serve para quem vende serviço recorrente, seja qual for o nicho que você atende.'),
          ('Não tenho tempo sobrando. Dá para encaixar?', 'Falta de tempo costuma ser o sintoma: triagem de lead, call e cobrança passam todas por você. A mentoria é individual, então o ritmo da implantação é combinado na conversa, a partir da sua semana real.'),
          ('E se eu não for aprovado?', 'Você fica sabendo assim que enviar e recebe o conteúdo gratuito para começar pelo cano que mais vaza. Quando o momento da agência mudar, pode aplicar de novo.'),
          ('Isso é curso?', 'Não. É a mentoria individual de implantação do sistema que roda na nossa agência: anúncio, formulário que pontua o lead, CRM, roteiro de venda e cobrança. Você vê a tela, não a teoria.')]

body = f'''{topbar('t5')}
<main>
<section class="sec hero glow center">
  <div class="wrap">
    <span class="eyebrow"><i aria-hidden="true"></i>Mentoria individual Full10X</span>
    <!-- ✏️ HEADLINE = mesmo hook do anúncio -->
    <h1 style="max-width:20ch">Sua agência anuncia todo dia e o mês ainda fecha na indicação?</h1>
    <p class="lead" style="margin:22px auto 0">Então o problema não é mais lead. É o que acontece depois que ele chega. Na mentoria individual Full10X você instala na sua agência o filtro, o CRM, o roteiro de venda e a cobrança que rodam na nossa.</p>
    <div class="vsl-wrap">{VSL()}</div>
    <!-- ⚙️ data-delay = segundos até liberar o formulário (use o momento da oferta no vídeo) -->
    <div class="delayed wait" data-delay="90" data-hero-cta style="max-width:560px;margin:40px auto 0;text-align:left">
      {form_card('vsl-qualificacao', 'Aplicação · 5 perguntas', f3, 'Enviar aplicação', done3, NOK(), corte=8, evento='SubmitApplication')}
    </div>
    {PROOF.replace('class="proof-line"', 'class="proof-line" style="justify-content:center"')}
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="head center reveal"><h2>O que o sistema instala na sua agência</h2><p class="lead">O anúncio continua trazendo gente. A diferença está nos três canos seguintes, na ordem em que o dinheiro passa: Filtrar, Fechar e Sustentar.</p></div>
    <ol class="steps reveal" style="max-width:780px;margin:0 auto">{pontos3}</ol>
    <p class="small reveal" style="max-width:780px;margin:34px auto 0">Tudo isso roda primeiro na nossa operação, com +R$10 milhões em tráfego gerenciado e CRM e cobrança construídos para ela.</p>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Para quem é</h2></div>
    <div class="compare" style="max-width:900px;margin:0 auto">
      <div class="no reveal"><h3>Não é para você se</h3><ul><li>Ainda não tem cliente pagando todo mês.</li><li>Quer uma fórmula para assistir, sem mexer na operação.</li><li>Não consegue investir nos próximos 60 dias.</li></ul></div>
      <div class="yes reveal"><h3>É para você se</h3><ul><li>Tem agência ou carteira de tráfego entre R$10 mil e R$80 mil por mês.</li><li>Perde a semana em call com quem não tem verba.</li><li>Quer que a venda e a cobrança parem de passar só por você.</li></ul></div>
    </div>
    <div class="cta-row reveal" style="justify-content:center"><a class="btn btn-primary btn-m" href="#form" data-go="#form" data-pos="para-quem-e">Responder as 5 perguntas</a></div>
  </div>
</section>
<section class="sec glow center"><div class="wrap"><div class="head center reveal"><h2>Perguntas frequentes</h2></div><div class="faq reveal">{faq(FAQ_03)}</div></div></section>
</main>
{footer('f5', full=False)}
{mbar('Aplicar para a mentoria')}'''
pages['03-vsl-qualificacao.html'] = page('Full10X · Mentoria: veja o sistema e aplique', 'Sua agência anuncia todo dia e o mês ainda fecha na indicação? Veja o sistema da mentoria individual Full10X e aplique em 5 perguntas.', 'https://grupofull10x.com/vsl', 'vsl-qualificacao', body,
  ",\n  VIDEO_URL:''   /* 🔗 URL de embed do vídeo: YouTube (https://www.youtube.com/embed/ID), Vimeo, Panda ou Vturb */")
