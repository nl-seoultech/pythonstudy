def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def test_add():
    assert 6 == add(2,4)


def test_sub():
    assert 4 == sub(6, 2)
