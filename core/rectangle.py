from .base import Base


class Rectangle(Base):

    def __init__(self, name):
        super().__init__(name, 4)

    def perimeter(self, *args):
        if len(args) != 2:
            print("Не заданы значения сторон прямоугольника")
            return None
        self.perimeter_val = sum(args) * 2.0
        print(f"Периметр фигуры {self.name} равен: {self.perimeter_val}")
        return self.perimeter_val

    def area(self, *args):
        if len(args) != 2:
            print("Не заданы значения сторон прямоугольника")
            return None
        a, b = args
        self.area_val = a * b
        print(f"Площадь фигуры {self.name} равна: {self.area_val}")
        return self.area_val


if __name__ == '__main__':
    t1 = Rectangle("Прямоугольник1")
    print(type(t1))
    s1 = t1.area(1, 2)
    p1 = t1.perimeter(1, 2)

    t2 = Rectangle("Прямоугольник2")
    s2 = t2.area(2, 4)
    p2 = t2.perimeter(2, 4)

    a = t1.add_area(t2)
