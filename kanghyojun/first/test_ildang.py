def ildang(hour):
    sigup = 5000
    all_sigup = hour * sigup
    return all_sigup - tax(all_sigup)


def tax(price):
    return price * 0.15


def test_wage():
    assert 4250 == ildang(1)
    assert 8500 == ildang(2)


def test_tax():
    assert 15 == tax(100)
    assert 30 == tax(200)
    assert 45 == tax(300)
