__all__ = ["MONGODB_URI", "logger", "SECRET_KEY"]

import logging
import os

from dotenv import load_dotenv

# Cargamos nuestras variables de entorno
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_CONNECTION_STRING")
if not MONGODB_URI:
    raise Exception("MongoDB connection string not found")

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("Secret key not found")

logger = logging.getLogger("uvicorn")
# logger.setLevel(logging.DEBUG)

# Fixing a "bycript issue"
logging.getLogger("passlib").setLevel(logging.ERROR)
