# -*- coding: utf-8 -*-

def test_str1():
    a="def"
    assert 'def' == a
    b =  'def'
    assert 'def' == b
    c = "d\"ef"
    assert 'd"ef' == c

def test_uni1():
    a = '박경선'
    assert '박경선' == a

def test_str_join():
    a=['a','b','d','c']
    b= '+'.join(a)
    assert 'a+b+d+c' == b

def test_str_rep():
    a = 'hello world'
    assert 'bye world' ==  a.replace('hello' , 'bye')

def  test_start_or_end_width():
    assert 'hello world'.startswith('hello')
    assert 'hello world'.endswith('world')


