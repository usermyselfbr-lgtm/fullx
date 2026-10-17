# ═══════════════════ 08 · BACKREDIRECT ═══════════════════
from _comum import *

f8 = step(1, 'Para onde mandamos?', '', inp('nome', 'Seu nome', auto='given-name', err='Escreva seu nome.') + inp('email', 'E-mail', 'email', 'voce@agencia.com', auto='email', err='Confira o e-mail.'))
body = f'''<main>
<section class="sec hero glow center" style="min-height:100svh;display:grid;align-content:center">
  <div class="wrap">
    <div style="display:grid;place-items:center">{mark('bk', size=56)}</div>
    <span class="eyebrow" style="margin-top:26px"><i aria-hidden="true"></i>Antes de sair</span>
    <!-- ✏️ OFERTA DE SAÍDA: algo menor e mais fácil do que a oferta da página anterior -->
    <h1 style="max-width:18ch">Leve pelo menos o playbook. É grátis.</h1>
    <p class="lead">Não quis seguir agora? Tudo bem. Leve o modelo de formulário que qualifica lead e aplique sozinho.</p>
    <div style="max-width:460px;margin:34px auto 0;text-align:left" data-hero-cta>
      {form_card('backredirect', 'Receba no e-mail', f8, 'Quero o playbook', OK('Enviado.', 'Confira seu e-mail. O link também está aqui:', f'<a class="btn btn-primary on-light" href="#" data-dl="DOWNLOAD_URL" target="_blank" rel="noopener">{ic("down")}Baixar agora</a>'), evento='Lead')}
    </div>
    <p class="small" style="margin-top:22px"><a href="01-institucional.html">Não, obrigado. Ir para o site.</a></p>
  </div>
</section>
</main>'''
pages['08-backredirect.html'] = page('Full10X · Antes de sair', 'Leve o playbook gratuito da Full10X.', 'https://grupofull10x.com/espera', 'backredirect', body,
  ",\n  DOWNLOAD_URL:''\n  /* COMO USAR: nas outras páginas, coloque em BACK_URL o endereço desta página (ex.: 'https://grupofull10x.com/espera').\n     Quem apertar \"voltar\" no navegador cai aqui. Esta página não tem backredirect para não prender a pessoa. */")
