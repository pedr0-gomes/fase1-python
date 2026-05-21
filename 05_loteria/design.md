# Design — Loteria

## Visão
Loteria custom; pool fixo 1-10; jogador deposita saldo; aposta 3/4/5 números; programa sorteia mesma quantidade; ganha de acordo com os acertos.

## Parâmetros
- Saldo inicial: depositado pelo jogador, sem mínimo.
- Pool: números de 1 a 10.
- Apostas válidas: 3, 4 ou 5 números.
- Sorteio: programa sorteia a mesma quantidade que o jogador apostou.
- Custo por rodada: R$1,00 (aposta 3) / R$1,50 (aposta 4) / R$2,00 (aposta 5).

### Tabela de prêmios

**Aposta 3 (custo R$1,00):**

┌─────────┬─────────┬────────────┐
│ Acertos │ Prêmio  │ Frequência │
├─────────┼─────────┼────────────┤
│ 0       │ R$0,00  │ 29%        │
├─────────┼─────────┼────────────┤
│ 1       │ R$0,20  │ 53%        │
├─────────┼─────────┼────────────┤
│ 2       │ R$2,50  │ 17%        │
├─────────┼─────────┼────────────┤
│ 3       │ R$35,00 │ 0,8%       │
└─────────┴─────────┴────────────┘

Valor esperado: R$0,83 — casa fica com 17%.

**Aposta 4 (custo R$1,50):**

┌─────────┬─────────┬────────────┐
│ Acertos │ Prêmio  │ Frequência │
├─────────┼─────────┼────────────┤
│ 0       │ R$0,00  │ 7%         │
├─────────┼─────────┼────────────┤
│ 1       │ R$0,20  │ 38%        │
├─────────┼─────────┼────────────┤
│ 2       │ R$0,50  │ 43%        │
├─────────┼─────────┼────────────┤
│ 3       │ R$5,00  │ 11%        │
├─────────┼─────────┼────────────┤
│ 4       │ R$80,00 │ 0,5%       │
└─────────┴─────────┴────────────┘

Valor esperado: R$1,24 — casa fica com 17%.

**Aposta 5 (custo R$2,00):**

┌─────────┬─────────┬────────────┐
│ Acertos │ Prêmio  │ Frequência │
├─────────┼─────────┼────────────┤
│ 0       │ R$0,00  │ 0,4%       │
├─────────┼─────────┼────────────┤
│ 1       │ R$0,00  │ 10%        │
├─────────┼─────────┼────────────┤
│ 2       │ R$0,25  │ 40%        │
├─────────┼─────────┼────────────┤
│ 3       │ R$1,00  │ 40%        │
├─────────┼─────────┼────────────┤
│ 4       │ R$8,00  │ 10%        │
├─────────┼─────────┼────────────┤
│ 5       │ R$90,00 │ 0,4%       │
└─────────┴─────────┴────────────┘

Valor esperado: R$1,66 — casa fica com 17%.

## Fluxo do jogador

1. Programa pergunta o saldo inicial → jogador deposita.
2. Loop até condição de parada:
   - Parada: saldo < R$1.
   - Programa pergunta quantidade (3/4/5/q) — se q, termina.
   - Se custo > saldo: pede outra quantidade.
   - Saldo = saldo - custo.
   - Jogador escolhe os N números do pool 1-10.
   - Programa sorteia N números do pool 1-10.
   - Mostra acertos e prêmio se houver.
   - Saldo = saldo + prêmio.

## Estado
- Saldo atual do jogador.
- Números escolhidos na rodada atual.
- Números sorteados na rodada atual.

## Casos de borda
- Saldo insuficiente para aposta escolhida → pede outra quantidade.
- Saldo < R$1 → termina o programa.
- Jogador digita entrada inválida no prompt da quantidade → pede de novo.
- Jogador digita `q` no prompt da quantidade → termina o programa.
- Jogador digita número fora de 1-10 → pede de novo, sem gastar tentativa.
- Jogador digita número repetido na mesma aposta → pede de novo.
- Jogador digita algo que não é número → pede de novo.

## Funções

- `pedir_saldo_inicial() → float`
  Pergunta ao jogador quanto quer depositar; valida que é número e retorna.
- `pedir_quantidade(saldo) → int ou None`
  Pergunta ao jogador 3/4/5/q. Retorna a quantidade escolhida, ou `None` se o jogador digitar `q`.
- `custo(quantidade) → float`
  Mapeia 3 → 1,00 / 4 → 1,50 / 5 → 2,00.
- `escolher_numeros(quantidade) → set`
  Pede ao jogador para escolher N números válidos do pool 1-10 e retorna um conjunto com esses números.
- `sortear_numeros(quantidade) → set`
  Sorteia aleatoriamente N números do pool 1-10 e retorna um conjunto com esses números.
- `contar_acertos(escolhidos, sorteados) → int`
  Compara os dois conjuntos e retorna quantos números aparecem em ambos.
- `calcular_premio(quantidade, acertos) → float`
  Consulta a tabela de prêmios e retorna o valor correspondente a (quantidade, acertos).
- `mostrar_resultado(quantidade, acertos, premio, saldo) → None`
  Exibe a quantidade de acertos, o prêmio recebido e o saldo atualizado.
