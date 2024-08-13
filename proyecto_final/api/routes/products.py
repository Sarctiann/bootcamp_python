from fastapi.routing import APIRouter

from ..database.products import product_collection
from ..models import Product

products = []
iid = 0

__all__ = ["product_router"]


product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/products")
def list_products(products: product_collection):
    return products.find()


@product_router.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product.get("id") == id:
            return product
    return {"Error": "Product not found"}


@product_router.post("/products")
def create_product(product: Product):
    """
    Con simplemente declarar el tipo de nuestro parametro (`product: Product`)
    fastapi se va aencargar de validar nuestra data!

    Además también vamos a obtener la documentación necesaria en Swagger.

    """
    try:
        global iid
        iid += 1
        # De esta manera le decimos a python que estamos usando una variable
        # global iid

        product_dict = product.model_dump()  # en la docu: .dict()
        product_dict.update({"id": iid})
        products.append(product_dict)

    except Exception as e:
        return {"Error": str(e)}

    return {"Success": f"Product created with id {product_dict.get('id')}"}
