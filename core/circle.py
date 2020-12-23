from .base import Base
from math import pi


class Circle(Base):

    def __init__(self, name):
        super().__init__(name, None)

    def perimeter(self, *args):
        if len(args) != 1:
            print("Не задано значение радиуса окружности")
            return None
        self.perimeter_val = 2.0 * pi * args[0]
        print(f"Длина окружности {self.name} равна: {self.perimeter_val}")
        return self.perimeter_val

    def area(self, *args):
        if len(args) != 1:
            print("Не задано значение радиуса окружности")
            return None
        self.area_val = pi * args[0] ** 2
        print(f"Площадь фигуры {self.name} равна: {self.area_val}")
        return self.area_val
