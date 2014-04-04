# -*- coding: utf-8 -*-

def good_enough(guess, x):
    return abs(x - pow(guess, 2)) < 0.0001


def average(x, y):
    return (x + y) / 2.0


def improve(guess, x):
    return average(guess, x / guess)


def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)


def test_sqrt_iter():
    assert 1.414 == round(sqrt_iter(1, 2), 3) 
