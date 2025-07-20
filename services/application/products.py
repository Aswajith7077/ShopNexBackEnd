import re
from datetime import datetime

from config.database import product_collection, user_collection
from models.products import SearchFormData
from models.users import User
from services.application.auth import Authenticate


async def get_products(limit: int = 10):

    try:
        result = list(
            product_collection.find({"CATEGORIES": "Electronics"}).limit(limit)
        )
        for i in range(len(result)):
            result[i].pop("_id")
            result[i].pop("INITIAL_PRICE")
            result[i].pop("DESC")
            result[i]["CATEGORIES"] = result[i]["CATEGORIES"][:2]
            result[i]["IMAGES"] = result[i]["IMAGES"][0]
            result[i].pop("VARIATIONS")
            result[i].pop("REFERAL_LINK")
            result[i].pop("DOMAIN")
            result[i].pop("SELLER_NAME")
            result[i].pop("FEATURES")
            result[i].pop("REVIEWS")
        return result
    except Exception as e:
        print(e)
        return e.args


async def retrive_product_details(id: str):

    try:

        result = product_collection.find_one({"NAME": id})
        result.pop("_id")
        return result
    except Exception as e:
        return e.args


async def search_product_details(form_data: SearchFormData):

    try:

        pattern = re.compile(".*" + form_data.search_text + ".*", re.IGNORECASE)
        names = product_collection.find({"NAME": pattern}).limit(10)
        brand = product_collection.find({"BRAND": pattern}).limit(10)
        categories = product_collection.find(
            {"CATEGORIES": {"$elemMatch": {"$regex": pattern}}}
        ).limit(10)
        sellers = product_collection.find({"SELLER_NAME": pattern}).limit(10)

        names = list(names)
        brand = list(brand)
        categories = list(categories)
        sellers = list(sellers)

        result = names + brand + sellers + categories

        for i in range(len(result)):
            result[i].pop("_id")
            result[i].pop("INITIAL_PRICE")
            result[i].pop("DESC")
            result[i]["IMAGES"] = result[i]["IMAGES"][0]
            result[i].pop("VARIATIONS")
            result[i].pop("REFERAL_LINK")
            result[i].pop("DOMAIN")
            result[i].pop("FEATURES")
            result[i].pop("REVIEWS")

        print("Result : ", len(names), len(brand), len(sellers))
        return result

    except Exception as e:
        return e
