# import fact.func
# fact.factorial

# print fact.func.factorial(5
def factorial(n):
    #1 * 2 * 3 * 4 * ... * n
    r = 1
    for x in range(1, n + 1):
        r = r * x
    return r
