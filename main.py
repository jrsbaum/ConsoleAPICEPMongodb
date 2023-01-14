import re
from pymongo import MongoClient
from db import get_address_by_cep

def get_endereco_por_cep(cep):
    data = get_address_by_cep(cep)

    if "cep" not in data or "logradouro" not in data or "bairro" not in data or "localidade" not in data or "uf" not in data:
        return None

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
    cep = input("Por favor, digite um CEP ou digite 'sair' para sair: ")
    if cep == 'sair':
        break
    elif not re.match("^[0-9]{8}$", cep):
        print("CEP inválido. Por favor, tente novamente.")
    else:
        endereco = get_endereco_por_cep(cep)
        if endereco is None:
            print("CEP inválido. Por favor, tente novamente.")
        else:
            print(f"CEP: {endereco['cep']}")
            print(f"Logradouro: {endereco['logradouro']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Localidade: {endereco['localidade']}")
            print(f"UF: {endereco['uf']} \n")
            print(f"CEP {cep} registrado no sistema com sucesso.")
