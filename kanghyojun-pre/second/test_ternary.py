def test_like_ternary():
    a = 4 if True else 5
    assert 4 == a
    a = 4 if False else 5
    assert 5 == a
    a = True and 4 or 5
    assert 4 == a
    a = False and 4 or 5
    assert 5 == a
