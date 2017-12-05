#!/usr/local/bin/python


def jc(n):
	if n==1:
		return 1;
	return n * jc(n-1);


print( jc(int(input('input:'))) );
