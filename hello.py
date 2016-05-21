import functools
from types import *


def fool(text):
	print text


def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if type(text) is StringType and len(text) != 0:
				print 'begin %s %s():' % (text, func.__name__)
			else:
				print 'begin call %s():' % func.__name__

			res = func(*args, **kw)

			if type(text) is StringType and len(text) != 0:
				print 'end %s %s():' % (text, func.__name__)
			else:
				print 'end call %s():' % func.__name__
			return res
		return wrapper
	if type(text) is StringType:
		return decorator
	else:
		return decorator(text)

fool = log('execute')(fool)
# fool = log(fool)
fool('print log')
print 'git branch test'
print 'Creating a new branch is quick and simple'
print '-no-ff test'
print 'test multi-user'
