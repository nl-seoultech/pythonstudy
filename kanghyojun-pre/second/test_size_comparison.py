# -*- coding: utf-8 -*-
def in_0_5(n):
    """ [0, 5] 안에 범위에있는지 측정.
    """
    return n >= 0 and n <= 5


def in_0_5_(n):
    """ [0, 5] 안에 범위에있는지 측정. in_0_5 랑 다른방법으로 측정.
    """
    return 0 <= n <= 5


def in_0_not_5(n):
    """ [0, 5) 안에 범위에있는지 측정.
    """
    return 0 <= n < 5


def in_not_0_not_5(n):
    """ (0, 5) 안에 범위에있는지 측정.
    """
    return 0 < n < 5


def test_comp():
    assert in_0_5(1)
    assert in_0_5(2)
    assert in_0_5(5)
    assert in_0_5(0)
    assert not in_0_5(-1)
    assert not in_0_5(-6)


def test_2comp():
    assert in_0_5_(1)
    assert in_0_5_(2)
    assert in_0_5_(5)
    assert in_0_5_(0)
    assert not in_0_5_(-1)
    assert not in_0_5_(-6)


def test_in_0_not_5():
    assert in_0_not_5(1)
    assert in_0_not_5(0)
    assert not in_0_not_5(5)
    assert not in_0_not_5(-1)
    assert not in_0_not_5(-6)


def test_in_not_0_not_5():
    assert in_not_0_not_5(1)
    assert not in_not_0_not_5(0)
    assert not in_not_0_not_5(5)
    assert not in_not_0_not_5(-1)
    assert not in_not_0_not_5(-6)
