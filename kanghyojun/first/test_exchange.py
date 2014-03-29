def dollar_to_won(dollar):
    return dollar * 1069.1


def test_exchange_dollar_to_won():
    assert 1069.1 == dollar_to_won(1)
    assert 10691 == dollar_to_won(10)
