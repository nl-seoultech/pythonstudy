# price() = ticket price
# discount() = the number of times to discount
# p = ticket price

def profit(p):
    print spectator(p)
    print p
    print cost(p)
    return spectator(p) * p - cost(p)

def spectator(p):
    return round(5.0 - p, 2) * 10 * 15 + 120

def cost(p):
    return 180 + spectator(p) * 0.04
    


def test_profit():
    assert 415.2 == profit(5)
    assert 476.1 == profit(4.9)

def test_spectator():
    assert 135 == spectator(4.9)
    assert 270 == spectator(4)

def test_cost():
    assert 190.8 == cost(4)
    assert 185.4 == cost(4.9)
