def dollar_to_one(dollar):
    return dollar*1069.1


def test_exchange_dollar_to_one():
    assert 1069.1 == dollar_to_one(1)
