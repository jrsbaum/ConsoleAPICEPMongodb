import requests
from pymongo import MongoClient

def get_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()

    endereco = {
        "cep": data["cep"],
        "logradouro": data["logradouro"],
        "bairro": data["bairro"],
        "localidade": data["localidade"],
        "uf": data["uf"]
    }
    try:
        client = MongoClient("mongodb+srv://dbUserJrs:ItXYBOph51vcXK1N@cluster0.23sjuth.mongodb.net/?retryWrites=true&w=majority")
        db = client.CEPS
        enderecos = db.enderecos
        enderecos.insert_one(endereco)
    except Exception as e:
        print(f"An error occurred while trying to insert the data in MongoDB: {e}")
    return endereco


while True:
    cep = input("Por favor, digite um CEP: ")
    if cep is None:
        print("CEP invÃ¡lido. Por favor, tente novamente.")
    else:
        endereco = get_endereco_por_cep(cep)
        if endereco is None:
            print("CEP invÃ¡lido. Por favor, tente novamente.")
        else:
            print(f"CEP: {endereco['cep']}")
            print(f"Logradouro: {endereco['logradouro']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Localidade: {endereco['localidade']}")
            print(f"UF: {endereco['uf']}")
            break