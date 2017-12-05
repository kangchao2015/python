#!/usr/local/bin/python



def end(max):
	n,a,b = 0, 0, 1;
	while n <max:
		yield b;

		t = b;
		b = a+b;
		a = t;

		n = n+1
	return none;



ee = end(int(input('input:')));


for i in ee:
	print(i);
