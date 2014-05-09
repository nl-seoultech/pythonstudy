from fact.deco import me, you 

def test_deco():
    assert 'kyungsun' == me(22)['name']
    y = you(22,'hello')
    assert 22 == y['age']
    assert 'hyojun' == y['name']
    assert 'hello' == y['message']
