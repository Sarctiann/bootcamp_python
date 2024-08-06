from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import mod

app = FastAPI(title="Nuestra primer App")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        context={"mensaje": mod.text, "request": request},
    )


obj = dict(
    mensaje="hola mundo",
    descripcion="mi primer app",
    existe=None,
    booleano=True,
    tupla={1, 2, 3},
)


def hola():
    return "hola"


@app.get("/about")
async def about():
    return hola
