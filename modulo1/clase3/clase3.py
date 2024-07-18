from typing import Any


def ejercicios_de_la_clase_3() -> Any:
    """
    Esta función generadora funciona de la misma manera que la que resolvierion
    en la clase 2.

    Por cualquier duda revise su documentación.

    En esta oportunidad vamos a tener que reemplazar el "cuerpo de las funciones"
    que inicialmente solo contendrán un return. Para cumplir con las
    consignas.

    Tenga en cuenta que en contraste con los ejercicios de la clase anterior,
    en vez de usar "variables", deberá trabajar con los parametros de las funciones.

    Luego cuando corra los tests. estan funciones serán probadas con diferentes
    valores para verificar que funcionan correctamente.
    """

    # Ejercicio 1: Modifique esta función para que devuelva el texto "menor a 10"
    # si `valor` es menor a 10, y "mayor o igual a 10" en caso contrario.
    # Debe usar un `if` para resolverlo, sin usar `else`.
    def a(valor: int) -> str:
        return ""

    yield a

    # Ejercicio 2: Modifique esta función para que devuelva el valor más grande
    # entre `valor1` y `valor2`. Si los valores son iguales, debe devolver 0.
    # Debe usar al menos un `if` y un `else` para resolverlo.
    def b(valor1: int, valor2: int) -> int:
        return 0

    yield b

    """
        NOTA: Si pudo resolver el primer ejercicio cumpliendo con la consigna, 
        habrá para el segundo ejercicio no es necesario útilizar `else`.

        Esto en realidad casi siempre es asi en el contexto de una función que 
        retorna un valor, ya que la ejecución de la función termina con `return`.
        Por lo cual es considerado una "buena práctica" simplificar los condicionales
        siempre que sea posible.

        Si aún no resolvió el primer ejercicio, esta nota le puede resultar de ayuda.

        De todas formas, estamos usando estructuras condicionales inecesariamente
        más complejas, para ponerlas en práctica.
    """

    # Ejercicio 3: Modifique esta función para que devuelva 0 si `valor` es menor
    # a 10, 1 si `valor` es igual a 10 y 2 si `valor` es mayor a 10. Debe usar
    # un `if`, un `elif` y un `else` para resolverlo.
    def c(valor: int) -> int:
        return 0

    yield c

    # Ejercicio 4: Modifique esta función para que devuelva la sumatoria
    # números enteros menores a `valor`. Debe usar un `for` con un range para
    # resolverlo.
    def d(valor: int) -> int:
        return 0

    yield d

    # Ejercicio 5: Modifique esta función para que devuelva la sumatoria
    # números enteros menores a `valor`, pero si `solo_impares` es `True` solo
    # sume los números impares. Debe usar un `while` y un `if`combinado con la
    # palabra clave `continue` para resolverlo. (CUIDADO CON LOS BUCLES INFINITOS).
    def e(valor: int, solo_impares: bool) -> int:
        return 0

    yield e

    # Ejercicio 6: Modifique esta función para que devuelva el texto correspondiente
    # al número en español. Por ejemplo, si `valor` es 1, debe devolver "uno". Si
    # `valor` no está en el rango de 1 a 5, debe devolver "no encontrado". Debe usar
    # un diccionario para resolverlo.
    def f(valor: int) -> str:
        return ""

    yield f

    # Ejercicio 7: Modifique esta función para que devuelva el texto correspondiente
    # al número en español, pero solo si `valor` está en el rango de 1 a 5. Si no
    # lo está, debe devolver "valor no soportado". Debe usar `match` en combinación
    # con la función `f` (del ejercicio anterior) para resolverlo.
    def g(valor: int) -> str:
        return ""

    yield g
