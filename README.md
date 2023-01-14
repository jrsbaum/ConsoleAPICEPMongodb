#### Para o código funcionar, precisa de um arquivo que não foi versionado por questões de segurança. 
#### O arquivo contém o seguinte código:

``` 
from pymongo import MongoClient

def insert_endereco_to_mongodb(endereco):
    try:
        client = MongoClient("chave_do_mongoDB")
        db = client.CEPS
        enderecos = db.enderecos
        enderecos.insert_one(endereco)
    except Exception as e:
        print(f"An error occurred while trying to insert the data in MongoDB: {e}")
```

### Substitua chave_do_mongoDB pela sua.
