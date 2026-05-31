# fase1 — Python: base

Trajetória de aprendizado de Python, fase 1.
Contexto, stack e dinâmica de trabalho: ver `CLAUDE.md`.

## Camada atual

**2. APIs — em andamento.** `requests`, consumo de JSON via rede, tratamento de erro HTTP/rede.

Anterior: **1. Dados — concluída.** Tipos primitivos, coleções (`list`, `dict`, `set`, `tuple`), leitura/escrita de arquivos.

## Progressão do chatboot

| Arquivo | Tema | Conceitos exercitados |
|---|---|---|
| `01_chatboot.py` | Base | variáveis tipadas, f-strings, `while`/`break`, `if/elif`, `try/except`, `float()` |
| `02_chatboot.py` | Memória e mapeamento | `dict` (lookup de respostas), `list` + `for` (histórico), `set` + `Final` (palavras de saída em CAPS) |
| `03_chatboot.py` | Modularização e biblioteca | `def`/`return` (funções puras), dispatch via dict de funções, `import random` + `random.choice`, `tuple` + unpacking, `raise` |
| `04_chatboot.py` | Orientação a objetos | `class`, `__init__`, `self`, métodos de instância, dunder methods (`__str__`, `__len__`) |

**Progressão do chatboot concluída.**

## Outros exercícios da Camada 1

| Pasta | Tema | Conceitos exercitados |
|---|---|---|
| `05_loteria/` | Loteria customizada | funções puras vs interativas, `set` + intersecção (`&`), `random.sample`, `dict` aninhado, validação de input com `try/except` |
| `06_arquivos/` | Manipulação de arquivos | `csv.DictReader`, `json.dump`, `with`/context manager, encoding UTF-8, filtro com lista branca |

**Camada 1 concluída.**

## Exercícios da Camada 2

| Pasta | Tema | Conceitos exercitados |
|---|---|---|
| `01_nomes_ibge/` | Frequência de nomes (IBGE) | `requests.get` + `timeout`, `raise_for_status`, parsing de JSON via rede, hierarquia de exceções, exceção customizada (`UsuarioDesistiu`), loop de retry |
