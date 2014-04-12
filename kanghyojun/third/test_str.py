# -*- coding: utf-8 -*-

def test_str1():
    a = 'def'
    assert 'def' == a
    b = "def"
    assert 'def' == b
    c = "d\"ef"
    #  d\"ef
    assert 'd"ef' == c


def test_uni1():
    a = u"강효준"
    assert "강효준" == a.encode('utf-8')


def test_str_join():
    a = ['a', 'b', 'c', 'd']
    b = '+'.join(a)
    assert 'a+b+c+d' == b
    assert a == b.split('+')


def test_str_replace():
    a = 'hello world'
    c = a.replace('hello', 'bye')
    assert 'bye world' == c


def test_start_or_end_with():
    assert 'hello world'.startswith('h')
    assert 'hello world'.endswith('d')
