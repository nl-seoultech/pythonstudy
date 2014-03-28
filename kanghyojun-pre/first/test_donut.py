# -*- coding: utf-8 -*-

def circle(r):
    return 3.14 * pow(r, 2)


def donut(inner, outer):
    return circle(outer) - circle(inner)


def test_donut():
    assert 37.68 == donut(2, 4)
