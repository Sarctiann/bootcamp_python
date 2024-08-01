"""
Este archivo contiene el código de ejemplo de la clase6.

Al final del mismo contiene unas consignas para resolver,
luego ejecute los test, para verificar las soluciones.
"""

# Clase vacía


class Empty:
    """
    Clase vacía.

    Esta clase no tiene atributos ni métodos (por el momento).
    Por ahora podemos considerarla como un placeholder.
    """

    pass


# Clase simple


class SimplePoint:
    """
    Esta clase representa un punto en el plano cartesiano. Se comporta como una
    simple structura de datos, con dos atributos x e y.
    """

    x = 0
    "Atributo de clase `x`"
    y = 0
    "Atributo de clase `y`"


p1 = SimplePoint()

print(p1)  # -> <__main__.SimplePoint object at 0xAlgunaPosiciónDeMemoria>
print(type(p1))  # -> <class '__main__.SimplePoint'>

# Notación de punto


class SimplePointYet:
    """
    Agregamos un método a la clase `SimplePoint`.
    """

    x = 0
    "Atributo de clase `x`"
    y = 0
    "Atributo de clase `y`"

    @classmethod
    def change(cls, new_x, new_y):
        """
        Este método cambia los valores de los atributos `x` e `y`.
        """
        cls.x = new_x
        cls.y = new_y


p2 = SimplePointYet()

print(p2.y)  # -> 0

p2.change(1, 2)

print(p2.y)  # -> 2

# Atributos de clace vs atributos de instancia

p3 = SimplePointYet()
p3.change(1, 2)

p4 = SimplePointYet()
p4.change(3, 4)

print(p4.x)  # -> 3
print(p3.x)  # -> ?


class BasicPoint:
    """
    Clase que representa un punto en el plano cartesiano.
    """

    def __init__(self, x, y):
        """
        Constructor de la clase.
        Este es un método especial (también llamado "dunder method" o "magic method").
        Y nos sirve para inicializar los atributos de la INSTANCIA.
        Luego vamos a tratar este tema con más detalles
        """
        self.x = x
        "Atributo de instancia `x`"
        self.y = y
        "Atributo de instancia `y`"

    def change(self, new_x, new_y):
        """
        Este método cambia los valores de los atributos `x` e `y`.
        """
        self.x = new_x
        self.y = new_y


p5 = BasicPoint(1, 2)
p6 = BasicPoint(0, 0)

p6.change(3, 4)

print(p6.x)  # -> 3
print(p5.x)  # -> 1

# Modificadores de acceso


class Point:
    def __init__(self, x, y):
        """
        Constructor de la clase.
        """
        # Notar que los atributos ahora empiezan con un guión bajo.
        # Esto es una convención para indicar que son "PROTEGIDOS".
        self._x = x
        self._y = y

    def __log(self):
        """
        Esto funcionaría como un método PRIVADO.
        (el nombre empieza con dos guiones bajos)
        """
        print(f"({self._x}, {self._y})")

    def change(self, new_x, new_y):

        self._x = new_x
        self._y = new_y
        self.__log()

    @property
    def x(self):
        """
        Gracias al decorador @property podemos acceder a `x`
        como si fuera un atributo.
        Pero como es una función podemos retornar un "valor computado"
        También podemos referirnos a este tipo de funciones como "propiedades"
        """
        # Getter para el atributo `x`. (Para obtener `x`)
        # (podemos incluir mas lógica dentro de la función)
        return self._x

    @x.setter
    def x(self, value):
        # Setter para el atributo `x`. (Para modificar `x`)
        # (podemos incluir mas lógica dentro de la función)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, _):
        # Podemos decidir por ejemplo que el aributo x sea inmutable
        raise AttributeError("El atributo `y` es inmutable")


p7 = Point(1, 2)
# p7.__log()  #       Esto arroja un AttributeError, ya que "__log" es privado.
p7.x = 2  #          Podemos hacer esta asignación gracias a @x.setter
# p7.y = 4  #         Esto arroja un AttributeError, ya que "y" es inmutable.
print(p7.x)  # -> 1 Podemos obtener el valor de x gracias a @property

# Atributos de Módulo

__all__ = ["print_module_attrs"]


def print_module_attrs():
    """
    Esta función imprime los atributos del módulo.
    """
    print(dir())


if __name__ == "__main__":
    print_module_attrs()

"""
Consignas:

1. Crear una clase Persona que tenga los atributos first_name, last_name, y age.
    - La clase debe tener un constructor que reciba estos tres atributos en ese orden.
    - La clase debe tener una propiedad `full_name`.
    - La case debe tener un metodo `greet` que imprima un saludo: 
        "Hola, mi nombre es {full_name} y tengo {age} años".

2. Cree una función con el nombre `add_points` que sume dos objetos de tipo `Point`,
    debe retornar un nuevo objeto Point, con la suma de las coordenadas x e y.
"""
