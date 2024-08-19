from api.config import COLLECTIONS, db


def create_collections():
    print("Initializing collections...")
    for collection in COLLECTIONS:
        if collection not in db.list_collection_names():
            db.create_collection(collection)
            print(f"\tCollection '{collection}' created.")
        else:
            print(f"\tCollection '{collection}' already exists.")
    print()


if __name__ == "__main__":
    create_collections()
