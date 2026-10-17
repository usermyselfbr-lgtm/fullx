# ═══════════════════ 04 · MENTORIA (VÍDEO + APLICAÇÃO + AGENDA) ═══════════════════
# Brief RMBC da mentoria: docs/landing-audit/paginas/05-aplicacao.md · diferenças de ângulo: 04-mentoria.md
from _comum import *

f4 = (step(1, 'Seu contato', 'Para o time falar com você se você for aprovado.', CONTATO())
      + step(2, 'Hoje, você é…', '', radios('perfil', PERFIL))
      + step(3, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses.', radios('faturamento', FATUR))
      + step(4, 'Se fizer sentido, qual sua situação para investir?', 'O investimento da mentoria fica entre R$2.500 e R$5.000.', radios('momento', MOMENTO)))
# Sem agenda configurada: a aprovação vira contato do time. Com Calendly, acrescente '<div data-calendly></div>' ao terceiro argumento.
done4 = OK('Você foi aprovado.', 'O time fala com você em até 24 horas úteis para marcar a conversa. Fique de olho no WhatsApp que você informou.')

DORES_04 = [('Atrair', 'O mês depende de indicação. Você anuncia para cliente e não para a própria agência.'),
            ('Filtrar', 'Lead chega, mas sem verba. A semana vai embora em call com curioso.'),
            ('Fechar', 'Só você vende. Sem roteiro e sem CRM, cada call é um chute.'),
            ('Sustentar', 'Cliente cancela em 3 meses. Boleto atrasa. Time demora para produzir.')]
dores4 = ''.join(f'<article class="card reveal"><span class="k">Vazamento no cano {t}</span><p style="margin-top:12px">{d}</p></article>' for t, d in DORES_04)

CANOS_04 = [('Atrair', 'Anúncio para a sua agência, com a mesma lógica que você já usa para os clientes. O próximo cliente deixa de depender de quem indica.'),
            ('Filtrar', 'Formulário que pontua cada resposta e uma nota de corte. Quem tem verba chega na call; o curioso para antes dela.'),
            ('Fechar', 'CRM com etapas, tarefas do SDR, WhatsApp dentro do CRM e roteiro de call. Outra pessoa consegue vender sem você em todas as calls.'),
            ('Sustentar', 'Régua de cobrança por WhatsApp e entrega com processo, para o boleto não atrasar e o time não aprender de boca.')]
canos4 = ''.join(f'<li><span class="n">{i}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(CANOS_04, 1))

FAQ_04 = [('Quanto custa a mentoria?', 'O investimento fica entre R$2.500 e R$5.000. O valor da sua implantação é apresentado na conversa, depois da aprovação.'),
          ('Já fiz curso de tráfego e de vendas. O que muda aqui?', 'Curso ensina a peça. Na mentoria você vê as peças ligadas na tela da nossa operação e monta a mesma ligação na sua agência. Seu problema não é conhecimento. É instalação.'),
          ('Meu nicho é diferente. Funciona?', 'O sistema é de captação, venda e cobrança da agência, não do cliente final. Serve para quem vende serviço recorrente, seja qual for o nicho que você atende.'),
          ('Não tenho tempo sobrando. Dá para encaixar?', 'Falta de tempo costuma ser o sintoma: triagem de lead, call e cobrança passam todas por você. A mentoria é individual, então o ritmo da implantação é combinado na conversa, a partir da sua semana real.'),
          ('E se eu não for aprovado?', 'Você fica sabendo assim que enviar e recebe o conteúdo gratuito para começar pelo cano que mais vaza. Quando o momento da agência mudar, pode aplicar de novo.'),
          ('O que acontece depois que eu envio?', 'As 4 respostas somam pontos. Se você passar da nota de corte, o time fala com você em até 24 horas úteis para marcar a conversa.')]

body = f'''{topbar('t6')}
<main>
<section class="sec hero glow">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Mentoria individual Full10X</span>
      <!-- ✏️ HEADLINE = mesmo hook do anúncio -->
      <h1>O sistema que roda a nossa agência, instalado na sua.</h1>
      <p class="lead">Anúncio, formulário que pontua o lead, CRM, roteiro de venda e cobrança, ligados entre si e montados com você na sua operação. Para donos de agência e gestores de tráfego que faturam de R$10 mil a R$80 mil por mês.</p>
      <div style="margin-top:30px">{VSL()}</div>
      {PROOF}
    </div>
    <div class="delayed wait" data-delay="60" data-hero-cta style="position:sticky;top:90px">
      {form_card('vsl-form-calendly', 'Aplicação · 4 perguntas', f4, 'Enviar aplicação', done4, NOK(), corte=8, evento='SubmitApplication')}
    </div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Toda agência vaza em pelo menos um cano</h2><p class="lead">A agência não trava por falta de técnica. Trava porque vende, cobra e opera na mão do dono. Veja onde o dinheiro escapa na sua.</p></div>
    <div class="grid g2" style="max-width:900px;margin:0 auto">{dores4}</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="head center reveal"><h2>O que a mentoria instala, na ordem em que o dinheiro passa</h2><p class="lead">Atrair, Filtrar, Fechar e Sustentar. Cada cano liga no seguinte: o lead que o anúncio traz é pontuado, cai no CRM, segue o roteiro de venda e entra na régua de cobrança.</p></div>
    <ol class="steps reveal" style="max-width:780px;margin:0 auto">{canos4}</ol>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head reveal">
      <h2>Você vê a tela, não a teoria</h2>
      <p class="lead">Sou o Julio, founder da Full10X. Opero agência com tráfego, comercial e cobrança próprios. O CRM, o formulário que pontua o lead e o sistema de cobrança que você vai ver foram construídos para a minha operação. Eu mostro o que roda, não o que li.</p>
    </div>
    <div class="stats reveal" style="max-width:1000px">
      <div><b>+R$10 milhões</b><span>em tráfego gerenciado</span></div>
      <div><b>+2.300</b><span>clientes de serviço gerados</span></div>
      <div><b>+R$100 mil</b><span>a primeira agência passou de R$100 mil em 90 dias</span></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="head center reveal"><h2>Como funciona</h2></div>
    <div class="grid g3">
      <article class="card reveal"><span class="ico">{ic("check")}</span><h3>1. Responda 4 perguntas</h3><p>Cada resposta vale pontos, como no formulário que você vai instalar. Leva um minuto.</p></article>
      <article class="card reveal"><span class="ico">{ic("whats")}</span><h3>2. O time fala com você</h3><p>Se você passar da nota de corte, recebe contato em até 24 horas úteis para marcar a conversa.</p></article>
      <article class="card reveal"><span class="ico">{ic("cal")}</span><h3>3. Conversa sobre a sua agência</h3><p>Olhamos onde a sua operação vaza e você vê como fica a implantação e o investimento antes de decidir.</p></article>
    </div>
    <div class="cta-row reveal" style="justify-content:center"><a class="btn btn-primary btn-m" href="#form" data-go="#form" data-pos="como-funciona">Responder as 4 perguntas</a></div>
  </div>
</section>
<section class="sec glow center"><div class="wrap"><div class="head center reveal"><h2>Perguntas frequentes</h2></div><div class="faq reveal">{faq(FAQ_04)}</div></div></section>
</main>
{footer('f6', full=False)}
{mbar('Aplicar para a mentoria')}'''
pages['04-vsl-form-calendly.html'] = page('Full10X · Mentoria individual', 'Mentoria individual Full10X: o sistema de anúncio, formulário que pontua, CRM, roteiro de venda e cobrança que roda na nossa agência, instalado na sua.', 'https://grupofull10x.com/mentoria', 'vsl-form-calendly', body,
  ",\n  VIDEO_URL:''   /* 🔗 embed do vídeo */,\n  CALENDLY_URL:'' /* 🔗 link do evento no Calendly */,\n  POS_AGENDAMENTO_URL:''")
