def under_1000(account):
    return account*0.040


def test_under_1000():
    assert 40 == under_1000(1000)
    assert 60 == under_1000(1500)
    assert 80 == under_1000(2000)


def under_5000(account):
    return account*0.045


def test_under_5000():
    assert 45 == under_5000(1000)
    assert 67.5 == under_5000(1500)
    assert 78.75 == under_5000(1750)


def over_5000(account):
    return account*0.05


def test_over_5000():
    assert 50 == over_5000(1000)
    assert 477 == over_5000(9540)
    assert 1367 == over_5000(27340)


def interest(account):
     if account<=1000:
	return under_1000(account)
     elif 1000 <= account < 5000:
	return under_5000(account)
     else:
	return over_5000(account)


def test_interest():
    assert 1367 == interest(27340)
    assert 67.5 == interest(1500)
    assert 39.2 == interest(980)
