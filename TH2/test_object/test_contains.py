from object.contains import contains


def test_value_in_list():
    assert contains([1, 2, 3, 4, 5], 3) == True


def test_value_not_in_list():
    assert contains([1, 2, 3, 4, 5], 6) == False


def test_empty_list():
    assert contains([], 5) == False
