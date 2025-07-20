import jwt
from passlib.context import CryptContext

from config.config import (
    jwt_access_token_secret_key,
    jwt_encode_algorithm,
    jwt_refresh_token_secret_key,
)
from config.database import user_collection

pwd_context = CryptContext(schemes=["bcrypt"])


class CurrentUser:

    async def get_current_user_by_access_token(self, token: bytes):
        result = jwt.decode(
            token, key=jwt_access_token_secret_key, algorithms=[jwt_encode_algorithm]
        )
        return result

    async def get_current_user_by_refresh_token(self, token: bytes):
        result = jwt.decode(
            token, key=jwt_refresh_token_secret_key, algorithms=[jwt_encode_algorithm]
        )
        return result


class Authenticate:

    def generate_access_token(self, data: dict):
        return jwt.encode(
            data, key=jwt_access_token_secret_key, algorithm=jwt_encode_algorithm
        )

    def generate_refresh_token(self, data: dict):
        return jwt.encode(
            data, key=jwt_refresh_token_secret_key, algorithm=jwt_encode_algorithm
        )

    async def user_in_db(self, username):
        try:
            result = list(user_collection.find({"username": username}))
            if not len(result):
                return None
            return result[0]
        except Exception as e:
            return None

    def check_password(self, login_password, actual_password):
        return pwd_context.verify(login_password, actual_password)

    def generate_hash(self, text: str):
        return pwd_context.hash(text)

    async def authenticate_user(self, username: str, password: str):

        result = await self.user_in_db(username)
        if result is None:
            return None
        elif not self.check_password(password, result["password"]):
            return None
        else:
            return result
