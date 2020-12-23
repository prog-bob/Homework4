from abc import ABC, abstractmethod


class Base(ABC):

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles
        self.area_val = None
        self.perimeter_val = None

    """
    вычисление площади фигуры
    """
    @abstractmethod
    def area(self, *args):
        pass

    """
    вычисление периметра фигуры
    """
    @abstractmethod
    def perimeter(self, *args):
        pass

    """
    вычисление суммы площадей данной фигуры и другой фигуры
    """
    def add_area(self, other):
        if not isinstance(other, Base):
            print(f"Передан неправильный класс {type(other)}. Класс должен быть подклассом Base")
            return None
        if not other.area_val:
            print(f"Не имеется значения для площади фигуры {other.name}.")
            return None
        if not self.area_val:
            print(f"Не имеется значения для площади фигуры {self.name}.")
            return None

        sum_areas = self.area_val + other.area_val
        print(f"Сумма площадей фигур {other.name} и {self.name} равна: {sum_areas}")
        return sum_areas
