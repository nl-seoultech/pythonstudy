# -*- incoding: utf-8 -*-

from deco import my, other

def test_deco():
	m = my(22) # {'age':22, 'name': 'gong'}
	assert 'age' in m
	assert 'name' in m
	assert 22 == m['age']
	assert 'gong' == m['name']
	o = other(24)
	assert my(24)
	assert 'age' in o
	assert 'name' in o
