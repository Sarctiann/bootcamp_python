__all__ = [
    "MONGODB_URI",
    "logger",
    "SECRET_KEY",
    "HOST_URL",
    "HOST_PORT",
    "FRONTEND_HOST",
]

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

HOST_URL = os.getenv("HOST_URL")
if not HOST_URL:
    raise Exception("Host url not found")

FRONTEND_HOST = os.getenv("FRONTEND_HOST")
if not FRONTEND_HOST:
    raise Exception("Frontend host not found")

HOST_PORT = int(os.getenv("HOST_PORT") or 8000)

logger = logging.getLogger("uvicorn")
# logger.setLevel(logging.DEBUG)

# Fixing a "bycript issue"
logging.getLogger("passlib").setLevel(logging.ERROR)
