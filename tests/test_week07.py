import pytest
from exercises.week07.solution import Shape, Circle, Rectangle


def test_circle_area():
    assert abs(Circle(2).area() - 12.566) < 0.01


def test_rectangle_area():
    assert Rectangle(3, 4).area() == 12


def test_shape_is_abstract():
    with pytest.raises(TypeError):
        Shape()
