# ═══════════════════ 07 · AULAS GRATUITAS (isca) ═══════════════════
# Não existe curso gravado: a página capta cadastro para receber as 5 aulas quando forem publicadas
# e faz ponte para a aula ao vivo de 25/10 (fullxmarketing.com). Decisão registrada em docs/landing-audit/paginas/07-curso.md.
from _comum import *

AULA_VIVO = 'https://www.fullxmarketing.com/'
f7 = step(1, 'Receba a aula 1 quando ela sair', '', CONTATO())
done7 = OK('Cadastro feito.', 'A aula 1 chega no seu e-mail assim que for publicada.',
           f'<a class="btn btn-primary on-light" href="{AULA_VIVO}" target="_blank" rel="noopener">Enquanto isso, garanta sua vaga na aula ao vivo de 25/10</a>')

mods = [('Atrair', 'O anúncio para a própria agência e os 4 funis de captação, para o mês não depender de indicação.'),
        ('Filtrar', 'O formulário que pontua o lead e a nota de corte que separa verba de curioso antes da call.'),
        ('Fechar', 'O roteiro de call e o CRM: pipeline, tarefas do SDR e WhatsApp dentro do CRM, para outra pessoa vender além de você.'),
        ('Sustentar', 'A régua de cobrança por WhatsApp e o que segura o cliente depois do terceiro mês.'),
        ('Escalar', 'IA na operação: a base de processos que responde o time, que estamos construindo na nossa agência.')]
