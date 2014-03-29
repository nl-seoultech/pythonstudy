# -*- coding: utf-8 -*-


def circle(radius):
    """원의 넓이를 구하는 함수"""
    return pow(radius, 2) * 3.14


def donut(in_circle, out_circle):
    return circle(out_circle) - circle(in_circle)


def test_circle2():
    assert 12.56 == circle(2)


def test_donut():
    assert 37.68  == donut(2, 4)
