def good_enough(origin, improved):
    return abs(origin - improved) < 0.0001

def average(x,y):
    return (x + y) / 2.0

def test_average():
    assert 1.5 == average(1,2)

def test_good_enough():
    assert good_enough(1, 1.0001)
