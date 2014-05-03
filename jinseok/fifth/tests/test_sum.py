from deco.func import my_sum

def test_my_sum():
    assert 55 == my_sum(1,2,3,4,5,6,7,8,9,10)
    assert 45 == my_sum(1,2,3,4,5,6,7,8,9)

def test_my_cal():
    args = [1,2,3]
    kwargs = {cal == '+'}
    assert 6 == my_cal(*arg, **kwargs)
    
