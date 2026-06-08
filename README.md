# fase1 — Python: base

Trajetória de aprendizado de Python, fase 1.
Contexto, stack e dinâmica de trabalho: ver `CLAUDE.md`.

## Camada atual

**3. Estrutura — em andamento.** Módulos, pacotes, separação de responsabilidades, testes com `pytest`.

Anteriores: **2. APIs — concluída** (`requests`, consumo de JSON via rede, tratamento de erro HTTP/rede) · **1. Dados — concluída** (tipos primitivos, coleções, leitura/escrita de arquivos).

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

**Camada 2 concluída.**

## Exercícios da Camada 3

| Pasta | Tema | Conceitos exercitados |
|---|---|---|
| `01_nomes_em_lote/` | Pipeline de nomes em lote (capstone) | separação de responsabilidades em 4 módulos (`entrada`/`ibge`/`saida`/`main`), `set` para dedupe, `csv.DictWriter`, reúso de módulo entre exercícios, guard `if __name__ == "__main__"` |
