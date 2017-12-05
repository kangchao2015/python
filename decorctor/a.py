#!/usr/local/bin/python

def kkk(txt):
	def log(func):
		def wrapper(*args, **kw):
			print(" %s %s is called" % (txt,func.__name__) );
			return func(*args, **kw);
		return wrapper;
	return log;
@kkk('asdf')
def now():
	print("hahahah");

now();
