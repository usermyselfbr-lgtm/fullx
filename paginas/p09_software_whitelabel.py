# ═══════════════════ 09 · SOFTWARE WHITE LABEL ═══════════════════
from _comum import *

f9 = (step(1, 'Seu contato', '', CONTATO() + inp('empresa', 'Nome da agência ou empresa', err='Escreva o nome da empresa.'))
      + step(2, 'Quantos clientes você atende hoje?', 'Define o plano ideal.', radios('clientes', [('ate-10', 'Até 10', 1), ('11-30', '11 a 30', 2), ('31-100', '31 a 100', 3), ('100+', 'Mais de 100', 3)]))
      + step(3, 'Quais módulos interessam?', 'Pode escolher o principal agora.', radios('modulo', [('crm', 'CRM', 1), ('pagamento', 'Gateway de pagamento', 1), ('ia-op', 'IA operacional', 1), ('ia-com', 'IA comercial', 1), ('todos', 'Todos integrados', 2)])))
done9 = OK('Vamos montar sua demonstração.', 'Escolha o horário. Mostramos o painel com a sua marca.', '<div data-calendly></div>')
body = f'''{topbar('t10', ('Agendar demonstração', '#form', 'data-go="#form" data-pos="topo"'))}
<main>
<section class="sec hero glow">
  <div class="wrap split">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>White label para agências e consultorias</span>
      <h1>Seu próprio software de CRM, cobrança e IA. Com a sua marca.</h1>
      <p class="lead">Revenda para os seus clientes um sistema completo, com seu logo, suas cores e seu domínio. Nós cuidamos da tecnologia.</p>
      <div class="cta-row" data-hero-cta><a class="btn btn-primary btn-m" href="#form" data-go="#form" data-pos="hero">Agendar demonstração</a><a class="btn btn-ghost btn-m" href="#planos" data-go="#planos">Ver planos</a></div>
    </div>
    <!-- 🖼️ MÍDIA: interface desenhada em código, já com "Sua Agência" no lugar da marca. Troque por print real quando tiver -->
    <div class="side-shot reveal">{app_mock('wl', white_label=True)}</div>
  </div>
  <div class="wrap">{strip()}</div>
</section>
<section class="sec glow">
  <div class="wrap">
    <div class="head center reveal"><h2>Quatro módulos, uma marca: a sua.</h2><p class="lead">Seu logo, suas cores e seu domínio em cada tela que o seu cliente vê.</p></div>
    {soft_cards.replace('Ver demonstração', 'Incluído no white label').replace('09-software-whitelabel.html', '#form')}
  </div>
</section>
<section class="sec light">
  <div class="wrap split">
    <div class="reveal"><h2>Como o white label funciona.</h2></div>
    <ol class="steps reveal">
      <li><span class="n">1</span><div><h3>Sua marca</h3><p>Logo, cores, domínio próprio e e-mails com seu nome.</p></div></li>
      <li><span class="n">2</span><div><h3>Seus clientes</h3><p>Você cadastra, define o preço e fica com a margem.</p></div></li>
      <li><span class="n">3</span><div><h3>Nossa tecnologia</h3><p>Servidor, atualização, segurança e suporte de nível 2 com a Full10X.</p></div></li>
    </ol>
  </div>
</section>
<section class="sec light mist" id="planos">
  <div class="wrap">
    <div class="head center reveal"><h2>Planos</h2><p class="lead">Valores de referência. Fechamos a proposta na demonstração.</p></div>
    <div class="plans">
      <div class="plan reveal"><span class="tag">Start</span><p class="price"><span class="todo">[R$X]</span><small>/mês</small></p><p>Até <span class="todo">[10]</span> clientes.</p><ul><li>{ic("check")}CRM com sua marca</li><li>{ic("check")}Domínio próprio</li><li>{ic("check")}Suporte por e-mail</li></ul><a class="btn btn-primary" href="#form" data-go="#form" data-pos="plano-start">Falar com vendas</a></div>
      <div class="plan hot reveal"><span class="tag">Mais escolhido</span><p class="price"><span class="todo">[R$X]</span><small>/mês</small></p><p>Até <span class="todo">[50]</span> clientes.</p><ul><li>{ic("check")}CRM + gateway de pagamento</li><li>{ic("check")}IA comercial</li><li>{ic("check")}Suporte prioritário</li></ul><a class="btn btn-primary" href="#form" data-go="#form" data-pos="plano-pro">Falar com vendas</a></div>
      <div class="plan reveal"><span class="tag">Scale</span><p class="price"><span class="todo">[Sob consulta]</span></p><p>Clientes ilimitados.</p><ul><li>{ic("check")}Os 4 módulos</li><li>{ic("check")}IA operacional treinada</li><li>{ic("check")}Gerente de conta</li></ul><a class="btn btn-primary" href="#form" data-go="#form" data-pos="plano-scale">Falar com vendas</a></div>
    </div>
  </div>
</section>
<section class="sec glow">
  <div class="wrap split" style="align-items:start">
    <div class="reveal"><h2>Veja o painel com a sua marca.</h2><p class="lead" style="margin-top:16px">Na demonstração de 30 minutos montamos uma prévia com o seu logo e mostramos os módulos funcionando.</p>
      <div class="faq" style="margin-top:28px">{faq([("Preciso saber programar?","Não. A configuração é feita pela Full10X."),("Quanto tempo para ficar pronto?","<span class=\"todo\">[PRAZO]</span> após a assinatura."),("Posso cobrar o que eu quiser?","Sim. Você define o preço para o seu cliente e fica com a margem."),("Meus dados ficam seguros?","<span class=\"todo\">[DESCREVA HOSPEDAGEM, BACKUP E LGPD]</span>")])}</div></div>
    {form_card('software-whitelabel', 'Agende sua demonstração', f9, 'Ver horários', done9, evento='Lead', fid='form')}
  </div>
</section>
</main>
{footer('f10')}
{mbar('Agendar demonstração')}'''
pages['09-software-whitelabel.html'] = page('Full10X · Software white label para agências', 'CRM, gateway de pagamento e IA com a sua marca para revender aos seus clientes.', 'https://grupofull10x.com/white-label', 'software-whitelabel', body,
  ",\n  CALENDLY_URL:'' /* 🔗 evento de demonstração */,\n  POS_AGENDAMENTO_URL:''")
