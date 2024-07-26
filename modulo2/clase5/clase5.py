"""
Este archivo contiene el código de ejemplo de la clase5.

Al final del mismo contiene unas consignas para resolver,
luego ejecute los test, para verificar las soluciones.
"""

# By convention, import statements should be at the top of the file
# We will use this later
from copy import deepcopy

# Mutable vs Immutable

li = ["ten", "two", "three"]  # list

# Change the first element successfully
li[0] = "one"


# ----------------------------

di = {"one": 1, "two": 2}  # dict

# Add a new key-value pair successfully
di["three"] = 3

# ----------------------------

se = {1, 2, 3}  # set

# Add a new element successfully
se.add(4)

# ----------------------------

tu = (10, 2, 3)  # tuple

# Tryin to change the first element unsuccessfully

try:
    # You will get a TypeError here... don't worry we are handling it
    tu[0] = 1  # type: ignore # noqa
except TypeError:
    tu = (1, *tu[1:])
finally:
    pass


print("Colecciones resultantes:", li, di, se, tu, sep="\n\t")
# -----------------------------------------------------------------------------

# Comprehensions

lii = [i for i in range(3)]

dii = {k: v for k, v in zip(li, lii)}

see = {i for i in dii}

# Generator comprehension (this returns the generator object)

gen = (i for i in tu)

print("Objetos resultantes:", lii, dii, see, gen, sep="\n\t")

# -----------------------------------------------------------------------------

# -------------------- Indexing ---------------------

elements = [i for i in range(100)]
dictionary = {str(i): i for i in elements}

# Get tge fifth element
print(elements[4])

# Get the last element
print(elements[-1])

# Same with the dictionary but using the key
print(dictionary["4"])
print(dictionary["99"])

# --------------------- Slicing [:]------------------

# Get the first 10 elements
print(elements[:10])

# Omit the first 50 elements
print(elements[50:])

# Get the elements from 10 to 20 (inclusive)
print(elements[10:21])

# -----------------------------------------------------------------------------

# copy (shallow) and deep copy

prices = [100, 200, 300]

db1 = {"prices": prices}
print("Precios inicializados:", db1["prices"])

shallow_copy = db1.copy()

shallow_copy["prices"][0] = 150
print("Precios modificados:", shallow_copy["prices"])

# Trying to acces the original prices
print("Precios originales ?:", db1["prices"])
print("¿QUE PASÓ?, lista de precios original ?:", prices)

# -----------------------------------------------------------------------------


prices = [100, 200, 300]

db1 = {"prices": prices}
print("Precios inicializados:", db1["prices"])

deep_copy = deepcopy(db1)

deep_copy["prices"][0] = 150
print("Precios modificados:", deep_copy["prices"])

# Trying to acces the original prices
print("Precios originales ?:", db1["prices"], "OK!")

# -----------------------------------------------------------------------------

# assert and raise expressions

condition1 = 1 == 1
condition2 = 1 == 2

error_message = "This is an error message"

assert condition1, error_message

# This will raise an AssertionError
# assert condition2, error_message


map = {"key1": "value1", "key2": "value2", "key3": "value3"}


def restrictive_map(key):
    if key not in map:
        raise KeyError(
            'Esta función solo toma los valores "key1", "key2" o "key3"',
        )
    return map[key]


print(restrictive_map("key1"))

# This will raise a KeyError
# print(restrictive_map("key4"))

# -----------------------------------------------------------------------------

"""
Consignas:

1. Crear una función llamada `get_first_element` que reciba una lista y retorne
    el primer elemento de la lista.

2. Crear una función llamada `make_dict` que reciba dos listas, una de claves y 
    otra de valores, y retorne un diccionario con las claves y valores correspondientes.

3. Dado un diccionario con la estructura {"precios": [100, 200, 300]}.

    A. Crear una función llamada `reset_price` que reciba el diccionario y un índice,
        modifique el precio en la posición indicada por el índice a 0.
    
    B. Crear una función llamada `backup_prices` que reciba el diccionario
        y retorne una copia profunda del mismo, en donde debe incluir la clave 
        "prices_origin" con la lista de precios original.

"""
