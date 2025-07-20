from datetime import datetime, timezone

from config.database import user_collection
from models.users import User
from services.application.auth import Authenticate

a = Authenticate()


async def insert_user(form_data: User, expire_time: datetime = None):
    if not expire_time:
        expire_time = datetime.now(timezone.utc)
    try:
        user_collection.insert_one(
            {
                "username": form_data.username,
                "fullname": form_data.fullname,
                "email": form_data.email,
                "password": a.generate_hash(form_data.password),
                "lastlogin": expire_time,
            }
        )
        return True, None
    except Exception as e:
        return False, str(e)


async def find_single_user(id: str):

    try:
        results = user_collection.find_one({"username": id})
        return results, None
    except Exception as e:
        return None, e


async def update_user(username: str, form_data: User, expire_time: datetime = None):

    try:
        user_collection.update_one(
            {"username": username},
            {"$set": {**form_data.dict(), "lastlogin": expire_time}},
        )
        return True, None

    except Exception as e:
        return False, e.args
