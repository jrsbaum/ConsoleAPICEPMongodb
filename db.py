from pymongo import MongoClient
from cfg import mongo_client_key

def insert_endereco_to_mongodb(endereco):
    try:
        client = MongoClient(mongo_client_key)
        db = client.CEPS
        enderecos = db.enderecos
        enderecos.insert_one(endereco)
    except Exception as e:
        print(f"An error occurred while trying to insert the data in MongoDB: {e}")