mod_html = ''.join(f'<li><span class="n">{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(mods))

dores = [('Atrair', 'O mês depende de indicação.', 'Você anuncia para cliente e não para a própria agência.'),
         ('Filtrar', 'Lead chega, mas sem verba.', 'A semana vai embora em call com curioso.'),
         ('Fechar', 'Só você vende.', 'Sem roteiro e sem CRM, cada call é um chute.'),
         ('Sustentar', 'O boleto atrasa.', 'Cliente cancela em 3 meses e o mês recomeça do zero.')]
dor_html = ''.join(f'<article class="card reveal"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p></article>' for k, t, d in dores)

FAQ_07 = [('Quando sai a aula 1?', 'Ainda não tem data fechada. As aulas vão ser gravadas a partir do conteúdo da aula ao vivo de 25/10. Quem se cadastra aqui recebe cada uma por e-mail e WhatsApp assim que ela for publicada.'),
          ('Quanto custa?', 'Nada. As 5 aulas são gratuitas e o cadastro não pede cartão.'),
          ('É a mesma coisa da aula ao vivo?', 'É o mesmo sistema, separado em 5 aulas curtas, uma por etapa. A aula ao vivo é no domingo, 25/10, às 14h (Brasília), no Google Meet, com perguntas no final. A gravação da aula ao vivo fica só para quem se inscreveu nela.'),
          ('Serve para o meu nicho?', 'O sistema é de captação, comercial e cobrança de agência. Serve para quem vende serviço recorrente, seja qual for o nicho do cliente.'),
          ('Vão tentar me vender alguma coisa?', 'As aulas não dependem de compra. Para quem quiser implantar com acompanhamento existe a mentoria individual Full10X, com investimento entre R$2.500 e R$5.000.')]

body = f'''{topbar('t9')}
<main>
<section class="sec hero glow center">
  <div class="wrap">
    <span class="eyebrow"><i aria-hidden="true"></i>Aulas gratuitas Full10X · 5 aulas curtas</span>
    <h1 style="max-width:22ch;margin-inline:auto">O sistema Full10X em 5 aulas curtas, na ordem em que o dinheiro passa.</h1>
    <p class="lead" style="max-width:60ch;margin-inline:auto">Uma aula para cada etapa: Atrair, Filtrar, Fechar, Sustentar e Escalar. As aulas vão ser gravadas a partir do conteúdo da aula ao vivo de 25/10. Cadastre-se e cada uma chega no seu e-mail e WhatsApp assim que for publicada.</p>
    <div class="vsl-wrap">{VSL('TRAILER_URL')}</div>
    <div style="max-width:480px;margin:36px auto 0;text-align:left" data-hero-cta>{form_card('playbook-curso', 'Cadastro gratuito', f7, 'Quero receber a aula 1', done7, evento='CompleteRegistration')}</div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Toda agência vaza em pelo menos um cano.</h2><p class="lead" style="margin-top:16px">Quatro vazamentos, quatro etapas do sistema. As 4 primeiras aulas abrem um cano cada.</p></div>
    <div class="grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px">{dor_html}</div>
    <p class="lead reveal" style="text-align:center;margin:36px auto 0;max-width:none">Seu problema não é conhecimento. É instalação.</p>
  </div>
</section>
<section class="sec">
  <div class="wrap split" style="align-items:start">
    <div class="reveal"><h2>As 5 aulas.</h2><p class="lead" style="margin-top:16px">Um cano por aula, na ordem em que o dinheiro passa. Você vê a tela da nossa operação, não a teoria.</p>
      <div class="card" style="margin-top:28px"><h3>Como as aulas chegam</h3><p>Você se cadastra. Quando a aula 1 for publicada, o link chega no seu e-mail e no WhatsApp. As outras 4 seguem na mesma ordem.</p></div></div>
    <ol class="steps reveal">{mod_html}</ol>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Para quem são estas aulas.</h2></div>
    <div class="compare" style="max-width:900px;margin:0 auto">
      <div class="no reveal"><h3>Não é para você se</h3><ul><li>Ainda não tem nenhum cliente.</li><li>Procura fórmula sem implementar.</li><li>Quer só aula de configuração de anúncio.</li></ul></div>
      <div class="yes reveal"><h3>É para você se</h3><ul><li>Tem agência ou carteira de clientes própria.</li><li>Já anuncia e o mês ainda fecha na indicação.</li><li>Quer ver como captação, venda e cobrança se ligam.</li></ul></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    <div class="head center reveal"><h2>Quem dá as aulas.</h2>
      <p class="lead" style="margin-top:16px;max-width:62ch;margin-inline:auto">Sou o Julio, founder da Full10X. Opero agência com tráfego, comercial e cobrança próprios. O CRM, o formulário que pontua o lead e o sistema de cobrança que você vai ver foram construídos para a minha operação.</p></div>
    <div class="reveal" style="display:flex;justify-content:center">{PROOF}</div>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Não quer esperar? A aula ao vivo é domingo, 25/10.</h2>
      <p class="lead" style="margin-top:16px;max-width:60ch;margin-inline:auto">Às 14h (Brasília), no Google Meet, com perguntas no final. Gratuita, com 100 lugares, que é o limite da sala. O link chega pelo WhatsApp.</p></div>
    <div class="cta-row reveal" style="justify-content:center"><a class="btn btn-primary btn-m" href="{AULA_VIVO}" target="_blank" rel="noopener" data-pos="aula-ao-vivo">Garantir minha vaga na aula ao vivo</a></div>
  </div>
</section>
<section class="sec glow center"><div class="wrap"><div class="head center reveal"><h2>Perguntas frequentes</h2></div><div class="faq reveal" style="margin-inline:auto;text-align:left">{faq(FAQ_07)}</div></div></section>
<section class="sec"><div class="wrap">{cta_panel('c7', 'Daqui a 90 dias, sua agência vai depender de quem?', 'Cadastre-se agora e a aula 1 chega no seu e-mail e WhatsApp assim que sair. Grátis.', [('Quero receber a aula 1', '#form', 'btn-primary')]).replace('href="#form"', 'href="#form" data-go="#form" data-pos="final"')}</div></section>
</main>
{footer('f9', full=False)}
{mbar('Receber a aula 1')}'''
pages['07-playbook-curso.html'] = page('Full10X · Aulas gratuitas: o sistema em 5 aulas curtas', 'Cadastre-se e receba a aula 1 do sistema Full10X: Atrair, Filtrar, Fechar, Sustentar e Escalar, em 5 aulas curtas e gratuitas.', 'https://grupofull10x.com/curso', 'playbook-curso', body,
  ",\n  TRAILER_URL:'' /* 🔗 embed do vídeo de apresentação (vazio = player escondido) */")
