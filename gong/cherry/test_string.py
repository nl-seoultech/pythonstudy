# -*- coding: utf-8 -*-

def test_str1():
    a = 'def'
    assert 'def' == a
    b = "def"
    assert 'def' == b
    c = "d\"ef"
    # d\"ef
    assert 'd"ef' == c


def test_uni1():
    a = None  # initialize
    assert u"12345" == "12345"
    a = "123"
    assert "123" == a.encode('utf-8')


def test_str_join():
    a = ['a', 'b', 'c', 'd']
    b = '\t'.join(a)
    assert b == 'a	b	c	d'
    assert a == b.split('\t')



def test_str_replace():
    a = 'hello world' 
    assert 'bye world' == a.replace('hello', 'bye')



def test_start_or_end_with():
    assert 'hello world'.startswith('hello')
    assert 'hello world'.endswith('world')
