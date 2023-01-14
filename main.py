import re
from api import get_res_api
from db import insert_endereco_to_mongodb

def get_endereco_por_cep(cep):
    data = get_res_api(cep)

    if "cep" not in data or "logradouro" not in data or "bairro" not in data or "localidade" not in data or "uf" not in data:
        return None

    endereco = {
        "cep": data["cep"],
        "logradouro": data["logradouro"],
        "bairro": data["bairro"],
        "localidade": data["localidade"],
        "uf": data["uf"]
    }

    insert_endereco_to_mongodb(endereco)
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
