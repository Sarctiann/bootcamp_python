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


# FAKE DATABASE ----------------------------------------------------------------

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

iid = len(products)

# ------------------------------------------------------------------------------


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

    Además también vamos a obtener la documentación necesaria en Swagger.

    """
    global iid
    # De esta manera le decimos a python que estamos usando una variable
    # global iid

    try:
        iid += 1
        products.append(Product(id=iid, **product.model_dump()))
    except Exception as e:
        return {"Error": str(e)}
    return {"Success": f"Product created with id {product.id}"}
