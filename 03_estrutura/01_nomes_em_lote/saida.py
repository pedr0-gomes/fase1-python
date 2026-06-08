import csv

def grava(resultados: dict,doc: str) -> None:
    with open(doc,"w",encoding="utf-8",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=["nome","frequencia"])
        writer.writeheader()
        for nome,freq in resultados .items():
            line = {"nome": nome,"frequencia": freq}
            writer.writerow(line)