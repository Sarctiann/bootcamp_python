from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .api.routes import api_router


app = FastAPI(title="Final Project API")
app.include_router(api_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context=dict(
            title="Final Project API",
            description='Go to "/docs" for API documentation',
        ),
    )
