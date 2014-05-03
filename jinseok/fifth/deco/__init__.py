def name_decorator(f):
    def decorator(f):
        def wraps(age):
            print age
            return f(age)
        return wraps
    return decorator

# my = name_decorator(my)
# my(27)

@name_decorator
def my(age):
    return {'age':age, 'name': 'parkjinseok'}

def other(age):
    return {'nai':age, 'name': 'bongyong'}
