# -*- coding: utf-8 -*-

def name_decorator(f):
    def wraps(age):
        print age
        return f(age)
    return wraps


@name_decorator
def my(age):
    return  {'age': age, 'name':'bong'}


def other(o_age):
    return {'o_age':o_age, 'nai':'kang'}
