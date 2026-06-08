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
        
def consulta(nome: str) -> int:
    res = busca_com_retry(nome)
    if res is None:
        return 0
    cont: int = 0
    for i in res:
        cont += i["frequencia"]
    return cont
