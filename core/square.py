from .base import Base


class Square(Base):

    def __init__(self, name):
        super().__init__(name, 4)

    def perimeter(self, *args):
        if len(args) != 1:
            print("Не задано значение стороны квадрата")
            return None
        self.perimeter_val = args[0] * 4.0
        print(f"Периметр фигуры {self.name} равен: {self.perimeter_val}")
        return self.perimeter_val

    def area(self, *args):
        if len(args) != 1:
            print("Не задано значение стороны квадрата")
            return None
        self.area_val = args[0] ** 2
        print(f"Площадь фигуры {self.name} равна: {self.area_val}")
        return self.area_val


