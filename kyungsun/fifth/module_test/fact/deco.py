from functools import wraps

def human(name):
    def deco(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            r = func(*args, **kwargs)
            r['name'] = name
            return r
        return wrapper
    return deco


#me(22) = human('kyungsun')(me)(22)
@human('kyungsun')
def me(age):
    return {'age':age}

@human('hyojun')
def you(age,message):
    return  {'age': age, 'message': message}
