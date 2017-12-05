#!/usr/local/bin/pytho
import types

class a(object):
	def __init__(self, name, age):
		self.name = name;
		self.age = age;
#	def __len__(self):
#print("%s" % dir(a()));

#print(type(123), type('aaa'), type("aaaai"), type(a), type( a() ) );
#print(type(abs), type(fn), type(fn) == types.FunctionType, type(a), type( a() ) );


kang = a("kangchao", 27);
#print(hasattr(kang, 'name'), hasattr(kang, "asdf"));
b = getattr(kang, 'age', 100);
print("%d" % b);
setattr(kang, 'age', 1111);
b = getattr(kang, '__init__', 100);
print(b);




#print(len(kang));
