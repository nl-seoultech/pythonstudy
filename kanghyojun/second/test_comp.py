# -*- coding: utf-8 -*-
def in_0_5(x):
    """ 0이상 5이하
    """
    return 0 <= x <= 5


def test_in_0_5():
    assert in_0_5(0)
    assert in_0_5(5)
    assert in_0_5(1)
    assert not in_0_5(6)
    assert not in_0_5(-1)
