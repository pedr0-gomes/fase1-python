# ============================================================
# 04_chatboot.py - Orientação a objetos
# Tema: encapsular o bot numa classe + integrar à sintaxe Python via dunder methods
# ============================================================
#
# TAREFA 04.1 - Encapsular em `class Chatbot`
#   - Criar `class Chatbot:` com `__init__(self, nome: str)` que popula:
#       self.nome, self.history, self.answers, self.arithmetic, self.exits
#   - Mover os dados que estavam soltos (answers, history, arithmetic, EXITS) para DENTRO do __init__.
#     A partir daqui, cada bot tem seu PRÓPRIO estado — duas instâncias não compartilham history.
#   - Criar métodos:
#       - `responder(self, entrada: str)`: recebe entrada do usuário, processa (responde, soma, etc.),
#         atualiza self.history. Pode chamar outros métodos auxiliares se quiser.
#       - `mostrar_historico(self)`: itera self.history e printa.
#   - No final do arquivo: `bot = Chatbot("Bob")` e o `while` chama `bot.responder(entrada)`.
#   - Pronto quando: criar `bot1 = Chatbot("Bob")` e `bot2 = Chatbot("Alice")` funciona,
#     cada um mantém seu próprio history independente.
#   - Commit:
#       git add 04_chatboot.py
#       git commit -m "exercise(04): encapsulate chatbot state and behavior into a class"
#
# TAREFA 04.2 - Dunder methods
#   - Adicionar `__str__(self) -> str` retornando algo legível, ex:
#       f"Chatbot {self.nome} ({len(self.history)} mensagens)"
#   - Adicionar `__len__(self) -> int` retornando `len(self.history)`.
#   - Criar comando "info" no loop que faz `print(bot)` — Python chama __str__ automaticamente.
#   - Pronto quando:
#       - `print(bot)` mostra "Chatbot Bob (N mensagens)" em vez de "<__main__.Chatbot object at 0x...>"
#       - `len(bot)` retorna o tamanho do history (mesmo valor de len(bot.history))
#   - Commit:
#       git add 04_chatboot.py
#       git commit -m "exercise(04): integrate Chatbot with Python syntax via __str__ and __len__"
#
# Ao final das 2 tarefas, atualizar README.md e commitar:
#   git add README.md
#   git commit -m "docs: log completion of 04_chatboot (classes, dunder) - chatboot progression done"
# ============================================================


# Referências de estudo (vindas do 01):
# link 1: https://youtu.be/8KCuHHeC_M0?si=qiskmxx-k4T6EVwN
# link 2: https://www.youtube.com/watch?v=Ro_MScTDfU4
# link 3: https://youtu.be/Gx5qb1uHss4?si=LtpBNIB6yST3Vlcq

import random

def add(a: float, b: float) -> float: return a + b
def sub(a: float,b: float) -> float: return a - b
def mul(a: float, b: float) -> float: return a * b
def div(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")

def parse_two_numbers(enter: str) -> tuple[float, float]:
    tup = enter.split()
    if len(tup) != 2:
        raise ValueError("Esperado dois números separados por espaço")
    return float(tup[0]), float(tup[1])


class Chatbot:
    def __init__(self,bot_name: str) -> None:
        self.bot_name = bot_name
        self.history: list[str] = []
        self.answers: dict[str,list[str]] = {
            "hi": ["Hi there!", "Hello!", "Hey, how can I help?"],
            "hello": ["Hi there!", "Hello!", "Hey, how can I help?"]
        }
        self.exits: set[str] = {"bye","goodbye","see you"}
        self.arithmetic = {"+": add, "-": sub, "*": mul, "/": div}
        
    
    def show_history(self) -> None:
        for hist in self.history:
            print(hist)
    
    def responder(self, user_input: str) -> bool:
      self.history.append(f"You: {user_input}")

      if user_input in self.exits:
        print(f"{self.bot_name}: Goodbye! Have a great day! ")
        return False    # sinaliza "sai do loop"
      elif user_input in self.answers:
        resposta = random.choice(self.answers[user_input])
        print(resposta)
        self.history.append(f"{self.bot_name}: {resposta}")
        return True
      elif user_input in self.arithmetic:
        print(f"{self.bot_name}: Sure! Let's do some {self.arithmetic[user_input].__name__}! Please enter two numbers")
        self.history.append(f"{self.bot_name}: Sure! Let's do some {self.arithmetic[user_input].__name__}! Please enter two numbers")
        try:
            numbers: str = input("Two numbers (space-separated): ")
            num1, num2 = parse_two_numbers(numbers)
            print(f"{self.bot_name}: The {self.arithmetic[user_input].__name__} is {self.arithmetic[user_input](num1,num2)}")
            self.history.append(f"{self.bot_name}: The {self.arithmetic[user_input].__name__} is {self.arithmetic[user_input](num1,num2)}")
            return True
        except ValueError:
            print(f"{self.bot_name}: Oops! That doesn't sem like a valid number. Try again!")
            self.history.append(f"{self.bot_name}: Oops! That doesn't sem like a valid number. Try again!")
            return True
      elif user_input == "history":
        self.show_history()
        return True
      else:
        print(f"{self.bot_name}: I'm sory, I don't understand that, Please try again.")
        self.history.append(f"{self.bot_name}: I'm sory, I don't understand that, Please try again.")
        return True

bot: Chatbot = Chatbot("Bob")
while True:
    user_input: str = input('You: ').lower()
    if not bot.responder(user_input):
        break