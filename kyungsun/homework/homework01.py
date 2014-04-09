# -*- coding: utf-8 -*-

def test_interest():
    assert interest(500)==20
    assert interest(1000)==40
    assert interest(1500)==67.5
    assert interest(5000)==250
    assert interest(6000)==300

def interest(deposit):
    if(deposit<=1000):
        return deposit*0.04
    elif(1000<deposit<5000):
        return deposit*0.045
    elif(5000<=deposit):
        return deposit*0.05


