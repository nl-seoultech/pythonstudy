# -*- coding: utf-8 -*-

def circle(r):
    return 3.14 * pow(r, 2)


def test_circle():
    assert 3.14 == circle(1)
    assert 12.56 == circle(2)
    assert 50.24 == circle(4)
