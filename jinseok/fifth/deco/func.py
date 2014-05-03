def my_cal(cal, *args):
    if cal == '+':
	    return my_sum(args)


def my_sum(*args):
    # 1 2 3 4 5 6 7 8 9 10 11
    #return reduce(lambda x, y: x + y, args)

    sum_ = 0
    for x in args:
	    sum_ += x
    return sum_
