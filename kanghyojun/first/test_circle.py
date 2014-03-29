def circle(radius):
    pi = 3.14
    return pow(radius, 2) * pi


def test_circle2():
    assert 12.56 == circle(2)
