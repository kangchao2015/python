#/usr/local/bin/python

def is_odd(n):
	return n % 2 == 0;

a = filter(is_odd, list(range(10,100)));
print(list(a));
