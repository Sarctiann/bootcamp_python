import logging
import os

from dotenv import load_dotenv

__all__ = ["MONGODB_URI", "logger", "COLLECTIONS"]

# Cargamos nuestras variables de entorno
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_CONNECTION_STRING")
if not MONGODB_URI:
    raise Exception("MongoDB connection string not found")

COLLECTIONS = ["products"]

logger = logging.getLogger("uvicorn")
# logger.setLevel(logging.DEBUG
