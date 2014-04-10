
def interest(deposit):
    if 0 <= deposit <= 1000:
        return deposit * 0.04
    elif 1000 < deposit < 5000:
        return deposit * 0.045
    elif 5000 < deposit:
        return deposit * 0.05


def test_interest():
    assert 40 == interest(1000)
