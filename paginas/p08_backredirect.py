# ═══════════════════ 08 · BACKREDIRECT ═══════════════════
# Oferta de saída = o mesmo Playbook Full10X da página 06 (PDF real, servido em /playbook/Playbook-Full10X.pdf)
from _comum import *

f8 = step(1, 'Libere o seu PDF', '', inp('nome', 'Seu nome', auto='given-name', err='Escreva seu nome.') + inp('email', 'E-mail', 'email', 'voce@agencia.com', auto='email', err='Confira o e-mail.'))
BULLETS = ['As 5 métricas que dizem se a agência pode escalar: CAC, LTV, retorno, ticket e conversão.',
           'Pré-vendas e vendas no papel: os 4 tipos de SDR, a call do closer e o pipeline do CRM.',
           'O plano de 6 semanas para implantar um módulo por vez, com checklist.']
bullets = ''.join(f'<span>{ic("check")}{b}</span>' for b in BULLETS)
body = f'''<main>
<section class="sec hero glow center" style="min-height:100svh;display:grid;align-content:center">
  <div class="wrap">
    <div style="display:grid;place-items:center">{mark('bk', size=56)}</div>
    <span class="eyebrow" style="margin-top:26px"><i aria-hidden="true"></i>Antes de sair</span>
    <h1 style="max-width:18ch;margin-inline:auto">Antes de sair, leve o playbook. 147 páginas, grátis.</h1>
    <p class="lead">Não quis seguir agora? Tudo bem. O Playbook Full10X fica com você para aplicar no seu ritmo.</p>
    <div class="proof-line" style="flex-direction:column;align-items:flex-start;max-width:460px;margin:26px auto 0;text-align:left">{bullets}</div>
    <div style="max-width:460px;margin:30px auto 0;text-align:left" data-hero-cta>
      {form_card('backredirect', 'Grátis · download na hora', f8, 'Baixar o playbook grátis', OK('O playbook é seu.', 'PDF de 25 MB: no 4G, salve para ler depois.', f'<a class="btn btn-primary on-light" href="#" data-dl="DOWNLOAD_URL" target="_blank" rel="noopener">{ic("down")}Baixar o playbook (PDF)</a>'), evento='Lead')}
    </div>
    <p class="small" style="margin-top:22px"><a href="01-institucional.html">Não, obrigado. Ir para o site.</a></p>
  </div>
</section>
</main>'''
pages['08-backredirect.html'] = page('Full10X · Antes de sair', 'Leve grátis o Playbook Full10X: 147 páginas de oferta, funil, comercial e retenção para donos de agência.', 'https://grupofull10x.com/espera', 'backredirect', body,
  ",\n  DOWNLOAD_URL:'/playbook/Playbook-Full10X.pdf' /* mesmo PDF da página 06 */\n  /* COMO USAR: nas outras páginas, coloque em BACK_URL o endereço desta página (ex.: 'https://grupofull10x.com/espera').\n     Quem apertar \"voltar\" no navegador cai aqui. Esta página não tem backredirect para não prender a pessoa. */")
