from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from ..config import MONGODB_URI, COLLECTIONS

uri = MONGODB_URI

__all__ = ["db"]

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))


# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client.bootcamp_eCommerce_app

# Create Collections (optional)
print("Initializing collections...")
for collection in COLLECTIONS:
    if collection not in db.list_collection_names():
        db.create_collection(collection)
        print(f"\tCollection '{collection}' created.")
    else:
        print(f"\tCollection '{collection}' already exists.")
