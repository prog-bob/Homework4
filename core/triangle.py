from .base import Base


class Triangle(Base):

    def __init__(self, name):
        super().__init__(name, 3)

    def perimeter(self, *args):
        if len(args) != 3:
            print("Не задано значение сторон треугольника")
            return None
        self.perimeter_val = sum(args)
        print(f"Периметр фигуры {self.name} равен: {self.perimeter_val}")
        return self.perimeter_val

    def area(self, *args):
        if len(args) != 2:
            print("Не заданы значение основания и высоты треугольника")
            return None
        basis, height = args
        self.area_val = basis * height / 2.0
        print(f"Площадь фигуры {self.name} равна: {self.area_val}")
        return self.area_val


if __name__ == '__main__':
    t1 = Triangle("Треугольник1")
    print(type(t1))
    s1 = t1.area(1, 2)
    p1 = t1.perimeter(1, 2, 3)

    t2 = Triangle("Треугольник2")
    s2 = t2.area(2, 4)
    p2 = t2.perimeter(2, 3, 5)

    a = t1.add_area(1)
