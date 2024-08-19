from api.models import CreationUser, Order, Product
from api.services import AuthService, OrdersService, ProductsService, UsersService

# Create two basic users

users = [
    {
        "username": "Vendedor1",
        "email": "a@a.com",
        "password": "123",
        "role": "seller",
    },
    {
        "username": "Vendedor2",
        "email": "c@c.com",
        "password": "123",
        "role": "seller",
    },
    {
        "username": "Comprador",
        "email": "b@b.com",
        "password": "123",
        "role": "customer",
    },
]

print("Creating users...")
users_ids = []
for user in users:
    hash_password = AuthService.get_password_hash(user["password"])
    insertion_user = CreationUser.model_validate(user)
    result_id = UsersService.create_one(insertion_user, hash_password=hash_password)
    users_ids.append(result_id)

# Create some products

products = [
    {
        "seller_id": users_ids[0],
        "name": "Product 1",
        "description": "Product 1 description",
        "price": 100,
        "quantity": 10,
    },
    {
        "seller_id": users_ids[0],
        "name": "Product 2",
        "description": "Product 2 description",
        "price": 200,
        "quantity": 20,
    },
    {
        "seller_id": users_ids[0],
        "name": "Product 3",
        "description": "Product 3 description",
        "price": 300,
        "quantity": 30,
    },
    {
        "seller_id": users_ids[0],
        "name": "Product 4",
        "description": "Product 4 description",
        "price": 400,
        "quantity": 40,
    },
    {
        "seller_id": users_ids[0],
        "name": "Product 5",
        "description": "Product 5 description",
        "price": 500,
        "quantity": 50,
    },
    {
        "seller_id": users_ids[0],
        "name": "Product 6",
        "description": "Product 6 description",
        "price": 600,
        "quantity": 60,
    },
    {
        "seller_id": users_ids[1],
        "name": "Product 7",
        "description": "Product 7 description",
        "price": 700,
        "quantity": 70,
    },
    {
        "seller_id": users_ids[1],
        "name": "Product 8",
        "description": "Product 8 description",
        "price": 800,
        "quantity": 80,
    },
    {
        "seller_id": users_ids[1],
        "name": "Product 9",
        "description": "Product 9 description",
        "price": 900,
        "quantity": 90,
    },
    {
        "seller_id": users_ids[1],
        "name": "Product 10",
        "description": "Product 10 description",
        "price": 1000,
        "quantity": 100,
    },
]


print("Creating products...")
product_ids = []
for product in products:
    insertion_product = Product.model_validate(product)
    result_id = ProductsService.create_one(insertion_product)
    product_ids.append(result_id)

# Create some orders

orders = [
    {
        "customer_id": users_ids[2],
        "product_id": product_ids[9],
        "price": 900,
        "quantity": 1,
    },
    {
        "customer_id": users_ids[2],
        "product_id": product_ids[5],
        "price": 496,
        "quantity": 2,
    },
]

print("Creating orders...")
for order in orders:
    insertion_order = Order.model_validate(order)
    OrdersService.create_one(insertion_order)

print("Done!")
