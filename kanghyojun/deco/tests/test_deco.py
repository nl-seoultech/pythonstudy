from fact.deco import me, you


def test_deco():
    m = me(22)
    assert 22 == m['age']
    assert 'kanghyojun' == m['name']
    y = you(22, 'hello world')
    assert 22 == y['age']
    assert 'kyungsun' == y['name']
    assert 'hello world' == y['message']
