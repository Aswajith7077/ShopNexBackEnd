from pymongo import MongoClient

from config.config import (
    collection_cart,
    collection_product,
    collection_promotion,
    collection_user,
    db_name,
    db_url,
)

client = None
db = None

user_collection = None
product_collection = None
cart_collection = None
promotion_collection = None


try:
    client = MongoClient(db_url)

    db = client[db_name]

    user_collection = db[collection_user]
    product_collection = db[collection_product]
    cart_collection = db[collection_cart]
    promotion_collection = db[collection_promotion]

    print("Connection Successfull")
    # print(list(product_collection.find().limit(10)))
except Exception as e:

    print("Mongo DB Error : ", e)
