# -*- coding: utf-8 -*-


def circle(radius):
    """ 원의 넓이를 구하는 프로그램

      .. sourcecode::python

         >> circle(1)
         3.14
    """
    pi = 3.14
    return pow(radius, 2) * pi


def test_circle2():
    assert 12.56 == circle(2)
