# -*- coding: utf-8 -*-
# Implement sqrt by Newton method.
# PyCharm


def good_enough(guess, origin):
    return abs(origin - pow(guess, 2)) <= 0.0001


def average(x, y):
    return (x + y) / 2.0


def improve(guess, origin):
    return average(guess, origin / float(guess))


def sqrt_(guess, origin):
    if good_enough(guess, origin):
        return guess
    else:
        print guess
        return sqrt_(improve(guess, origin), origin)


def test_average():
    assert 1.5 == average(1, 2)
    assert 2.5 == average(3, 2)


def test_improve():
    assert 1.5 == improve(1, 2)


def test_sqrt_():
    assert 1.414 == round(sqrt_(1, 2), 3)
    assert 1.732 == round(sqrt_(1, 3), 3)
