#!/usr/local/bin/python




class man(object):
	def say(self):
		print("this is a man say");

class a(man):
	def say(self):
		print("this is a say");

class b(man):
	def say(self):
		print("this is b say");

def pp(t):
	t.say();

pp(a())
pp(b())

