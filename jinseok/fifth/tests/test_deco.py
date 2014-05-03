from deco import my, other


def test_deco():
    m = my(27) # {'age' : 27, 'name':'parkjinseok'}
    assert 'age' in m
    assert 'name' in m
    o = other(24) #{'nai':24,'name' : 'bongyong'}
    assert 'nai' in o
    assert 'name' in o
    assert 24 == o['nai']
    assert 'bongyong' == o['name']
    
