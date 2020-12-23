from Homework4.core.base import Base
import pytest
from Homework4.core.circle import Circle
from Homework4.core.square import Square
from Homework4.core.triangle import Triangle
from Homework4.core.rectangle import Rectangle


def test_is_instance(figure):
    obj = figure("Name")
    assert isinstance(obj, Base)
    print(f"Объект {obj} является экземпляром классса {Base}")


def test_has_attribute(figure, self_attribute):
    obj = figure("Name")
    assert hasattr(obj, self_attribute)
    print(f"Объект {obj} содержит атрибут \"{self_attribute}\"")


def test_has_calc_attribute(figure, self_calc_attribute):
    obj = figure("Name")
    assert hasattr(obj, self_calc_attribute)
    print(f"Объект {obj} содержит вычисляемый атрибут \"{self_calc_attribute}\"")


def test_has_method(figure, self_method):
    obj = figure("Name")
    assert hasattr(obj, self_method)
    print(f"Объект {obj} содержит метод \"{self_method}\"")


@pytest.mark.parametrize("figure1, name1, fig1_par1, fig1_par2, figure2, name2, fig2_par1, fig2_par2",
                         [
                             (Circle, "Кргу_1", (5,), (5,), Circle, "Кргу_2", (3,), (3,)),
                             (Square, "Квадрат_1", (4,), (4,), Square, "Квадрат_2", (3,), (3,)),
                             (Rectangle, "Прямоугольник_1", (4, 5), (4, 5), Rectangle, "Прямоугольник_2", (3, 2),
                              (3, 2)),
                             (
                             Triangle, "Треугольник_1", (4, 2), (4, 5, 6), Triangle, "Треугольник_2", (3, 2), (3, 2, 1))
                         ])
def test_for_figures(figure1, name1, fig1_par1, fig1_par2, figure2, name2, fig2_par1, fig2_par2):
    f1 = figure1(name1)
    s1 = f1.area(*fig1_par1)
    p1 = f1.perimeter(*fig1_par2)
    f2 = figure2(name2)
    s2 = f2.area(*fig2_par1)
    p2 = f2.perimeter(*fig2_par2)
    s = f1.add_area(f2)
    assert s1 > s2
    assert p1 > p2
    assert s == s1 + s2
    assert f1.area_val is not None
    assert f1.perimeter_val is not None
    name = figure1.__name__
    if name == "Circle":
        assert f1.angles is None and f2.angles is None
    elif name == "Square" or name == "Rectangle":
        assert f1.angles == f2.angles == 4
    elif name == "Triangle":
        assert f1.angles == f2.angles == 3
    else:
        assert False, f"Неизвестный класс! {name}"
