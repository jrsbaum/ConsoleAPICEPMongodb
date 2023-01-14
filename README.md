# ConsoleAPICEPMongodb

### Descrição: consulta no console um CEP válido. Se existir e não tiver erro de digitação, imprime a consulta e salva no MongoDB.

## Documentação

```
    def get_res_api(cep):
```
Esta função recebe um número cep e retorna os dados do endereço no formato json
    obtido da API https://viacep.com.br/ws/{cep}/json. Se o cep for inválido ou
    o código de status da solicitação não for 200, ele retornará None.

```
    def insert_endereco_to_mongodb(endereco):
```   
Esta função recebe um dado de endereço e o insere no banco de dados MongoDB. Se ocorrer uma exceção, ele imprime uma mensagem de erro.

```
    def get_endereco_por_cep(cep):
```
Esta função recebe um número cep, obtém os dados de endereço da API, insere-o no banco de dados MongoDB e retorna os dados de endereço em um dicionário.



### Para o código funcionar, precisa de um arquivo que não foi versionado por questões de segurança.
### O arquivo contém o seguinte código:

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

### Substitua `chave_do_mongoDB` pela sua.
