# ═══════════════════ 05 · APLICAÇÃO ═══════════════════
# Destino do botão "Falar com o time". Brief RMBC da mentoria: docs/landing-audit/paginas/05-aplicacao.md
from _comum import *

f5 = (step(1, 'Como você se chama?', 'Comece pelo fácil.', inp('nome', 'Seu nome', auto='given-name', err='Escreva seu nome.'))
      + step(2, 'Para onde mandamos a resposta?', 'A resposta chega no WhatsApp em até 48 horas úteis.', inp('email', 'E-mail', 'email', 'voce@agencia.com', auto='email', err='Confira o e-mail.') + inp('whatsapp', 'WhatsApp com DDD', 'tel', '(11) 91234-5678', auto='tel-national', err='Confira o WhatsApp: DDD + número.') + inp('instagram', 'Instagram da agência', ph='@suaagencia', opt=True))
      + step(3, 'Hoje, você é…', '', radios('perfil', PERFIL))
      + step(4, 'Quanto sua agência fatura por mês?', 'Média dos últimos 3 meses.', radios('faturamento', FATUR))
      + step(5, 'Quantas pessoas trabalham com você?', 'Contando você.', radios('time', [('solo', 'Só eu', 0), ('2-3', '2 a 3 pessoas', 1), ('4-8', '4 a 8 pessoas', 2), ('9+', '9 ou mais', 2)]))
      + step(6, 'Onde sua agência mais vaza hoje?', 'Escolha um. É por ele que a conversa começa.', radios('gargalo', GARG))
      + step(7, 'Se for aprovado, qual sua situação para investir?', 'O investimento da mentoria fica entre R$2.500 e R$5.000.', radios('momento', MOMENTO))
      + step(8, 'Por que agora?', 'Em 2 linhas: onde a agência está hoje e onde você quer chegar.', inp('motivo', 'Sua resposta', 'textarea', 'Ex.: tenho 8 clientes, fecho por indicação e quero chegar a R$30 mil/mês.', err='Conte em uma ou duas frases o seu momento.', mn=10)))

FAQ_05 = [('Quanto custa a mentoria?', 'O investimento fica entre R$2.500 e R$5.000. O valor da sua implantação é apresentado na conversa, depois da aprovação.'),
          ('Já fiz curso de tráfego e de vendas. O que muda aqui?', 'Curso ensina a peça. Aqui você vê as peças ligadas na tela da nossa operação (anúncio, formulário que pontua, CRM, roteiro de venda e cobrança) e monta a mesma ligação na sua agência. Seu problema não é conhecimento. É instalação.'),
          ('Meu nicho é diferente. Funciona?', 'O sistema é de captação, venda e cobrança da agência, não do cliente final. Serve para quem vende serviço recorrente, seja qual for o nicho que você atende.'),
          ('Não tenho tempo sobrando. Dá para encaixar?', 'Falta de tempo costuma ser o sintoma: triagem de lead, call e cobrança passam todas por você. A mentoria é individual, então o ritmo da implantação é combinado na conversa, a partir da sua semana real.'),
          ('E se eu não for aprovado?', 'Você fica sabendo assim que enviar e recebe o conteúdo gratuito para começar pelo cano que mais vaza. Quando o momento da agência mudar, pode aplicar de novo.'),
          ('Por que tem aplicação em vez de um botão de compra?', 'Porque a mentoria é individual e parte da sua operação. As 8 perguntas mostram, antes da conversa, quantos clientes você tem, quem vende e onde o dinheiro escapa. Aprovamos quem conseguimos ajudar de verdade.')]

CANOS_05 = [('Atrair', 'Anúncio para a sua agência, não só para os clientes. O mês para de depender de indicação.'),
            ('Filtrar', 'Formulário que pontua cada resposta. Quem tem verba chega na call; o curioso fica antes dela.'),
            ('Fechar', 'CRM com etapas, tarefas do SDR e roteiro de call. Outra pessoa consegue vender além de você.'),
            ('Sustentar', 'Régua de cobrança por WhatsApp e entrega com processo, para o boleto não atrasar e o cliente não sair no 3º mês.')]
canos5 = ''.join(f'<article class="card reveal"><span class="k">Cano {i}</span><h3>{t}</h3><p>{d}</p></article>' for i, (t, d) in enumerate(CANOS_05, 1))

body = f'''{topbar('t7')}
<main>
<section class="sec hero glow">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Mentoria individual Full10X</span>
      <h1>Antes de falar com o time, mostre onde sua agência vaza.</h1>
      <p class="lead">São 8 perguntas sobre a sua operação. Lemos cada aplicação e respondemos no WhatsApp em até 48 horas úteis. Se fizer sentido, a conversa já começa pelo seu gargalo.</p>
      {PROOF}
    </div>
    <div data-hero-cta>{form_card('aplicacao', 'Aplicação · 8 perguntas', f5, 'Enviar aplicação', OK('Aplicação enviada.', 'Vamos ler suas respostas e falar com você no WhatsApp em até 48 horas úteis. Fique de olho no número que você informou.'), NOK(), corte=9, evento='SubmitApplication')}
      <div class="card" style="margin-top:20px"><h3>Você está usando o filtro agora</h3><p>Cada resposta deste formulário vale pontos, e a aplicação passa por uma nota de corte. É o cano Filtrar, o mesmo que a mentoria instala na sua agência para separar quem tem verba de quem é curioso, antes de gastar uma call.</p></div></div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Quem é aprovado</h2><p class="lead">A mentoria é individual e parte da operação que você já tem. Por isso o critério é o momento da agência, não a vontade.</p></div>
    <div class="compare" style="max-width:900px;margin:0 auto">
      <div class="no reveal"><h3>Não é para você se</h3><ul><li>Ainda não tem cliente pagando todo mês.</li><li>Quer uma fórmula para assistir, sem mexer na operação.</li><li>Procura alguém para rodar o tráfego dos seus clientes no seu lugar.</li><li>Não consegue investir nos próximos 60 dias.</li></ul></div>
      <div class="yes reveal"><h3>É para você se</h3><ul><li>É dono de agência ou gestor de tráfego com clientes, entre R$10 mil e R$80 mil por mês.</li><li>Anuncia todo dia para o cliente e o seu mês ainda fecha na indicação.</li><li>Perde a semana em call com quem não tem verba.</li><li>Quer que a venda e a cobrança parem de passar só por você.</li></ul></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="head center reveal"><h2>O que a mentoria instala, na ordem em que o dinheiro passa</h2><p class="lead">Quatro canos: Atrair, Filtrar, Fechar e Sustentar. Toda agência vaza em pelo menos um. Tudo roda primeiro na nossa operação, com CRM e cobrança construídos para ela. Você vê a tela, não a teoria.</p></div>
    <div class="grid g2" style="max-width:900px;margin:0 auto">{canos5}</div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Perguntas antes de aplicar</h2></div>
    <div class="faq reveal" style="max-width:760px;margin:0 auto">{faq(FAQ_05)}</div>
    <div class="cta-row reveal" style="justify-content:center"><a class="btn btn-primary btn-m" href="#form" data-go="#form" data-pos="fim-da-pagina">Responder as 8 perguntas</a></div>
  </div>
</section>
</main>
{footer('f7', full=False)}
{mbar('Enviar minha aplicação')}'''
pages['05-aplicacao.html'] = page('Full10X · Aplicação para a mentoria individual', 'Aplique para a mentoria individual Full10X: 8 perguntas sobre a sua agência e resposta no WhatsApp em até 48 horas úteis.', 'https://grupofull10x.com/aplicacao', 'aplicacao', body)
