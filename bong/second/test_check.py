# -*- coding: utf-8 -*-
def same_0_5(x):
    """ 0이상 5이하
    """
    return 0 <= x and x <= 5


def test_same_0_5():
    assert not same_0_5(-5)
    assert same_0_5(0)
    assert same_0_5(3)
    assert same_0_5(5)
    assert not same_0_5(7)
    
