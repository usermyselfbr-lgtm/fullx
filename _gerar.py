import sys, pathlib, importlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _comum import pages, go_ic
OUT = pathlib.Path(__file__).parent

# O texto de cada página fica em paginas/pNN_*.py; design e componentes em _sistema.py; helpers em _comum.py
PAGINAS = ['p01_institucional', 'p01b_blog', 'p01c_blog_artigo', 'p02_form_calendly', 'p03_vsl_qualificacao', 'p04_vsl_form_calendly', 'p05_aplicacao', 'p06_playbook_ebook', 'p07_playbook_curso', 'p08_backredirect', 'p09_software_whitelabel', 'p00_modelos']
for m in PAGINAS: importlib.import_module(f'paginas.{m}')

import re as _re
def _setas(html):
    # seta animada nos CTAs principais (só links grandes, sem ícone próprio)
    return _re.sub(r'(<a class="btn btn-primary btn-m"[^>]*>)([^<]+)</a>', lambda m: m.group(1) + m.group(2) + go_ic() + '</a>', html)
for name, html in pages.items():
    (OUT / name).write_text(_setas(html), encoding='utf-8')
print(len(pages), 'páginas')
