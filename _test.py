import pytest

def square(x):
    return x * x

def cube(x):
    return x * x * x

def check_square(x):
    assert square(x) == x * x, f"Square of {x} should be {x * x}"

def check_cube(x):
    assert cube(x) == x * x * x, f"Cube of {x} should be {x * x * x}"

def test_invlid_input():
    with pytest.raises(TypeError):
        square("a")
    with pytest.raises(TypeError):
        cube("b")