def equation1(x):
    return (pow(x, 2) - 2 * x + 1) == 0


def equation2(x):
    return (pow(x, 2) - pow(3, 2)) == 0


def test_equation1():
    assert equation1(1)
    assert not equation1(-1)


def test_equation2():
    assert equation2(3)
    assert not equation2(4)
