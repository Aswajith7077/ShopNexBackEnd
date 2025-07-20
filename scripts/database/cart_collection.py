from pymongo import ASCENDING, MongoClient

from config.database import client


def update_cart_config():

    try:

        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")

        db = client["ShopNex"]
        user_collection = db["USER"]

        # Drop existing index (optional if already dropped)
        try:
            user_collection.drop_index("cart.product_id_1")
            print("Dropped existing index.")
        except Exception as e:
            print(f"Index not found or already dropped: {e}")

        # Create partial index to enforce uniqueness only when product_id is not null
        user_collection.create_index(
            [("cart.product_id", ASCENDING)],
            unique=True,
            partialFilterExpression={"cart.product_id": {"$exists": True, "$ne": None}},
        )
        print("Created partial unique index on cart.product_id")

    except Exception as e:
        print(e)
