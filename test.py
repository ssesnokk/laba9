import pytest
from calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize("a,b,expected", [
    (4, 6, 10),
    (-3, 8, 5),
    (7, 0, 7),
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (20, 4, 5),
    (15, 5, 3),
])
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(25, 0)

@pytest.mark.parametrize("n,expected", [
    (5, True),
    (11, True),
    (9, False),
    (19, True),
    (0, False),
    (1, False),
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected
