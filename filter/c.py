#/usr/local/bin/python


def gen(n):
	x = 0;
	while True: 
		if x == n:
			break;
		else:
			x = x + 1;
			yield x

a = int(input("aa:"));


for i in gen(a):
	print(i);
