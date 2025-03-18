import pytest

from object.divide import divide


def test_divide_positive():
    assert divide(10, 2) == 5
    assert divide(15, 3) == 5


def test_divide_negative():
    assert divide(-10, 2) == -5
    assert divide(-15, 3) == -5


def test_divide_by_one():
    assert divide(10, 1) == 10
    assert divide(-10, -1) == 10
    assert divide(0, 1) == 0
    assert divide(0, -1) == 0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Không thể chia cho 0."):
        divide(-5, 0)
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
