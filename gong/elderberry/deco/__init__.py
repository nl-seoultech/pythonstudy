def name_decorator(f):
	def wraps(age):
		print 'hello world %d' % age 
		r['name'] = 'gong seong hyeon'
		return r
	return wraps


@name_decorator
# my = name_decorator(my)
# my (22)



""" 
.. sourcede:: python
	
	>>> my(22)
	>>> a = name_decorator('gong')
	>>> b = a(my)
	>>> c = b(22)
"""

def my(age):
	return {'age': age, 'name': 'gong'}

def other(age):
	return {'age': age, 'name': 'bong'}