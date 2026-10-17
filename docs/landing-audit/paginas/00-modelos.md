# 00 · /modelos — Mapa das páginas (interno)

- **Rota:** `/modelos/` (noindex,nofollow). **Fonte:** `paginas/p00_modelos.py`, rotas em `_rotas.py`.
- **Mercado / ICP:** não é página de venda; uso interno do Julio e do time para abrir cada página e saber quando usar.
- **Objetivo:** navegação e documentação viva das rotas públicas.
- **Diagnóstico anterior:** cartões numerados "01, 02…" com nomes de arquivo e descrições de template ("modelo de post", "LP institucional"); título "Modelos de funil"; `lead` dizia "11 páginas no mesmo sistema visual".
- **Mudanças editoriais:** título → "Mapa das páginas Full10X"; cada cartão mostra o caminho público (`/white-label`), o que a página faz em linguagem de operação e "Quando usar" (origem de tráfego recomendada); ordem por importância comercial; aviso explícito de que a página é interna.
- **Mudanças técnicas:** `SLUGS`/`DOMINIO`/`NOINDEX` movidos para `_rotas.py` (compartilhado entre `_gerar.py` e esta página); `noindex,nofollow` aplicado no build.
- **Testes:** `python3 _gerar.py` → `12 páginas`; `node qa/screens.mjs 00-v1 modelos` → `overflow:0 console:0 todo:0 placeholders:0 links-quebrados:0 lcp390:219ms`; print 1440 conferido.
- **Pendências:** nenhuma. **Status:** CONCLUÍDA.
