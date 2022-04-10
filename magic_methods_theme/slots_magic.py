# Slots ускоряет работу.
# С 3.10 в dataclasses появились slots - это ускоряет создание на 20% и работу с локальными свойствами.
# Также уменьшается использование памяти.
# Но при этом ломается множественное наследование
# При использовании slots не создается __dict__ для хранения аргументов класса.

# Источники
# https://docs.python.org/3/reference/datamodel.html#object.__slots__
# https://www.youtube.com/watch?v=P0uvWDpqB8I

import math


class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = math.sqrt(x * x + y * y)

    @property
    def length(self):
        return self.__length

    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y})'

    def __str__(self):
        return f'Point2D({self.x},{self.y}) length {self.length}'


class Point3D(Point2D):
    __slots__ = 'z'

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z




p = Point2D(2, 3)
print(p)
