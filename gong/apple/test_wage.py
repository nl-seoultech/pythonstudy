def wage(hour):
    sigup = 5000
    all_sigup = hour * sigup
    return all_sigup - tax(all_sigup)

def tax(money):
    return money*0.15

def test_wage():
    assert 4250 == wage(1)

def test_tax():
    assert 15 == tax(100)
    assert 30 == tax(200)
