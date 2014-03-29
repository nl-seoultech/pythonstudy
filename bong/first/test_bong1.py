def pay(hour):
	sigup = 5000
	all_sigup = 5000 * hour
   	return all_sigup - tax(all_sigup)


def tax(price):
    return price * 0.15


def test_tax():
   assert 15 == tax(100)
   assert 30 == tax(200)
   assert 45 == tax(300)


def test_pay():
    assert 4250 == pay(1)
    assert 8500 == pay(2)
