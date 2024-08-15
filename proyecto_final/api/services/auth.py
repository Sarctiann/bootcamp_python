__all__ = []


from ..config import COLLECTIONS


class UsersService:
    assert (collection_name := "products") in COLLECTIONS
    collection = db[collection_name]
