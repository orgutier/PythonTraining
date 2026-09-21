from challenges.challenge14.solution import (
    Drawable,
    Circle,
    Rectangle,
    CompositeShape,
    total_area,
    largest_by_area,
)


def test_circle_and_rectangle_never_inherit_from_drawable():
    assert Drawable not in Circle.__bases__
    assert Drawable not in Rectangle.__bases__
    assert Circle.__bases__ == (object,)


def test_circle_and_rectangle_satisfy_drawable_structurally():
    assert isinstance(Circle(1), Drawable)
    assert isinstance(Rectangle(1, 1), Drawable)


def test_composite_shape_delegates_via_composition():
    composite = CompositeShape([Circle(1), Rectangle(2, 3)])
    expected_area = Circle(1).area() + Rectangle(2, 3).area()
    assert round(composite.area(), 4) == round(expected_area, 4)
    assert CompositeShape.__bases__ == (object,)


def test_composite_shape_itself_is_drawable():
    composite = CompositeShape([Circle(1)])
    assert isinstance(composite, Drawable)


def test_total_area_skips_non_drawables():
    result = total_area([Circle(1), "not a shape", 42])
    assert round(result, 4) == round(Circle(1).area(), 4)


def test_total_area_empty_and_all_non_drawable():
    assert total_area([]) == 0.0
    assert total_area(["a", "b"]) == 0.0


def test_largest_by_area_works_uniformly():
    small = Circle(1)
    big = Rectangle(10, 10)
    composite = CompositeShape([small])
    assert largest_by_area([small, big, composite]) is big
