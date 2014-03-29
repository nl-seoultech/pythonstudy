def exchange_dollor_to_won(dollor):
    return dollor * 1069.1


def test_exchange_dollor_to_won():
    assert 1069.1 == exchange_dollor_to_won(1)
