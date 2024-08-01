from fastapi import FastAPI

from .routes import roles_router

app = FastAPI()
app.title = "Final Project API"


@app.get("/")
def home():
    return {"message": "Hello, World!"}


app.include_router(roles_router, prefix="/roles", tags=["Roles"])
