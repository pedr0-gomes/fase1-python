import requests

class UsuarioDesistiu(Exception):
    pass

def chama_API(nome: str) -> list | None:
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    resposta = requests.get(url,timeout=10)    
    resposta.raise_for_status()
    dados = resposta.json()
    if not dados:
        return None
    return dados[0]["res"]

def busca_com_retry(nome: str) -> list | None:
    while True:
        try:
            dados = chama_API(nome)
            return dados
        except requests.exceptions.RequestException:
            escolha = input("Tivemos um erro! Você gostaria de tentar novamente? (s/n)").lower()
            if escolha == "s":
                continue
            raise UsuarioDesistiu()

def main():
    nome: str = input("Digite o nome do usuário que você quer que eu busque: ")
    try:
        resultado: list | None = busca_com_retry(nome)
        if resultado is None:
            print("Não há dados disponíveis para esse nome")
        else:
            print(f"## Resultado do Nome {nome} ##")
            print(resultado)
    except UsuarioDesistiu:
        print(f"Estou à disposição caso queira buscar o nome {nome} em outro momento!")

main()    