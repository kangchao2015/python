#!/usr/local/bin/python



def add_end(L=[1,2,3]):
	if L is None:
		L = [];
	L.append('end')
	return L


print(add_end([1]));
print(add_end([1, 2]));
print(add_end());
print(add_end());
print(add_end());
