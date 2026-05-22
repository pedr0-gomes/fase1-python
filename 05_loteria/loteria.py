import random

CUSTOS: dict[int,float] = {
    3 : 1.0,
    4 : 1.5,
    5 : 2.0
}

PREMIOS: dict[int,dict[int,float]] = {
    3 : {0 : 0, 1 : 0.2, 2 : 2.5, 3 : 35},
    4 : {0 : 0, 1 : 0.2, 2: 0.5, 3 : 5, 4 : 80}, 
    5 : {0 : 0, 1 : 0, 2 : 0.25, 3 : 1, 4 : 8, 5 : 90}
}

POOL: list[int] = [1,2,3,4,5,6,7,8,9,10]

def custo(quantidade: int) -> float:
    return CUSTOS[quantidade]

def calcular_premio(quantidade: int, acertos: int) -> float:
    return PREMIOS[quantidade][acertos]

def sortear_numeros(quantidade: int) -> set[int]:
    return set(random.sample(POOL,quantidade))

def contar_acertos(escolhidos: set[int], sorteados: set[int]) -> int:
    return len(escolhidos & sorteados)

def pedir_saldo_inicial() -> float:
    while True:
        try:
            saldo: float = float(input("O quanto você tem disponível para apostar? R$"))
        except ValueError:
            print("Não é número, tente de novo.")
            continue
        if saldo <= 0:
            print("Saldo precisa ser positivo.")
            continue
        return saldo
    
def pedir_quantidade(saldo: float) -> int | None:
    while True:
        quantidade: str = input("Deseja apostar quantos números (3/4/5/q) — se q, termina:  ").lower()
        if quantidade == 'q':
            return None
        try:
            n: int = int(quantidade)
        except ValueError:
            print("Entrada inválida. Digite novamente.")
            continue
        if n not in {3,4,5}:
            print("Quantidade inválida. Digite novamente")
            continue
        if saldo < custo(n):
            print("Você não tem saldo suficiente para apostar essa quantidade. Digite outra opcao")
            continue
        return n
    
def escolher_numeros(quantidade: int) -> set[int]:
    escolhidos: set[int] = set()
    print(f"## Escolha {quantidade} números ##")
    while len(escolhidos) < quantidade:
        try:
            n: int = int(input("Escolha um número: "))
        except ValueError:
            print("Entrada Inválida. Digite novamente")
            continue
        if n not in POOL:
            print("Digito fora da pool. Digite novamente")
            continue
        if n in escolhidos:
            print("Esse número já foi escolhido. Digite outro número.")
            continue
        escolhidos.add(n)
    return escolhidos
        
def mostrar_resultado(quantidade: int,acertos: int,premio: float,saldo: float) -> None:
    print("## TABELA DE RESULTADO ##")
    print(f"Quantidade de números escolhidos: {quantidade}")
    print(f"Número de acertos: {acertos}")
    print(f"Ganho: R${premio:.2f}")
    print(f"Saldo: R${saldo:.2f}")

def main():
    print("Boas Vindas a Loterica do Pedro")
    saldo: float = pedir_saldo_inicial()
    while saldo >= 1:
        quantidade: int = pedir_quantidade(saldo)
        if quantidade is None:
            break
        saldo -= custo(quantidade)
        escolhidos: set[int] = escolher_numeros(quantidade)
        sorteados: set[int] = sortear_numeros(quantidade)
        acertos: int = contar_acertos(escolhidos,sorteados)
        premio = calcular_premio(quantidade,acertos)
        saldo += premio
        mostrar_resultado(quantidade,acertos,premio,saldo)
    print("Até mais...")


main()