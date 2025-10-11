import pytest
from calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize("a, b, expected",
[
    (2, 3, 5),
    (-1, 5, 4),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected",
[
    (10, 2, 5),
    (9, 3, 3),
])
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected

@pytest.mark.parametrize("a", [1, 14,])
def test_divide_by_zero(a):
    with pytest.raises(ZeroDivisionError):
        calc.divide(a, 0)


@pytest.mark.parametrize("n, expected",
[
    (2, True),
    (4, False),
    (10, False),
    (7, True),
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected
