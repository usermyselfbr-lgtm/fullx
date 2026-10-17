import sys, pathlib, importlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _comum import pages, go_ic
OUT = pathlib.Path(__file__).parent

# O texto de cada página fica em paginas/pNN_*.py; design e componentes em _sistema.py; helpers em _comum.py
PAGINAS = ['p01_institucional', 'p01b_blog', 'p01c_blog_artigo', 'p02_form_calendly', 'p03_vsl_qualificacao', 'p04_vsl_form_calendly', 'p05_aplicacao', 'p06_playbook_ebook', 'p07_playbook_curso', 'p08_backredirect', 'p09_software_whitelabel', 'p00_modelos']
for m in PAGINAS: importlib.import_module(f'paginas.{m}')

import re as _re
# ───────────── publicação por caminho em fullxmarketing.com ─────────────
from _rotas import DOMINIO, SLUGS, NOINDEX
DIST = OUT / 'dist'

def _setas(html):
    # seta animada nos CTAs principais (só links grandes, sem ícone próprio)
    return _re.sub(r'(<a class="btn btn-primary btn-m"[^>]*>)([^<]+)</a>', lambda m: m.group(1) + m.group(2) + go_ic() + '</a>', html)

def _links(html, slug):
    # links internos NN-nome.html → /slug/ (mantém #âncora); canônico e domínio antigo → fullxmarketing.com
    html = _re.sub(r'href="(0\d[a-z]?-[a-z-]+\.html)(#[^"]*)?"', lambda m: f'href="/{SLUGS[m.group(1)]}/{m.group(2) or ""}"', html)
    html = _re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{DOMINIO}/{slug}/">', html)
    html = html.replace('https://grupofull10x.com/espera', f'{DOMINIO}/espera/').replace('https://grupofull10x.com', DOMINIO)
    if slug in NOINDEX: html = html.replace('<meta name="description"', '<meta name="robots" content="noindex,nofollow">\n<meta name="description"', 1)
    return html

for name, html in pages.items():
    slug = SLUGS[name]
    d = DIST / slug; d.mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(_links(_setas(html), slug), encoding='utf-8')
print(len(pages), 'páginas em', DIST)
