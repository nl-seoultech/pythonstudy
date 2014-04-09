def is_good_enough(guess, origin):
    return abs(origin - pow(guess, 2)) < 0.0001


def average(x, y):
    return (x + y) / 2.0


def improve(guess, origin):
    return average(guess , origin / float(guess))


def sqrt_iter(guess, origin):
    if is_good_enough(guess, origin):
        return guess
    else:
        guess = improve(guess, origin)
        return sqrt_iter(guess, origin)

def test_average():
    assert 1.5 == average(1, 2)
    assert 3.0 == average(2, 4)


def test_is_good_enough():
    assert not is_good_enough(1, 1.1)
    assert is_good_enough(1, 1.00001)


def test_improve():
    assert 1.4763157894736842 == improve(1.9, 2)
    assert 1.5 == improve(1, 2)
    

def test_sqrt_iter():
    assert 1.414 == round(sqrt_iter(1, 2), 3)
    assert 4 == round(sqrt_iter(3.5, 16),3)
