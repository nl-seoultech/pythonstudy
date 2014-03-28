# -*- coding: utf-8 -*-

def dollor_to_won(dollor):
    return dollor * 1071


def won_to_dollor(won):
    return won / dollor_to_won(1)


def test_exchange():
    assert 1071 == dollor_to_won(1)
    assert 1 == won_to_dollor(1071)
    assert 1 == won_to_dollor(dollor_to_won(1))
