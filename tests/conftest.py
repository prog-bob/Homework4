import pytest
from Homework4.core.circle import Circle
from Homework4.core.square import Square
from Homework4.core.triangle import Triangle
from Homework4.core.rectangle import Rectangle


@pytest.fixture(scope="module", params=[Circle, Square, Triangle, Rectangle])
def figure(request):
    return request.param


@pytest.fixture(scope="module", params=['name', 'angles'])
def self_attribute(request):
    return request.param


@pytest.fixture(scope="module", params=['area_val', 'perimeter_val'])
def self_calc_attribute(request):
    return request.param


@pytest.fixture(scope="module", params=['area', 'perimeter', 'add_area'])
def self_method(request):
    return request.param
