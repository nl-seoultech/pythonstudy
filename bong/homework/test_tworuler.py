# -*- coding: utf-8 -*-
def how_interest(interest):
    """ 이자를 구하는 함수
    """
    if interest <= 1000:
        return 4
    elif interest < 5000:
        return 4.5
    else:
        return 5


def test_interest():
    assert 4 == how_interest(500)
    assert 4 == how_interest(1000)
    assert 4.5 == how_interest(2300)
    assert 5 == how_interest(5000)
    assert 5 == how_interest(6320)
