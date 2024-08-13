import os
from dotenv import load_dotenv
import logging

__all__ = ["MONGODB_URI", "COLLECTIONS", "logger"]

# Loads the environment variables
load_dotenv()  # If we don't pass it will looks for ".env" file name
load_dotenv(".secret")

MONGODB_PASS = os.getenv("MONGODB_PASS", "")
MONGODB_URI = os.getenv("MONGODB_CONN_STR", "").replace("<password>", MONGODB_PASS)

COLLECTIONS = ["products", "users", "roles"]

logger = logging.getLogger("uvicorn")
# logger.setLevel(logging.DEBUG)
