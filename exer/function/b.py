#!/usr/local/bin/python


def kw(a, b, **pp):
	print("1:",a, "2:",b, "c:" ,pp);
	return None;


def pow(a,b=2):
	ret = 1;
	while b > 0:
		ret = a * ret;
		b = b - 1;
	
	return ret;


def add_end(L=[]):
	L.append("end");
	return L;


def aaa(*num):
	a = 0;
	for i in num:
		a = a + i * i

	print(a);
	return None;


print(add_end([]));
print(add_end([]));
print(add_end([]));
print(add_end([]));


aaa(1,2,3,4);
aaa(1,2,3,4,5,6,7,8);

l = (1,2,3,4);
p = [2,3,4,5];

aaa(*l);
aaa(*p);
ll={'asdf':r'asdf', 'zzzz':123, '2343':'asdfasdf'}
#kw('12a', 'zz', city='beijing', sdf='sdf', ll);
kw('12a', 'zz',  **ll);
