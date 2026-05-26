import json
import csv

DOMINIO: dict[str,int] = {}

def extrai_dominio_ativo(linha: dict[str,str]) -> str | None:
    if "Ativo" in linha["status"]:
        return linha["dominio"]
    return None

def cria_dominio(dominio: str) -> None:
    DOMINIO[dominio] = 1

def incrementa_dominio(dominio: str) -> None:
    DOMINIO[dominio] += 1

def decide(dominio: str) -> None:
    if dominio in DOMINIO:
        incrementa_dominio(dominio)
        return
    cria_dominio(dominio)

def escreve_resumo() -> None:
    with open("resumo_dominios.json","w",encoding="utf-8") as f:
        json.dump(DOMINIO,f,indent=2,ensure_ascii=False)

def main():
    with open("nanda-i-2024-2026.csv","r",encoding="utf-8",newline="") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            dominio: str | None = extrai_dominio_ativo(linha)
            if dominio is None:
                continue
            decide(dominio)
    escreve_resumo()

main()