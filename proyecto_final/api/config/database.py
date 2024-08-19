__all__ = ["db", "COLLECTIONS"]

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from .__base_config import MONGODB_URI, logger

DB_NAME = "bootcamp_eCommerce_app"
COLLECTIONS = ["products", "users", "orders"]

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))


# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    logger.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client[DB_NAME]
