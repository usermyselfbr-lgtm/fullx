# ═══════════════════ 00 · MAPA DAS PÁGINAS (uso interno) ═══════════════════
from _comum import *
from _rotas import SLUGS, DOMINIO

# (arquivo, nome, o que a página faz, quando mandar tráfego para ela)
HUB = [('01-institucional.html', 'Institucional', 'Apresenta a Full10X: os quatro softwares, a mentoria e os conteúdos gratuitos.', 'Link da bio, busca orgânica e tráfego frio de marca'),
       ('09-software-whitelabel.html', 'Software white label', 'Vende o CRM, a cobrança e as IAs com a marca da agência do cliente. Termina em demonstração agendada.', 'Anúncio e prospecção B2B para agências e consultorias'),
       ('02-form-calendly.html', 'Call de diagnóstico', 'Três perguntas, nota de corte e agenda aberta para quem passa.', 'Tráfego morno: quem já viu conteúdo ou anúncio'),
       ('04-vsl-form-calendly.html', 'Mentoria · vídeo + agenda', 'Vídeo de vendas, aplicação em 4 perguntas e agenda só para aprovados.', 'Anúncio direto para a mentoria com call'),
       ('03-vsl-qualificacao.html', 'Mentoria · vídeo + aplicação', 'Vídeo de vendas; o formulário aparece no momento da oferta.', 'Anúncio para a mentoria sem agenda imediata'),
       ('05-aplicacao.html', 'Aplicação para a mentoria', 'Oito perguntas com nota de corte. Explica por que existe seleção.', 'Botão "Falar com o time" do site, remarketing e turmas'),
       ('06-playbook-ebook.html', 'Playbook (isca)', 'Captura curta e download do PDF na hora.', 'Topo de funil: anúncio de isca e CTA dos artigos'),
       ('07-playbook-curso.html', 'Curso gratuito (isca)', 'Cadastro para as 5 aulas gratuitas.', 'Topo e meio de funil, link da bio'),
       ('01b-blog.html', 'Conteúdos', 'Lista de aulas, playbooks e artigos com filtro e aviso por WhatsApp.', 'SEO e redes sociais'),
       ('01c-blog-artigo.html', 'Artigo', 'Modelo de artigo com chamada para o playbook no meio do texto.', 'SEO e remarketing'),
       ('08-backredirect.html', 'Antes de sair', 'Oferta de saída para quem aperta "voltar": leva o playbook.', 'Configure BACK_URL nas outras páginas; nunca anuncie para cá')]
cards = ''.join(f'<a class="card reveal" href="{f}"><span class="k">/{SLUGS[f]}</span><h3>{t}</h3><p>{d}</p><p class="small" style="margin-top:10px">Quando usar: {u}</p><span class="more">Abrir página {ic("arrow")}</span></a>' for f, t, d, u in HUB)
body = f'''<main>
<section class="sec hero glow center" style="padding-bottom:40px"><div class="wrap">{logo('hb', h=40)}<h1 style="margin:28px auto 0;max-width:18ch">Mapa das páginas Full10X</h1><p class="lead">{len(HUB)} páginas publicadas em {DOMINIO.replace('https://', '')}. Cada cartão mostra o endereço, o que a página faz e para qual tráfego ela serve. Esta página é interna e não aparece no Google.</p></div></section>
<section class="sec tight" style="padding-bottom:96px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
</main>'''
pages['00-modelos.html'] = page('Full10X · Mapa das páginas', 'Índice interno das páginas da Full10X em fullxmarketing.com.', 'https://grupofull10x.com/modelos', 'hub', body)
