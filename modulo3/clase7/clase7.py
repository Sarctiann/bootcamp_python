"""
Este archivo contiene el código de ejemplo de la clase7.

"""

from dataclasses import dataclass

# Dunder methods


class NDPoint:
    """
    Punto en N dimensiones
    implementa las operaciones de suma y comparación
    """

    def __init__(self, *args):
        # `enumerate` nos permite obtener el índice y el valor de una lista
        for i, arg in enumerate(args):
            # `setattr` nos permite setear un atributo de la instancia dinámicamente
            # `chr(i + 97)` nos permite obtener la letra correspondiente al índice,
            # en este caso, a=97, b=98, c=99, ... ya que `i` comienza en 0.
            setattr(self, chr(i + 97), arg)

    def __str__(self):
        return f'({", ".join(f"{k}: {v}" for k, v in self.__dict__.items())})'

    def __repr__(self):
        # Originalmente sería algo así
        # return f"<{__name__}.Point object at {hex(id(self))}>"
        return "<{name}.Point({values}) object at {location}>".format(
            name=__name__,
            values=", ".join(f"{k}: {v}" for k, v in self.__dict__.items()),
            location=hex(id(self)),
        )

    def __add__(self, other):
        # Primero chequeamos que ambos puntos tienen las mismas dimensiones
        # `all` nos permite chequear si todos los elementos de un iterable "verifican como verdaderos"
        if not all(
            k in self.__dict__ and k in other.__dict__
            for k in frozenset((*self.__dict__.keys(), *other.__dict__.keys()))
        ):
            raise ValueError(f"Las dimensiones {self} y {other} no coinciden")

        return NDPoint(
            # `getattr` nos permite obtener un atributo de la instancia dinámicamente
            *(getattr(self, k) + getattr(other, k) for k in self.__dict__.keys())
        )

    def __eq__(self, other):
        return all(getattr(self, k) == getattr(other, k) for k in self.__dict__.keys())


p1 = NDPoint(1, 2)
p2 = NDPoint(3, 4)
print(p1)
print(p1 + p2)
print(p1 == p2)

# Herencia de clases


class Point2D(NDPoint):
    """
    Punto en 2 dimensiones
    """

    def __init__(self, x, y):
        # Declaramos los atributos para que sean reconocidos por las dev-tools
        self.a: int
        self.b: int
        # `super` nos permite acceder a los métodos de la clase padre
        # de esta foma útilizamos el constructor de la clase padre (NDPoint)
        super().__init__(x, y)
        # sabemos que la slace padre nos devolberá un punto
        # con los atributos a y b

    # No es necesario definir los métodos __str__, __repr__, __add__ y __eq__
    # pero supongamos que tenemos una implementación especial para __add__

    def __add__(self, other):
        print("Sumando punto de 2 dimensiones")
        return Point2D(self.a + other.b, self.a + other.b)


class Point3D(NDPoint):
    """
    Punto en 3 dimensiones
    """

    def __init__(self, x, y, z):
        super().__init__(x, y, z)


p3 = Point2D(1, 2)
p4 = Point2D(3, 4)
p5 = Point3D(1, 2, 3)

print(p3 == p4)
# print(p3 + p5) # esto nos arrojará un error

# Herencia Multiple


class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()


c = C()
# -> A

print(C.__mro__)
# -> (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# Poloimorfismo


def sumar_puntos(p_a: NDPoint, p_b: NDPoint) -> NDPoint:
    # Esta función espera recibir dos NDPoints y luego retorna la suma de ambos,
    # sabe que los puntos son sumables porque NDPoint implementa el método __add__
    return p_a + p_b


print(type(p1))  # -> <class '__main__.NDPoint'>
print(type(p4))  # -> <class '__main__.Point2D'>

print(sumar_puntos(p1, p4))

# Metaprogramación (ejemplo de Singleton con decoradores)


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class SingletonClass1:
    def __init__(self, value):
        self.value = value


obj1 = SingletonClass1(10)
obj2 = SingletonClass1(10000)

print(obj1.value)  # 10
print(obj2.value)  # 10

obj1.value = 30

print(obj1.value)  # 30
print(obj2.value)  # 30

print(obj1 is obj2)  # True

# Metaprogramación (ejemplo con metaclasses)


# Una metaclase es una clase de la que derivan las clases, es decir,
# una clase de la que se derivan las clases en lugar de los objetos.
class SingletonMeta(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class SingletonClass2(metaclass=SingletonMeta):

    def __init__(self, value):
        self.value = value


obj1 = SingletonClass2(10)
obj2 = SingletonClass2(10000)

print(obj1.value)  # 10
print(obj2.value)  # 10

obj1.value = 30

print(obj1.value)  # 30
print(obj2.value)  # 30

print(obj1 is obj2)  # True

# Metaprogramación (ejemplo de uso con dataclasses)


@dataclass
class Person:
    # Este attr especial nos permite definir los atributos de la clase,
    # de manera restrictiva
    __slots__ = ["name", "age"]

    name: str
    age: int

    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old"


p = Person("John", 30)
# p.legs = 2
print(p.greet())
