"""
# Consigna única:
    tomando de ejemplo los test de la clase 2 y 3. escriba al menos un test
    para cada sección de este módulo.

### tenga en cuenta que el archivo debe llamarse "test_clase4.py" y cada función
    de test debe comenzar con "test_".

"""

# Vamos a necesitar esto para los decoradores
from functools import wraps

# -----------------------------------------------------------------------------

# A: Funciones comunes de todos los dias


def saludo1(nombre):

    print(f"Hola {nombre}! Bienvenido a la clase de Python!")


def saludo2(nombre: str) -> None:

    print(f"Hola {nombre}! Bienvenido a la clase de Python!")


def saludo3(nombre: str) -> None:
    """
    Función que recibe un nombre e imprime un saludo.
    ---
    Parameters:
        * nombre (str): Nombre de la persona a saludar.
    ---
    Returns:
        * str: Saludo a la persona.
    """

    print(f"Hola {nombre}! Bienvenido a la clase de Python!")


saludo3("Juan")


saludo3(nombre="Juan")

# Descomentar para probar el autocompletado al abrir parentesis.
# O la documentacion enlinea haciendo "hover" sobre el nombre de la función

# saludo3


help(saludo3)

# -----------------------------------------------------------------------------

# B: Funciones con parámetros opcionales (con valores por defecto)


def imprime_suma1(a: int, b: int = 0) -> None:

    print(f"La suma de {a} y {b} es {a+b}.")


imprime_suma1(5, 3)
imprime_suma1(5)

# -----------------------------------------------------------------------------

# C: Funciones con parámetros variables


def imprime_suma2(a: int, *args: int) -> None:

    suma = a
    for arg in args:
        suma += arg
    print(f"La suma es {suma}.")


imprime_suma2(1, 2)
imprime_suma2(1, 2, 3, 4, 5)
imprime_suma2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# -----------------------------------------------------------------------------

# D: Funciones con parámetros nombrados


def imprime_operacion(*args: int, verboso: bool = False, **kwargs) -> None:

    if verboso:
        print(f"Los argumentos posicionales son {args}.")
        print(f"Los argumentos nombrados son {kwargs}.")

    result = 0
    if kwargs.get("operacion") == "sumar" or kwargs.get("sumar"):
        #                            or kwargs.get["sumar"] is True
        #                            or kwargs.get("sumar", False)
        for arg in args:
            result += arg
        print(f"La suma es {result}.")

    if kwargs.get("operacion") == "multiplicar" or kwargs.get("multiplicar"):
        for arg in args:
            result *= arg
        print(f"La multiplicación es {result}.")

    if kwargs.get("operacion") == "dividir" or kwargs.get("dividir"):
        result = args[0]
        for arg in args[1:]:
            result /= arg
        print(f"La división es {result}.")


imprime_operacion()
imprime_operacion(1, 2, 3, 4, 5, verboso=True)
imprime_operacion(1, 2, 3, 4, 5, verboso=True, operacion="sumar")
imprime_operacion(1, 2, 3, 4, 5, multiplicar=True)


# -----------------------------------------------------------------------------

# E: Funciones con argumentos nombrados obligatorios


def imprime_division(*, dividendo: int, divisores: list[int]):
    """
    Función que recibe un dividendo y una lista de divisores y
    imprime el resultado de la división.
    ---
    Parameters:
        * dividendo (int): Número a dividir.
        * divisores (list[int]): Lista de números para dividir.
    """
    for divisor in divisores:
        print(f"El resultado de dividir {dividendo} entre {divisor} es", end=" ")
        imprime_operacion(dividendo, divisor, operacion="dividir")


imprime_division(dividendo=10, divisores=[2, 5, 3, 1])


# -----------------------------------------------------------------------------

# F: Funciones decoradoras


def decorador(funcion_decorada):

    @wraps(funcion_decorada)
    def envoltura(*args, **kwargs):

        print("Se llamó a la función decorada")
        if len(args) > 0:
            print("Con los argumentos:", args)
        if len(kwargs) > 0:
            print("Con los argumentos nombrados:", kwargs)

        result = funcion_decorada(*args, **kwargs)

        if result:
            print("La función retornó", result)

        return result

    return envoltura


@decorador
def funcion_normal(texto):
    print(texto, "Soy una función normal.")


@decorador
def suma(a, b):
    return a + b


funcion_normal("Hola")

suma(5, b=3)

# -----------------------------------------------------------------------------

# G: Funciones decoradoras con parámetros


def decorador_con_parametros(parametro1, parametro2):
    def decorador(funcion_decorada):
        @wraps(funcion_decorada)
        def envoltura(*args, **kwargs):
            print("Se llamó a la función decorada")
            print("Con los parámetros", parametro1, parametro2)
            if len(args) > 0:
                print("Con los argumentos:", args)
            if len(kwargs) > 0:
                print("Con los argumentos nombrados:", kwargs)
            result = funcion_decorada(*args, **kwargs)
            if result:
                print("La función retornó", result)
            return result

        return envoltura

    return decorador


@decorador_con_parametros("ARGUMENTO 1", "ARGUMENTO 2")
def funcion_decorada_con_parametros(*args, **kwargs):
    print("Soy una función decorada con parámetros.")
    return args, kwargs


final = funcion_decorada_con_parametros(1, 2, 3, 4, 5, a=1, b=2, c=3)


# -----------------------------------------------------------------------------

# H: Closures o Cierres


def multiplicador(x):

    def multiplicacion(y):
        return x * y

    return multiplicacion


cinco_por = multiplicador(5)

print("5 por 3 es", cinco_por(3))
print("5 por 4 es", cinco_por(4))
print("5 por 5 es", cinco_por(5))


# -----------------------------------------------------------------------------

# I: Funciones lambda

persona = {}

persona["nombre"] = "Faustino"
persona["edad"] = 10
persona["país"] = "Argentina"

persona["stats"] = lambda: print(
    f"{persona['nombre']} de {persona['país']} tiene {persona['edad']} años."
)
persona["hacer_magia"] = lambda: print("¡Jaque Mate!")


print(persona["stats"])
print(persona["hacer_magia"])
