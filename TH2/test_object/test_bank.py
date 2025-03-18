from object.bank import value


def test_hello():
    assert value("Hello, World!") == 0
    assert value("Hello, 10!") == 0


def test_h_but_not_hello():
    assert value("Hey, World!") == 20
    assert value("Hey, 10!") == 20


def test_other_value():
    assert value("1234567890") == 100
    assert value("What's up!") == 100


def test_empty_string():
    assert value("") == 100
    assert value("   ") == 100
