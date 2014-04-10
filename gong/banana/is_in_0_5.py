
def in_if_il(first, last, n):
    """ 
    return first <= n and n <= last



def in_nif_il(first, last, n):
    """ 
    return first < n and n <= last



def in_if_nil(first, last, n):
    """ 
    return first <= n and n < last



def in_nif_nil(first, last, n):
    """ 
    return first < n and n < last







def test_in_if_il():
    assert in_if_il(0,5,2)

def test_in_nif_il():
    assert in_if_il(0,5,5)

def test_in_if_nil():
    assert in_if_il(0,5,2)
    assert in_if_il(0,5,5)

def test_in_nif_nil():
    assert in_if_il(0,5,2)
