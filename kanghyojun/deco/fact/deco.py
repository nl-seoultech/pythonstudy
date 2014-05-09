from functools import wraps


def human(name):
    def wrapper(f):
        @wraps(f)
        def deco(*args, **kwargs):
            r = f(*args, **kwargs)
            r['name'] = name
            return r
        return deco
    return wrapper


# me(22) -> human('kanghyojun')(me)(22)
@human('kanghyojun')
def me(age):
    """abc
    """
    return {'age': age}


@human('kyungsun')
def you(age, message):
    return {'age': age, 'message': 'hello world'}

# you(22, 'hello')
