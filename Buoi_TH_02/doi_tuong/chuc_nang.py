def gcd(a: int, b: int) -> int:
    """Tìm ước chung lớn nhất của hai số."""
    while b:
        a, b = b, a % b
    return abs(a)

def simplify(numerator: int, denominator: int) -> tuple:
    """Tối giản phân số."""
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def input_fraction(numerator: int, denominator: int) -> tuple:
    """Nhập phân số và kiểm tra tính hợp lệ."""
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return simplify(numerator, denominator)
