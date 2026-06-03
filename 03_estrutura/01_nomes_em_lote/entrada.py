#  1. Ler o CSV — igual você já fez: with open(...) + csv.DictReader, pegando a coluna nome.
#  2. Normalizar — deixar cada nome num formato único. (Ex.: tirar espaços nas pontas, padronizar maiúscula/minúscula.) Por quê: a API do IBGE e o dedupe dependem de "Maria", " maria " e
#  "MARIA" virarem a mesma coisa.
#  3. Validar — descartar lixo: linha vazia, nome só com espaços, etc.
#  4. Dedupe — remover repetidos. Por quê: não vale a pena bater na API duas vezes pro mesmo nome.

import csv

def validar(linha: str) -> bool:
    if linha.strip():
        return True
    return False

def normalizar(linha: str) -> str:
    return linha.upper().strip()


def ler(doc: str) -> set:
    resultado: set = set()
    with open(doc,"r",encoding="utf-8",newline="") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            if (validar(linha["nome"])):
                resultado.add(normalizar(linha["nome"]))            
    return resultado
