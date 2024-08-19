"""
This script requires the file ADMIN_USER_CONF to be in the same directory as the 
script. Or you can set the username, email and password environment variables.
"""

import os

from api.models import CreationUser
from api.services import AuthService, UsersService

try:
    with open("scripts/ADMIN_USER_CONF", "r") as f:
        print("Reading the config file...")
        lines = f.read().splitlines()
        data = dict(line.split("=") for line in lines)
except FileNotFoundError:
    data = dict(
        username=os.environ.get("username"),
        email=os.environ.get("email"),
        password=os.environ.get("password"),
    )

insertion_user = CreationUser.model_validate(data)
hash_password = AuthService.get_password_hash(insertion_user.password)

print("Creating super user...")
result = UsersService.create_one(insertion_user, hash_password=hash_password, make_it_admin=True)

print(f"Super user: {data["username"]} created with id: {result}")
