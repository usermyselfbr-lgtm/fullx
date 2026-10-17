# ═══════════════════ 09 · SOFTWARE WHITE LABEL (acesso antecipado) ═══════════════════
# Estado real (FONTE-DA-VERDADE 3b): white label ainda não é contratável. CRM e cobrança rodam na nossa agência;
# IA operacional é protótipo; IA comercial não existe. Sem preço, plano, prazo ou texto de LGPD: nada disso aparece aqui.
from _comum import *

f9 = (step(1, 'Seu contato', 'Para o time falar com você sobre a demonstração.', CONTATO() + inp('empresa', 'Nome da agência ou consultoria', err='Escreva o nome da empresa.'))
      + step(2, 'Quantos clientes você atende hoje?', 'Ajuda a mostrar o sistema no volume da sua carteira.', radios('clientes', [('ate-10', 'Até 10', 1), ('11-30', '11 a 30', 2), ('31-100', '31 a 100', 3), ('100+', 'Mais de 100', 3)]))
      + step(3, 'O que você quer revender primeiro?', 'Escolha o principal. O resto entra na conversa.', radios('modulo', [('crm', 'CRM', 1), ('pagamento', 'Sistema de cobrança (régua por WhatsApp)', 1), ('ia-op', 'IA operacional (em construção)', 1), ('ia-com', 'IA comercial (ainda não existe)', 1), ('todos', 'CRM e cobrança juntos', 2)])))
# Sem agenda configurada: confirmação simples. Quando existir CALENDLY_URL, acrescente '<div data-calendly></div>' como 3º argumento.
done9 = OK('Vamos montar sua demonstração.', 'O time fala com você em até 24 horas úteis.')

# bento() do _sistema exige os 4 módulos (inclui IA comercial, que não existe). Mesma marcação, só com o que é verdade.
SOFT_09 = [('crm', 'CRM', 'Em uso na nossa operação. O comercial da agência vive aqui, do lead novo ao fechamento.', ['Pipeline por etapa', 'Formulário que pontua o lead', 'Tarefas do SDR e do closer', 'WhatsApp dentro do CRM'], 'w4', ''),
           ('pay', 'Sistema de cobrança', 'Construído para a nossa agência, roda sobre o Asaas. Lembra e cobra o cliente pelo WhatsApp.', ['Régua de cobrança por WhatsApp', 'Integrado ao Asaas', 'Atraso acima de 30 dias sinalizado'], 'w2', ''),
           ('ops', 'IA operacional (em construção)', 'Protótipo, fora da primeira leva do white label. Uma base com os processos da agência que responde as dúvidas do time de entrega.', ['Protótipo em teste', 'Base de processos', 'Responde o time'], 'w4', ' style="grid-column:1/-1"')]
def bento09(items, link_label='Quero ver na demonstração', link_href='#form'):
    out = ''
    for i, t, d, l, w, st in items:
        chips = ''.join(f'<span class="chip-s">{x}</span>' for x in l)
        out += (f'<article class="tile spot reveal {w}"{st}><span class="ico">{ic(i)}</span><h3>{t}</h3><p>{d}</p><div class="chips">{chips}</div>'
                f'<a class="more" href="{link_href}" data-go="{link_href}" data-pos="modulo-{i}">{link_label} {ic("arrow")}</a>{ART[i]()}</article>')
    return f'<div class="bento">{out}</div>'

TESE = [('layers', 'O problema do white label comum', 'O fornecedor nunca usou o sistema para vender nem para cobrar. Quem encontra as falhas é o seu cliente, com a sua marca na tela.'),
        ('crm', 'O que já roda aqui', 'O CRM e o sistema de cobrança foram construídos para a operação da Full10X e são usados nela. Você vê a tela, não a teoria.'),
        ('shield', 'Por que lista, e não venda', 'A versão com a sua marca só abre quando estiver pronta para o seu cliente usar. Até lá, mostramos o que roda e guardamos o seu lugar.')]
tese = ''.join(f'<article class="card reveal"><span class="ico">{ic(i)}</span><h3>{t}</h3><p>{d}</p></article>' for i, t, d in TESE)

FAQ_09 = [('Já posso contratar o white label?', 'Ainda não. Hoje o CRM e a cobrança rodam na nossa agência. Quem entra na lista vê o sistema na demonstração e é chamado primeiro quando a versão com a sua marca abrir.'),
          ('Quanto vai custar?', 'O preço ainda não está definido. Entrar na lista e ver a demonstração não custa nada.'),
          ('Preciso saber programar?', 'Não. A configuração é feita pela Full10X.'),
          ('Posso cobrar o que eu quiser do meu cliente?', 'Sim. Você define o preço que cobra do seu cliente.'),
          ('Meus dados e os dos meus clientes ficam seguros?', 'O CRM roda em nuvem e separa os dados de cada agência. Um teste automático no código confere essa separação. Os termos de privacidade (LGPD) e de backup vão por escrito antes de qualquer contrato.'),
          ('E a IA que atende o lead no WhatsApp?', 'Não existe hoje, por isso fica fora do white label. Aqui só entra o que já roda.')]

