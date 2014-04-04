def test_is_none():
    a = None
    assert a is None
    assert not a


def test_is_none():
    a = 1
    b = 1
    assert not a is b
    assert not (a is not b)
    a = b
    assert a is b
    assert not (a is not b)
