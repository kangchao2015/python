#!/usr/local/bin/python

from functools import reduce
def str1(x):
	return str(x);


a = [1,2,3,4,5,6];
b = list(range(100));


r = map(str, a);
z = map(str, b);


print(list(r), list(z));



def times(x, y):
	return int(str(x) + str(y));

print(reduce(times, list(range(0,110))));
