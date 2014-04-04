def test_attending():
    assert 120==attending(5)
    assert  135==attending(4.9)

def attending(price):
    return 120 + (15*(round((5-price),2)*10))


def test_cost():
    assert 184.8 == cost(5)
    assert 185.4 == cost(4.9)
def cost(price):
    return 180+attending(price)*0.04

def test_profit():
    assert 415.2 ==profit(5)
    assert 489.6 ==profit(4.9)

def profit(price):
    return attending(price)*5 - cost(price)

def test_result():
    l = [4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9] 
    max_profit = max([profit(x) for (x) in l ])
    for x in l:
        if profit(x) == max_profit:
            print x
    
    assert False
