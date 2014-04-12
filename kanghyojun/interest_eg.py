from utils import bank

def test_interest()
    """
      utils/
        __init__.py
        bank.py
         |
         | def interest():
         |
         |
    """
    assert bank.interest(1000) == 4
    assert bank.interest(4999) == 4.5
