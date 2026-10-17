# Progresso — reconstrução das landing pages Full10X

Estados: PENDENTE · EM ANÁLISE · EM IMPLEMENTAÇÃO · EM TESTE · CONCLUÍDA · BLOQUEADA

| Página | Estado | Registro |
|---|---|---|
| Sistema compartilhado (`_sistema.py`, `_comum.py`) | PENDENTE | `SISTEMA.md` |
| 01 institucional | PENDENTE | `paginas/01-institucional.md` |
| 09 white-label | PENDENTE | `paginas/09-white-label.md` |
| 05 aplicacao | PENDENTE | `paginas/05-aplicacao.md` |
| 04 mentoria | PENDENTE | `paginas/04-mentoria.md` |
| 03 assista | PENDENTE | `paginas/03-assista.md` |
| 02 diagnostico | PENDENTE | `paginas/02-diagnostico.md` |
| 06 playbook | PENDENTE | `paginas/06-playbook.md` |
| 07 curso | PENDENTE | `paginas/07-curso.md` |
| 01b conteudos | PENDENTE | `paginas/01b-conteudos.md` |
| 01c artigo | PENDENTE | `paginas/01c-artigo.md` |
| 08 espera | PENDENTE | `paginas/08-espera.md` |
| 00 modelos | PENDENTE | `paginas/00-modelos.md` |

## Linha do tempo
- 16/10 23:50 — projeto criado em `~/projetos/fullx-funis`, skills instaladas (16/16), gerador separado por página (HTML idêntico), saída em `dist/<slug>/`, baseline visual capturado.
- 17/10 00:05 — inventário publicado; pesquisa da fonte da verdade em andamento.

## Como retomar
1. Ler `INVENTARIO.md`, `FONTE-DA-VERDADE.md` e este arquivo.
2. Editar `paginas/pNN_*.py` (texto) ou `_sistema.py` (design/JS); rodar `python3 _gerar.py`; rodar `node qa/screens.mjs <fase> [slug]`.
3. Publicar: copiar `dist/*` para `~/projetos/fullx-aula/` e rodar `~/projetos/fullx-aula/deploy.sh`.
