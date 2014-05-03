#-*- coding: utf-8 -*-

def my_sum(*args, **kwargs):
    print args
    return reduce(lambda x, y: x + y, args)


def my_cal(cal, *args):
    if cal == '+':
        return my_sum(*args)
