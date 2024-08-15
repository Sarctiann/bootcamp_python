__all__ = ["token_expiration_time", "allowed_origins"]

from datetime import timedelta

token_expiration_time = timedelta(days=1)

allowed_origins = [
    "http://localhost",
    "http://localhost:8080",
]
