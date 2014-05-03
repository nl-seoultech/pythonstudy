# -*- coding: utf-8 -*-
from deco import my, other

def test_deco():
    m = my(22)  #{'age': 22, 'name': 'bong'}
    assert 'age' in m
    assert 'name' in m
    assert 22 == m['age']
    assert 'bong' == m['name']

    o = other(24)  #{'age': 22, 'name': 'bong'}
    assert 'o_age' in o
    assert 'nai' in o
    assert 24 ==  o['o_age']
    assert 'kang' == o['nai']
