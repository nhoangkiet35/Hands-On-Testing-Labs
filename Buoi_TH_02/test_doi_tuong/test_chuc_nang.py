import pytest
from doi_tuong.chuc_nang import gcd, simplify, input_fraction

def test_gcd():
    assert gcd(8, 12) == 4
    assert gcd(100, 10) == 10
    assert gcd(17, 5) == 1
    assert gcd(-8, 12) == 4
    assert gcd(0, 5) == 5

def test_simplify():
    assert simplify(4, 8) == (1, 2)
    assert simplify(10, 100) == (1, 10)
    assert simplify(25, 5) == (5, 1)
    assert simplify(9, 3) == (3, 1)

def test_input_fraction():
    assert input_fraction(3, 4) == (3, 4)
    assert input_fraction(2, 4) == (1, 2)
    
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        input_fraction(1, 0)
    
    with pytest.raises(TypeError, match=".*must be integers.*"):
        input_fraction(1.5, 2)
