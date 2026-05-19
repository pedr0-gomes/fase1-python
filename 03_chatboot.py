# ============================================================
# 03_chatboot.py - Modularização e biblioteca
# Tema: funções puras, dispatch dinâmico, módulos, tuplas
# ============================================================
#
# TAREFA 03.1 - Operações como funções puras
#   - Criar `def somar(a: float, b: float) -> float: return a + b`.
#   - Adicionar `subtrair`, `multiplicar`, `dividir` no mesmo padrão.
#   - Função pura = SEM `input` e SEM `print` dentro. Só recebe números e devolve número.
#   - Em `dividir`, tratar divisão por zero (checagem explícita ou try/except ZeroDivisionError).
#   - No elif da soma, chamar `somar(num1, num2)` em vez de fazer `num1 + num2` inline.
#   - Pronto quando: as 4 funções existem isoladas, e o elif da soma chama `somar(...)`.
#   - Commit:
#       git add 03_chatboot.py
#       git commit -m "exercise(03): extract arithmetic operations into pure typed functions"
#
# TAREFA 03.2 - Dispatch via dict de funções
#   - Criar `operacoes = {"+": somar, "-": subtrair, "*": multiplicar, "/": dividir}`.
#     (SEM parênteses nas funções - você guarda a REFERÊNCIA, não chama.)
#   - Substituir os 4 elif quase iguais por UM bloco:
#       if user_input in operacoes:
#           ... coleta n1, n2 ...
#           resultado = operacoes[user_input](n1, n2)
#           print(resultado)
#   - Adicionar `*`, `-`, `/` como comandos válidos (além do `+`).
#   - Pronto quando: um único bloco trata as 4 operações. Adicionar 5ª é só 1 linha no dict + a função.
#   - Commit:
#       git add 03_chatboot.py
#       git commit -m "exercise(03): dispatch arithmetic ops via dict of functions"
#
# TAREFA 03.3 - Variedade de respostas com `import random`
#   - No topo: `import random`.
#   - Mudar `answers` de `dict[str, str]` para `dict[str, list[str]]`:
#       answers["hi"] = ["Hi there!", "Hello!", "Hey, how can I help?"]
#   - Substituir `print(answers[user_input])` por `print(random.choice(answers[user_input]))`.
#   - Pronto quando: digitar "hi" duas vezes pode dar respostas diferentes.
#   - Commit:
#       git add 03_chatboot.py
#       git commit -m "exercise(03): vary greetings using random.choice over response lists"
#
# TAREFA 03.4 - Tuplas para entrada estruturada
#   - Criar `def parse_dois_numeros(entrada: str) -> tuple[float, float]`:
#       - faz .split() na string
#       - converte cada parte para float
#       - retorna tuple (num1, num2)
#       - trata ValueError se formato inválido (poucos números, texto, etc.)
#   - No fluxo de operação: pedir UMA linha só ("Dois números: "),
#     unpacking `a, b = parse_dois_numeros(entrada)`,
#     chamar `operacoes[user_input](a, b)`.
#   - Pronto quando: digitar `+` e depois `3 5` responde `8.0`. Formato inválido é tratado sem crash.
#   - Commit:
#       git add 03_chatboot.py
#       git commit -m "exercise(03): parse two numbers from single line returning tuple"
#
# Ao final das 4 tarefas, atualizar README.md e commitar:
#   git add README.md
#   git commit -m "docs: log completion of 03_chatboot (functions, dispatch, modules)"
# ============================================================


# Referências de estudo (vindas do 01):
# link 1: https://youtu.be/8KCuHHeC_M0?si=qiskmxx-k4T6EVwN
# link 2: https://www.youtube.com/watch?v=Ro_MScTDfU4
# link 3: https://youtu.be/Gx5qb1uHss4?si=LtpBNIB6yST3Vlcq

from typing import Final
EXITS: Final[set[str]] = {"bye","goodbye","see you"}

answers: dict[str,str] = {}
answers["hi"] = "Hi there! How can I help you?"
answers["hello"] = "Hi there! How can I help you?"

history: list[str] = []

def add(a: float, b: float) -> float: return a + b
def sub(a: float,b: float) -> float: return a - b
def mul(a: float, b: float) -> float: return a * b
def div(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")

arithmetic = {"+": add, "-": sub, "*": mul, "/": div}

bot_name: str = "Bob"
print(f"Hello! I'm {bot_name}! How can I assist you today?")

while True:
    user_input: str = input('You: ').lower()
    history.append(f"You: {user_input}")

    if user_input in EXITS:
        print(f"{bot_name}: Goodbye! Have a great day! ")
        break
    elif user_input in answers:
        print(answers[user_input])
        history.append(f"{bot_name}: {answers[user_input]}")
    elif user_input in arithmetic:
        print(f"{bot_name}: Sure! Let's do some {arithmetic[user_input].__name__}! Please enter two numbers")
        history.append(f"{bot_name}: Sure! Let's do some {arithmetic[user_input].__name__}! Please enter two numbers")
        try:
            num1: float = float(input("First number: "))
            num2: float = float(input("Second number: "))
            print(f"{bot_name}: The {arithmetic[user_input].__name__} is {arithmetic[user_input](num1,num2)}")
            history.append(f"{bot_name}: The {arithmetic[user_input].__name__} is {arithmetic[user_input](num1,num2)}")
        except ValueError:
            print(f"{bot_name}: Oops! That doesn't sem like a valid number. Try again!")
            history.append(f"{bot_name}: Oops! That doesn't sem like a valid number. Try again!")
    elif user_input == "history":
        print(f"{bot_name}: Here's our conversation: ")
        for hist in history:
            print(hist)
    else:
        print(f"{bot_name}: I'm sory, I don't understand that, Please try again.")
        history.append(f"{bot_name}: I'm sory, I don't understand that, Please try again.")
