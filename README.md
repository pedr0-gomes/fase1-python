# fase1 — Python: base

Trajetória de aprendizado de Python, fase 1.
Contexto, stack e dinâmica de trabalho: ver `CLAUDE.md`.

## Camada atual

**1. Dados** — tipos primitivos, coleções (`list`, `dict`, `set`, `tuple`), leitura/escrita de arquivos.

## Progressão do chatboot

| Arquivo | Tema | Conceitos exercitados |
|---|---|---|
| `01_chatboot.py` | Base | variáveis tipadas, f-strings, `while`/`break`, `if/elif`, `try/except`, `float()` |
| `02_chatboot.py` | Memória e mapeamento | `dict` (lookup de respostas), `list` + `for` (histórico), `set` + `Final` (palavras de saída em CAPS) |
| `03_chatboot.py` | Modularização e biblioteca | `def`/`return` (funções puras), dispatch via dict de funções, `import random` + `random.choice`, `tuple` + unpacking, `raise` |
| `04_chatboot.py` | Orientação a objetos | `class`, `__init__`, `self`, métodos de instância, dunder methods (`__str__`, `__len__`) |

**Progressão concluída.** Próximo passo: avançar para a camada 2 (APIs) com `requests`, ou consolidar com `pytest` sobre a `Chatbot` class.
