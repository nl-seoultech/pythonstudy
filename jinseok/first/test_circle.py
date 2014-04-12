def circle_nulbi(r):
    return round(3.14 * r * r, 2)


def test_circle_nulbi():
    assert 12.56 == circle_nulbi(2)
    assert 28.26 == circle_nulbi(3)
