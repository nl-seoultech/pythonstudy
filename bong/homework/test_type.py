#-*- coding: utf-8 -*-
def what_type(x):
    """타입을 확인하는 함수
    
    """
    data_type = 'null'
    if(isinstance(x, int)):
        data_type = 'int'
    elif(isinstance(x, float)):
        data_type = 'float'
    elif(isinstance(x, basestring)):
        data_type = 'str'
        if(isinstance(x, unicode)):
            data_type = 'unicode'
    else:
        data_type = 'not defined'
    return data_type


def test_what_type():
    assert 'int' == what_type(1)
    assert 'float'  == what_type(2.2)
    assert 'str' == what_type('abc')
    assert 'unicode' == what_type(u'abc')
