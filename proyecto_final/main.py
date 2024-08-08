from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .models import Product


app = FastAPI(title="Final Project API")

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


# esta lista emula nuestra base de datos, por el momento
pelis = [
    {"id": 1, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Harry Potter", "author": "J.K. Rowling"},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
]


@app.get("/pelis")
def list_pelis():
    return pelis


@app.get("/pelis/{id}")
def get_peli(id: int):
    """
    Esta función retorna la peli que coincida con el id
    comopodemos ver, le estamos pasando el id tanto por parámetro como en la url
    como a la función.

    Args:
        id (int): el id de la peli
    """
    for peli in pelis:
        if peli["id"] == id:
            return peli

    return {"Error": "Peli no encontrada"}


products = [
    Product(
        id=1, name="Product 1", description="Description 1", price=13.0, quantity=50
    ),
    Product(
        id=2, name="Product 2", description="Description 2", price=22.0, quantity=20
    ),
    Product(
        id=3, name="Product 3", description="Description 3", price=42.0, quantity=15
    ),
]


@app.get("/products")
def list_products():
    return products


@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"Error": "Product not found"}


@app.post("/products")
def create_product(product: Product):
    """
    Con simplemente declarar el tipo de nuestro parametro (`product: Product`)
    fastapi se va aencargar de validar nuestra data!

    """
    products.append(product)
