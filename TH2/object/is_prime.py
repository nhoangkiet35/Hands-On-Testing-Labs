def is_prime(n: int) -> bool:
    """Kiểm tra xem số n có phải là số nguyên tố không."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
