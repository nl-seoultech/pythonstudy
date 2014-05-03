def func(n):
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        r = func(n - 2) + func (n - 1)
    return r


def fac(n):
    if n == 1:
        r = 1
    else:
        r = n * fac(n - 1)
    return r
