# ═══════════════════ 00 · HUB DE MODELOS ═══════════════════
from _comum import *

HUB = [('01-institucional.html', 'LP institucional', 'Site da marca com softwares, conteúdos e mentoria.', 'Tráfego frio e orgânico, busca, bio'),
       ('01b-blog.html', 'Blog', 'Lista de aulas, playbooks e artigos com filtro.', 'SEO e conteúdo'),
       ('01c-blog-artigo.html', 'Artigo do blog', 'Modelo de post com CTA para o playbook.', 'SEO e remarketing'),
       ('02-form-calendly.html', 'Formulário + Calendly', 'Qualifica em 3 perguntas e abre a agenda.', 'Call de diagnóstico'),
       ('03-vsl-qualificacao.html', 'VSL + qualificação', 'Vídeo; formulário aparece no momento da oferta.', 'Mentoria high ticket'),
       ('04-vsl-form-calendly.html', 'VSL + formulário + Calendly', 'Vídeo, aplicação e agenda só para aprovados.', 'Mentoria com call'),
       ('05-aplicacao.html', 'Formulário de aplicação', '8 perguntas com nota de corte e escassez explicada.', 'Turmas e high ticket'),
       ('06-playbook-ebook.html', 'Playbook ebook (isca)', 'Captura curta e download na hora.', 'Topo de funil'),
       ('07-playbook-curso.html', 'Playbook curso (isca)', 'Cadastro para curso gratuito em 5 aulas.', 'Topo e meio de funil'),
       ('08-backredirect.html', 'Backredirect', 'Oferta de saída para quem aperta voltar.', 'Recuperar visita perdida'),
       ('09-software-whitelabel.html', 'Software white label', 'Módulos, planos e demonstração com agenda.', 'Venda B2B do software')]
cards = ''.join(f'<a class="card reveal" href="{f}"><span class="k">{f.split("-")[0]}</span><h3>{t}</h3><p>{d}</p><p class="small" style="margin-top:10px">Uso: {u}</p><span class="more">Abrir modelo {ic("arrow")}</span></a>' for f, t, d, u in HUB)
body = f'''<main>
<section class="sec hero glow center" style="padding-bottom:40px"><div class="wrap">{logo('hb', h=40)}<h1 style="margin:28px auto 0;max-width:18ch">Modelos de funil Full10X</h1><p class="lead">{len(HUB)} páginas no mesmo sistema visual. Clique para abrir.</p></div></section>
<section class="sec tight" style="padding-bottom:96px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
</main>'''
pages['00-modelos.html'] = page('Full10X · Modelos de funil', 'Índice dos modelos de página.', 'https://grupofull10x.com/modelos', 'hub', body)
