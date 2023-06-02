from pymongo import MongoClient

def get_collection():
    client = MongoClient("mongodb://localhost:27017/")
    database = client["Automatized_Test"]

    collection = database["test"]

    return collection