body = f'''{topbar('t10', ('Pedir demonstração', '#form', 'data-go="#form" data-pos="topo"'))}
<main>
<section class="sec hero glow">
  <div class="wrap split">
    <div>
      <span class="eyebrow"><i aria-hidden="true"></i>Acesso antecipado ao white label</span>
      <h1>Revenda o CRM que roda na nossa agência. Com a sua marca.</h1>
      <p class="lead">O CRM e o sistema de cobrança que usamos para vender e cobrar na Full10X vão ganhar versão com o seu logo e as suas cores, para você oferecer aos seus clientes. O white label ainda não está à venda. Peça a demonstração e entre na lista da primeira leva.</p>
      <div class="cta-row" data-hero-cta><a class="btn btn-primary btn-m" href="#form" data-go="#form" data-pos="hero">Pedir demonstração</a><a class="btn btn-ghost btn-m" href="#modulos" data-go="#modulos" data-pos="hero-modulos">Ver o que já roda</a></div>
      {PROOF}
    </div>
    <!-- 🖼️ MÍDIA: interface desenhada em código, com "Sua Agência" no lugar da marca. Troque por print real do CRM quando tiver -->
    <div class="side-shot reveal">{app_mock('wl', white_label=True)}</div>
  </div>
  <div class="wrap">{strip()}</div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="head center reveal"><h2>Primeiro roda na nossa agência. Depois leva a sua marca.</h2><p class="lead">Software com o seu nome é mais um motivo para o cliente continuar com você. Por isso ele precisa funcionar antes de chegar até ele.</p></div>
    <div class="grid g3">{tese}</div>
  </div>
</section>
<section class="sec glow" id="modulos">
  <div class="wrap">
    <div class="head center reveal"><h2>O que já roda e o que ainda estamos construindo.</h2><p class="lead">A primeira leva do white label é o CRM e a cobrança. A IA operacional entra quando sair do protótipo.</p></div>
    {bento09(SOFT_09)}
  </div>
</section>
<section class="sec light">
  <div class="wrap split">
    <div class="reveal"><h2>Como funciona o acesso antecipado.</h2></div>
    <ol class="steps reveal">
      <li><span class="n">1</span><div><h3>Você responde 3 perguntas</h3><p>Contato, tamanho da carteira e o que quer revender primeiro. Leva menos de um minuto.</p></div></li>
      <li><span class="n">2</span><div><h3>O time mostra o sistema rodando</h3><p>O CRM e a cobrança como usamos na nossa operação, e como ficariam para os seus clientes.</p></div></li>
      <li><span class="n">3</span><div><h3>Quando abrir, você é chamado primeiro</h3><p>A Full10X faz a configuração com a sua marca. O preço que você cobra do seu cliente é decisão sua.</p></div></li>
    </ol>
  </div>
</section>
<section class="sec light mist">
  <div class="wrap">
    <div class="head center reveal"><h2>Para quem é a lista.</h2></div>
    <div class="compare" style="max-width:900px;margin:0 auto">
      <div class="no reveal"><h3>Não é para você se</h3><ul><li>Precisa do sistema com a sua marca funcionando este mês.</li><li>Procura uma IA que atende e vende sozinha no WhatsApp.</li><li>Ainda não tem clientes pagando todo mês.</li></ul></div>
      <div class="yes reveal"><h3>É para você se</h3><ul><li>Tem agência ou consultoria com clientes recorrentes.</li><li>Quer vender software junto com o serviço.</li><li>Prefere esperar a versão pronta a revender uma tela de apresentação.</li></ul></div>
    </div>
  </div>
</section>
<section class="sec glow">
  <div class="wrap split" style="align-items:start">
    <div class="reveal"><h2>Veja o sistema antes de colocar o seu nome nele.</h2><p class="lead" style="margin-top:16px">Na demonstração você vê o CRM e a cobrança que rodam na nossa agência e tira as dúvidas sobre o white label.</p>
      <div class="faq" style="margin-top:28px">{faq(FAQ_09)}</div></div>
    {form_card('software-whitelabel', 'Peça sua demonstração', f9, 'Pedir demonstração', done9, evento='Lead', fid='form')}
  </div>
</section>
</main>
{footer('f10', full=False)}
{mbar('Pedir demonstração')}'''
pages['09-software-whitelabel.html'] = page('White label do CRM Full10X · acesso antecipado', 'Veja o CRM e o sistema de cobrança que rodam na nossa agência e entre na lista para revendê-los com a sua marca.', 'https://grupofull10x.com/white-label', 'software-whitelabel', body,
  ",\n  CALENDLY_URL:'' /* 🔗 evento de demonstração (hoje sem agenda: a conclusão mostra só a confirmação) */,\n  POS_AGENDAMENTO_URL:''")
