import requests

def get_address_by_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()
