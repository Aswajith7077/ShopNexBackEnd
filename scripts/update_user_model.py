from config.database import client


def update_user_model():

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        # Connect to your database and collection
        db = client["ShopNex"]  # Replace with your database name
        user_collection = db["USER"]  # Replace with your collection name

        user_collection.update_many(
            {},
            {
                "$set": {
                    "lastlogin": "2023-10-01T00:00:00+00:00"  # Set a default value for lastlogin
                }
            },
        )

    except Exception as e:
        print(e)
