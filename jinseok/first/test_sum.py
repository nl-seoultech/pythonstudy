def sum_(a, b):
    return a + b


def test_sum1():
    assert 2 == sum_(1, 1)
    assert 4 == sum_(1, 3)
    assert 4 == sum_(2, 2)
    assert 6 == sum_(5, 1)
    assert 7 == sum_(5, 2)
