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

### Para o código funcionar, precisa de um arquivo cfg.py que não foi versionado por questões de segurança.

### O arquivo contém o seguinte código:

```
mongo_client_key = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]"
url_api = "https://url_de_exemplo.com.br/ws/"
```

#### Substitua o valor de `mongo_cliente_key` pela sua chave no MongoDB.
#### Substitua o valor de `url_api` pela api que será usada.