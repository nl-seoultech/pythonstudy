
def interest(deposit):
    if 0 <= deposit <= 1000:
        return deposit * 0.04
    elif 1000 < deposit < 5000:
        return deposit * 0.045
    elif 5000 < deposit:
        return deposit * 0.05
    else:
        return False


def test_interest():
    assert 40 == interest(1000)
    assert False == interest(-10)
    assert 500 == interest(10000)
    assert 187.7265 == interest(4171.7)
    assert 459631588.5 == interest(9192631770)
