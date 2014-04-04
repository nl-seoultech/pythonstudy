def quadratic(a, b, c):
    r = pow(b, 2) - 4 * a * c
    ans = 0
    if r == 0:
        ans = 1
    elif r > 0:
        ans = 2
    return ans


def test_quadratic():
    assert 2 == quadratic(1, 4, 1)
    assert 1 == quadratic(2, 4, 2)
    assert 0 == quadratic(4, 4, 4)
