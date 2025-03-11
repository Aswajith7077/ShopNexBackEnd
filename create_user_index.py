
from pymongo import MongoClient
from datetime import datetime
from config.config import db_url, db_name, collection_user

try:
    client = MongoClient(db_url)
    db = client[db_name]
    collection = db[collection_user]

    collection.create_index(["username"],unique = True)

except Exception as e:
    print(f"Connection Failed : \n\n", e)