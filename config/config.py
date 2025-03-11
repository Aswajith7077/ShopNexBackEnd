from dotenv import load_dotenv
import os


load_dotenv()


def strip_out_quotations(result:str):
    return result[1:-1]

jwt_encode_algorithm = strip_out_quotations(os.getenv("JWT_ENCODE_ALGORITHM"))
jwt_access_token_secret_key = strip_out_quotations(os.getenv("JWT_ACCESS_TOKEN_SECRET_KEY"))
jwt_refresh_token_secret_key = strip_out_quotations(os.getenv("JWT_REFRESH_TOKEN_SECRET_KEY"))
jwt_access_token_expiry_time_minutes:int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_TIME_MINUTES"))
jwt_refresh_token_expiry_time_minutes:int = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_TIME_MINUTES"))

db_url = strip_out_quotations(os.getenv("DB_URL"))
db_password = strip_out_quotations(os.getenv("DB_PASSWORD"))
db_user = strip_out_quotations(os.getenv("DB_USER"))
db_host = strip_out_quotations(os.getenv("DB_HOST"))
db_name = strip_out_quotations(os.getenv('DB_NAME'))

collection_product = strip_out_quotations(os.getenv("COLLECTION_PRODUCTS"))
collection_user = strip_out_quotations(os.getenv("COLLECTION_USER"))
collection_cart = strip_out_quotations(os.getenv("COLLECTION_CART"))
collection_promotion = strip_out_quotations(os.getenv("COLLECTION_PROMOTION"))





