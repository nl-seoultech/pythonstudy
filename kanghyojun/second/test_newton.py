# -*- coding: utf-8 -*-
# Implement sqrt by Newton method.
# PyCharm


def good_enough(origin, guess):
    return abs(origin - guess) < 0.0001


def average(x, y):
    return (x + y) / 2.0


def test_average():
    assert 1.5 == average(1, 2)
    assert 2.5 == average(3, 2)


def test_good_enough():
    assert not good_enough(1, 1.1)
    assert good_enough(1, 1.00001)
    assert not good_enough(1, 1.0099)
