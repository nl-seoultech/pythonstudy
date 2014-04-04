# -*- coding: utf-8 -*-

def my_interest(money):
    """이자 계산 프로그램.

      - $1000 이하이면 4%의 이자
      - $5000 달러 미만이면 4.5%의 이자
      - $5000 이상이면 5%의 이자
    """
    if money <= 1000:
        return 0.4
    elif money < 5000:
        return 0.45
    else:
        return 0.5


def my_interest2(money):
    """이자 계산 프로그램. 리턴을 한개만둬봅시다.
    """
    r = 0.5
    if money <= 1000:
        r = 0.4
    elif money < 5000:
        r = 0.45
    return r


def test_bank_interest():
    assert 0.4 == my_interest(1000)
    assert 0.45 == my_interest(1001)
    assert 0.5 == my_interest(5000)


def test_bank_interest2():
    assert 0.4 == my_interest2(1000)
    assert 0.45 == my_interest2(1001)
    assert 0.5 == my_interest2(5000)
