# Design — Exercício 06: contagem de domínios NANDA-I

## Tarefa

Ler o CSV do NANDA-I 2024-2026, filtrar os 16 diagnósticos inativos, contar diagnósticos **ativos** por `dominio` e salvar o resumo em JSON.

## Entrada e saída

- **Entrada**: `nanda-i-2024-2026.csv` (291 registros, 8 colunas).
- **Saída**: arquivo JSON com `{dominio: contagem}`.

## Decomposição em funções

1. `verifica_dominio(linha)` — recebe uma linha do CSV. Se o registro for ativo, retorna o `dominio`; se inativo, retorna `None`.
2. `decide(dict, dominio)` — verifica se o domínio já existe no dict. Se sim, chama `incrementa_dominio`; se não, chama `cria_dominio`.
3. `cria_dominio(dict, dominio)` — adiciona o domínio ao dict com valor `1`.
4. `incrementa_dominio(dict, dominio)` — soma `1` ao valor do domínio.
5. `escreve_resumo(dict)` — grava o dict em arquivo JSON.
6. `main()` — abre o CSV, itera linha a linha, chama `verifica_dominio` → `decide`; ao fim, chama `escreve_resumo`.

## Decisões de design

- **Dict começa vazio e cresce** conforme novos domínios aparecem (em vez de pré-popular com os 13).
- **Filtro dos inativos** mora dentro de `verifica_dominio` (retorna `None` para inativos; o `main` ignora).
- **Formato de saída: JSON**, porque espelha direto a estrutura do dict, é o padrão da Camada 2 (APIs) e permite leitura de volta sem parser custom.
