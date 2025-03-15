from object.sum_list import sum_list


# Kiểm thử
def test_empty_list():
    assert sum_list([]) == 0


def test_single_element_list():
    assert sum_list([1]) == 1


def test_multiple_elements_list():
    assert sum_list([1, 2, 3, 4, 5]) == 15


def test_negative_numbers_list():
    assert sum_list([-1, -2, -3, -4, -5]) == -15
