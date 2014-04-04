def tax_cal(price):
    return price * 0.15


def test_tax_cal():
    assert 150 == tax_cal(1000)
    assert 375 == tax_cal(2500)


def wage(hour):
    day_wage = hour * 5000
    return day_wage - tax_cal(day_wage)


def test_wage():
    assert 4250 == wage(1)
    assert 8500 == wage(2)
    assert 12750 == wage(3)
