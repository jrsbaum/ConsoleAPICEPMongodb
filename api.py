import requests
from cfg import url_api


def get_res_api(cep):
    url = f"{url_api}{cep}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()
