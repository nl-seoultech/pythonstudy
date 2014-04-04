def people_per_price(price):
    people = round(5 - price, 2) * (15 / 0.1) + 120
    return people


def owner_loss(price):
    loss = 180 + people_per_price(price) * 0.04
    return loss


def owner_profit(price):
    return (people_per_price(price) * price) - owner_loss(price) 


def test_people_per_price():
    assert 126.0 == people_per_price(1)


def test_owner_loss():
    assert 190.8 == owner_loss(4)


def test_owner_profit():
    assert 415.2 == owner_profit(5)
    assert 476.1 == owner_profit(4.9)

def test_result():
    l = [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9]
    max_profit = max([owner_profit(x) for x in l])
    for x in l:
	if owner_profit(x) == max_profit:
		print x
    assert False
