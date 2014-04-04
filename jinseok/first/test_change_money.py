def change_money(won):
    return won / 1057


def test_change_money():
    assert 1 == change_money(1057)
    assert 2 == change_money(2114)
    assert 3 == change_money(3171)
