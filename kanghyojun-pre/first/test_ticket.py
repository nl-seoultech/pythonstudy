# -*- coding: utf-8 -*-

def attendee(price):
    r = 120 + (15 / 0.1) * round(5 - price, 2)
    return r


def cost(price):
    return 180 + 0.04 * attendee(price)


def profit(price):
    return price * attendee(price) - cost(price)


def test_attendee():
    assert 120 == attendee(5)
    assert 270 == attendee(4)
    assert 135 == attendee(4.9)


def test_cost():
    assert 185.4 == cost(4.9)


def test_profit():
    assert 476.1 == profit(4.9)
