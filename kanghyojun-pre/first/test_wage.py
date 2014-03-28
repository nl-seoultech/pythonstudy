# -*- coding: utf-8 -*-

def wage(money):
    return money - (0.15 * money)


def daily_wage(hour):
    return wage(5000) * hour


def test_wage():
    assert 4250 == wage(5000)


def test_daily_wage():
    assert 8500 == daily_wage(2)
