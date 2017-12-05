#!/usr/local/bin/python


def hahaha(x,y,z):
	if x > y:
		if y > z:
			return x;
		else:
			if x > z:
				return x;
			else:
				return z;
	else:
		if y < z:
			return z;
		else:
			return y;


print(hahaha(int(input("a:")),int(input("b:")),int(input("c:"))));

a =123123123213203311;

b = hex(a)
b = bin(a)

print(b);
