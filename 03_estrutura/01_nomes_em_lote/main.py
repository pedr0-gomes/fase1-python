import entrada, ibge, saida

def main():
    nomes: set = entrada.ler("nomes.csv")
    resultados: dict = {}
    for nome in nomes:
        resultados[nome] = ibge.consulta(nome)
    saida.grava(resultados,"resultado.csv")
    print("Gravação de nomes concluída com sucesso!")

if __name__ == "__main__":
    main()  