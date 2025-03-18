from object.is_prime import is_prime


def test_prime_number():
    assert is_prime(7) == True


def test_non_prime_number():
    assert is_prime(8) == False


def test_number_less_than_2():
    assert is_prime(1) == False
