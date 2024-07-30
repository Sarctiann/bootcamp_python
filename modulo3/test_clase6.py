"""
Consignas:

1. Crear una clase Persona que tenga los atributos first_name, last_name, y age.
    La clase debe tener una propiedad `full_name`.
    Y un metodo `greet` que imprima un saludo: 
        "Hola, mi nombre es {full_name} y tengo {age} años".

2. Cree una función que sume dos objetos de tipo `Point`, debe retornar un nuevo
    objeto Point, con la suma de las coordenadas x e y.
"""

from . import clase6 as mod


def test_person_class():
    try:
        Person = mod.Person  # type: ignore # noqa
    except ImportError:
        assert False, "No se pudo importar la clase `Person`"

    p = Person("Juan", "Perez", 30)
    assert p.full_name == "Juan Perez", "El valor de `full_name` es incorrecto"
    assert p.greet() == "Hola, mi nombre es Juan Perez y tengo 30 años"


def test_add_points():
    try:
        Point = mod.Point  # type: ignore # noqa
    except ImportError:
        assert False, "No se pudo importar la clase `Point`"
    try:
        add_points = mod.add_points  # type: ignore # noqa
    except ImportError:
        assert False, "No se pudo importar la función `add_points`"
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = add_points(p1, p2)
    assert p3.x == 4, "El valor de `x` es incorrecto"
    assert p3.y == 6, "El valor de `y` es incorrecto"
