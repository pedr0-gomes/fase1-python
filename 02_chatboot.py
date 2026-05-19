# ============================================================
# 02_chatboot.py - Memória e mapeamento
# Tema: coleções (dict, list, set) + Final + for
# ============================================================
#
# TAREFA 02.1 - Dicionário de respostas
#   - Criar `respostas: dict[str, str]` no topo, mapeando comando -> resposta.
#   - Substituir os `elif` de saudação/despedida triviais por:
#       if entrada in respostas:
#           print(respostas[entrada])
#   - Manter o `elif` da soma e o `else` do fallback.
#   - Pronto quando: bot responde "hi", "hello", "bye" via lookup.
#   - Commit:
#       git add 02_chatboot.py
#       git commit -m "exercise(02): replace if/elif chain with dict lookup for responses"
#
# TAREFA 02.2 - Histórico com list + for
#   - Criar `historico: list[str] = []`.
#   - A cada turno do loop: `.append` da entrada do usuário E da resposta do bot.
#   - Adicionar comando "history" que itera com `for` e imprime todas as mensagens.
#   - Pronto quando: digitar "history" mostra a conversa em ordem.
#   - Commit:
#       git add 02_chatboot.py
#       git commit -m "exercise(02): add conversation history with list and for-loop"
#
# TAREFA 02.3 - Constantes com Final + set
#   - No topo: `from typing import Final`.
#   - Declarar `SAIDAS: Final[set[str]] = {"bye", "goodbye", "see you"}`.
#   - Substituir o `in [...]` da despedida por `in SAIDAS`.
#   - Pronto quando: palavras de saída num único lugar, em CAPS, tipadas como Final[set[str]].
#   - Commit:
#       git add 02_chatboot.py
#       git commit -m "exercise(02): declare exit keywords as Final[set[str]] constant"
#
# Ao final das 3 tarefas, atualizar README.md e commitar:
#   git add README.md
#   git commit -m "docs: log completion of 02_chatboot (collections)"
# ============================================================


# Referências de estudo (vindas do 01):
# link 1: https://youtu.be/8KCuHHeC_M0?si=qiskmxx-k4T6EVwN
# link 2: https://www.youtube.com/watch?v=Ro_MScTDfU4
# link 3: https://youtu.be/Gx5qb1uHss4?si=LtpBNIB6yST3Vlcq


answers: dict[str,str]
answers["hi"] = "Hi there! How can I help you?"
answers["hello"] = "Hi there! How can I help you?"
answers["bye"] = "Goodbye! Have a great day!"
answers["see you"] = "Goodbye! Have a great day!?"

bot_name: str = "Bob"
print(f"Hello! I'm {bot_name}! How can I assist you today?")

while True:
    user_input: str = input('You: ').lower()

    if user_input in answers:
        print(answers[user_input])
    elif user_input in ["+", "add"]:
        print(f"{bot_name}: Sure! Let's do some addition! Please enter two numbers")
        try:
            num1: float = float(input("First number: "))
            num2: float = float(input("Second number: "))
            print(f"{bot_name}: The sum is {num1 + num2}")
        except ValueError:
            print(f"{bot_name}: Oops! That doesn't sem like a valid number. Try again!")
    else:
        print(f"{bot_name}: I'm sory, I don't understand that, Please try again.")
