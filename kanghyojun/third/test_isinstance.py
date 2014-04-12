def isinst(x):
    r = 'None'
    if isinstance(x, int):
        r = 'int'
    return r


def test_isinst_test():
    assert 'int' == isinst(1)
    assert 'None' == isinst(None)
